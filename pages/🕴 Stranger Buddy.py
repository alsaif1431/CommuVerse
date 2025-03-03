import streamlit as st
import asyncio
from services.utils import go_to_home
from prompts.strangerFriend import strangerFriendPrompt  # Make sure this exists
from services.llmUtils import get_chat_memory, get_llm, create_agent
from dotenv import load_dotenv

load_dotenv(override=True)

# Configure page for Stranger Friend
st.set_page_config(page_title="Stranger Friend", layout="wide", page_icon="🤝")

st.markdown("### 🤝 Stranger Friend: Connect and Share Your Thoughts!", unsafe_allow_html=True)
st.markdown(
    """
        Welcome to Stranger Friend, a safe and welcoming space where you can share your thoughts, express yourself, 
        and have meaningful conversations with someone new. Whether you're feeling low, need someone to talk to, or just want to connect, 
        you're not alone here.
    """,
    unsafe_allow_html=True,
)

# Optionally, you can add a "go to home" button if you have one
go_to_home()

# Initialize chat message history if not present
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(
        {
            "role": "assistant",
            "avatar": "🤖",
            "content": "Hello there! I'm your Stranger Friend. What would you like to talk about today?",
        }
    )

# Get LLM and conversation memory
llm = get_llm()
memory = get_chat_memory()
open_ai_agent = create_agent(strangerFriendPrompt, llm, memory)

# Display existing chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"], avatar=msg["avatar"]).write(msg["content"])

# Get user input via chat input box
if user_input := st.chat_input("Share your thoughts or ask me anything!"):
    st.chat_message("user", avatar="🎃").write(user_input)
    st.session_state.messages.append(
        {"role": "user", "avatar": "🎃", "content": user_input}
    )

    async def generate_response(prompt):
        # Pass both user input and conversation history to the agent
        response = open_ai_agent.invoke({"input": prompt, "history": memory.chat_memory.messages})
        return response['output']

    with st.spinner("Thinking..."):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(generate_response(user_input))
        st.session_state.messages.append(
            {"role": "assistant", "avatar": "🤖", "content": response}
        )
        st.chat_message("assistant", avatar="🤖").write(response)
