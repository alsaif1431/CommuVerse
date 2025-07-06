import streamlit as st
import asyncio
from services.utils import go_to_home
from prompts.mentalHealthWellness import mentalHealthWellnessPrompt
from services.llmUtils import get_chat_memory, get_llm, create_agent
from dotenv import load_dotenv

load_dotenv(override=True)

st.set_page_config(
    page_title="Mental Health & Wellness", layout="wide", page_icon="🧘‍♀️"
)

st.markdown(
    "### 🧘‍♀️ Mental Health & Wellness: Your Journey to Well-being!",
    unsafe_allow_html=True,
)
st.markdown(
    """
    Welcome to your safe space for mental health and wellness support. Whether you're looking for 
    self-care techniques, mindfulness practices, or just need someone to talk to, I'm here to provide 
    gentle guidance and support on your journey toward better mental health and overall well-being.
    """,
    unsafe_allow_html=True,
)

go_to_home()

key = "messages_mental_health_wellness"
if key not in st.session_state:
    st.session_state[key] = []
    st.session_state[key].append(
        {
            "role": "assistant",
            "avatar": "🤖",
            "content": "Hello! I'm your Mental Health & Wellness Guide. How are you feeling today?",
        }
    )

llm = get_llm()
memory = get_chat_memory()
open_ai_agent = create_agent(mentalHealthWellnessPrompt, llm, memory)

for msg in st.session_state[key]:
    st.chat_message(msg["role"], avatar=msg["avatar"]).write(msg["content"])

if user_input := st.chat_input(
    "Share your thoughts or ask about self-care techniques..."
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

    with st.spinner("Taking a moment to reflect..."):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(generate_response(user_input))
        st.session_state[key].append(
            {"role": "assistant", "avatar": "🤖", "content": response}
        )
        st.chat_message("assistant", avatar="🤖").write(response)
