import streamlit as st
import asyncio
from services.utils import go_to_home
from prompts.studyLifeHacks import studyLifeHacksPrompt
from services.llmUtils import get_chat_memory, get_llm, create_agent
from dotenv import load_dotenv

load_dotenv(override=True)

st.set_page_config(page_title="Study & Life Hacks", layout="wide", page_icon="📚")

st.markdown(
    "### 📚 Study & Life Hacks: Boost Your Productivity!", unsafe_allow_html=True
)
st.markdown(
    """
    Welcome to your productivity companion! Whether you're looking to improve your study habits, 
    discover clever life hacks, or boost your overall efficiency, I'm here to share proven techniques 
    and innovative solutions that will help you work smarter, not harder.
    """,
    unsafe_allow_html=True,
)

go_to_home()

key = "messages_study_life_hack"
if key not in st.session_state:
    st.session_state[key] = []
    st.session_state[key].append(
        {
            "role": "assistant",
            "avatar": "🤖",
            "content": "Hello! I'm your Study & Life Hacks Mentor. What area would you like to improve today?",
        }
    )

llm = get_llm()
memory = get_chat_memory()
open_ai_agent = create_agent(studyLifeHacksPrompt, llm, memory)

for msg in st.session_state[key]:
    st.chat_message(msg["role"], avatar=msg["avatar"]).write(msg["content"])

if user_input := st.chat_input(
    "Ask me about study techniques, productivity tips, or life hacks!"
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

    with st.spinner("Finding the perfect hack for you..."):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(generate_response(user_input))
        st.session_state[key].append(
            {"role": "assistant", "avatar": "🤖", "content": response}
        )
        st.chat_message("assistant", avatar="🤖").write(response)
