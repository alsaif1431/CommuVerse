import streamlit as st
import asyncio
from services.utils import go_to_home
from langchain_community.chat_message_histories import (
    StreamlitChatMessageHistory,
)
from prompts.hobbyHub import hobbyHubPrompt
from providers.llmUtils import get_chat_memory,get_llm,create_agent
from dotenv import load_dotenv
load_dotenv(override=True)

st.set_page_config(page_title="Hobby Hub", layout="wide", page_icon="🎨")

st.markdown("### 🎨Hobby Hub: Where Passion Meets Connection!", unsafe_allow_html=True)
st.markdown("""
        Whether you're a seasoned enthusiast or just starting out, the Hobby Hub is your space to explore, share, and connect with others who love what you love.
""", unsafe_allow_html=True)

go_to_home()

msgs = StreamlitChatMessageHistory(key="hobby_hub_messages")

if len(msgs.messages) == 0:
    msgs.add_ai_message("Hello there! I'm your Hobby Companion. What's on your mind today?")
    
    
llm = get_llm()
memory = get_chat_memory("hobby_hub_messages")
open_ai_agent = create_agent(hobbyHubPrompt, llm, memory)

for msg in msgs.messages:
    st.chat_message(msg.type).write(msg.content)

if prompt := st.chat_input("Ask me about any hobby or share your thoughts!"):
    st.chat_message("human").write(prompt)
    
    async def generate_response(prompt):
        response = open_ai_agent.run({"input": prompt, "history": memory.chat_memory.messages})
        return response
    
    with st.spinner("Thinking..."):
        response = asyncio.run(generate_response(prompt))
        msgs.add_ai_message(response)  # Save response to chat history
        st.chat_message("ai").write(response)
        
        
