import streamlit as st
import asyncio
from services.utils import go_to_home
from prompts.beautySkincare import beautySkincarePrompt
from services.llmUtils import get_chat_memory, get_llm, create_agent
from dotenv import load_dotenv

load_dotenv(override=True)

st.set_page_config(page_title="Beauty & Skincare", layout="wide", page_icon="💅")

st.markdown(
    "### 💅 Beauty & Skincare: Your Personal Beauty Guide!", unsafe_allow_html=True
)
st.markdown(
    """
    Welcome to your beauty and skincare companion! Whether you're looking for personalized skincare routines, 
    beauty tips, or product recommendations, I'm here to help you discover routines that work for your unique 
    skin type and beauty preferences. Let's focus on feeling confident and taking care of yourself!
    """,
    unsafe_allow_html=True,
)

go_to_home()

key = "messages_beauty_skincare"
if key not in st.session_state:
    st.session_state[key] = []
    st.session_state[key].append(
        {
            "role": "assistant",
            "avatar": "🤖",
            "content": "Hello! I'm your Beauty & Skincare Guide. What would you like to know about today?",
        }
    )

llm = get_llm()
memory = get_chat_memory()
open_ai_agent = create_agent(beautySkincarePrompt, llm, memory)

for msg in st.session_state[key]:
    st.chat_message(msg["role"], avatar=msg["avatar"]).write(msg["content"])

if user_input := st.chat_input(
    "Ask me about skincare routines, beauty tips, or product recommendations!"
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

    with st.spinner("Finding the perfect beauty advice for you..."):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(generate_response(user_input))
        st.session_state[key].append(
            {"role": "assistant", "avatar": "🤖", "content": response}
        )
        st.chat_message("assistant", avatar="🤖").write(response)
