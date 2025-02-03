import streamlit as st
import asyncio
from services.utils import go_to_home
from prompts.hobbyHub import hobbyHubPrompt
from services.llmUtils import get_chat_memory, get_llm, create_agent
from dotenv import load_dotenv

load_dotenv(override=True)

st.set_page_config(page_title="Hobby Hub", layout="wide", page_icon="🎨")

st.markdown("### 🎨 Hobby Hub: Where Passion Meets Connection!", unsafe_allow_html=True)
st.markdown("""
        Whether you're a seasoned enthusiast or just starting out, the Hobby Hub is your space to explore, share, and connect with others who love what you love.
""", unsafe_allow_html=True)

go_to_home()

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "assistant", "avatar": "🤖", "content": "Hello there! I'm your Hobby Companion. What's on your mind today?"})

llm = get_llm()
memory = get_chat_memory()  
open_ai_agent = create_agent(hobbyHubPrompt, llm, memory)

for msg in st.session_state.messages:
    st.chat_message(msg["role"], avatar=msg["avatar"]).write(msg["content"])

if user_input := st.chat_input("Ask me about any hobby or share your thoughts!"):
    st.chat_message("user", avatar="🎃").write(user_input)
    
    st.session_state.messages.append({"role": "user", "avatar": "🎃", "content": user_input})

    async def generate_response(prompt):
        return open_ai_agent.run({"input": prompt, "history": memory.chat_memory.messages})

    with st.spinner("Thinking..."):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(generate_response(user_input))
        st.session_state.messages.append({"role": "assistant", "avatar": "🤖", "content": response})
        st.chat_message("assistant", avatar="🤖").write(response)
