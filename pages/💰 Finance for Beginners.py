import streamlit as st
import asyncio
from services.utils import go_to_home
from prompts.financeBeginners import financeBeginnersPrompt
from services.llmUtils import get_chat_memory, get_llm, create_agent
from dotenv import load_dotenv

load_dotenv(override=True)

st.set_page_config(page_title="Finance for Beginners", layout="wide", page_icon="💰")

st.markdown(
    "### 💰 Finance for Beginners: Your Path to Financial Freedom!",
    unsafe_allow_html=True,
)
st.markdown(
    """
    Welcome to your financial education journey! Whether you're just starting to learn about money, 
    want to build better financial habits, or need help understanding personal finance concepts, 
    I'm here to make financial education accessible, practical, and less intimidating.
    """,
    unsafe_allow_html=True,
)

go_to_home()

key = "messages_finance_beginners"
if key not in st.session_state:
    st.session_state[key] = []
    st.session_state[key].append(
        {
            "role": "assistant",
            "avatar": "🤖",
            "content": "Hello! I'm your Finance Mentor for Beginners. What would you like to learn about today?",
        }
    )

llm = get_llm()
memory = get_chat_memory()
open_ai_agent = create_agent(financeBeginnersPrompt, llm, memory)

for msg in st.session_state[key]:
    st.chat_message(msg["role"], avatar=msg["avatar"]).write(msg["content"])

if user_input := st.chat_input(
    "Ask me about budgeting, saving, investing, or any financial topic!"
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

    with st.spinner("Calculating the best financial advice for you..."):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(generate_response(user_input))
        st.session_state[key].append(
            {"role": "assistant", "avatar": "🤖", "content": response}
        )
        st.chat_message("assistant", avatar="🤖").write(response)
