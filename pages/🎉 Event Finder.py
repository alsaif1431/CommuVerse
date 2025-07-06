import streamlit as st
import asyncio
from services.utils import go_to_home
from prompts.eventFinder import eventFinderPrompt
from services.llmUtils import get_chat_memory, get_llm, create_agent
from dotenv import load_dotenv

load_dotenv(override=True)

st.set_page_config(page_title="Event Finder", layout="wide", page_icon="🎉")

st.markdown(
    "### 🎉 Event Finder: Discover Amazing Experiences!", unsafe_allow_html=True
)
st.markdown(
    """
    Welcome to your event discovery companion! Whether you're looking for local activities, planning a special occasion, 
    or just want to explore new experiences, I'm here to help you find exciting events that match your interests, 
    budget, and schedule. Let's make every day an adventure!
    """,
    unsafe_allow_html=True,
)

go_to_home()

key = "messages_event_finder"
if key not in st.session_state:
    st.session_state[key] = []
    st.session_state[key].append(
        {
            "role": "assistant",
            "avatar": "🤖",
            "content": "Hello! I'm your Event Discovery Guide. What type of events are you looking for today?",
        }
    )

llm = get_llm()
memory = get_chat_memory()
open_ai_agent = create_agent(eventFinderPrompt, llm, memory)

for msg in st.session_state[key]:
    st.chat_message(msg["role"], avatar=msg["avatar"]).write(msg["content"])

if user_input := st.chat_input(
    "Tell me what events you're interested in or what you're planning!"
):
    st.chat_message("user", avatar="🎃").write(user_input)

    st.session_state[key].append(
        {"role": "user", "avatar": "🎃", "content": user_input}
    )

    async def generate_response(prompt):
        response = open_ai_agent.invoke(
            {"input": prompt, "history": memory.chat_memory.messages}
        )
        return response["output"]

    with st.spinner("Searching for the perfect events for you..."):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(generate_response(user_input))
        st.session_state[key].append(
            {"role": "assistant", "avatar": "🤖", "content": response}
        )
        st.chat_message("assistant", avatar="🤖").write(response)
