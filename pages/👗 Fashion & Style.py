import streamlit as st
import asyncio
from services.utils import go_to_home
from prompts.fashionStyle import fashionStylePrompt
from services.llmUtils import get_chat_memory, get_llm, create_agent
from dotenv import load_dotenv

load_dotenv(override=True)

st.set_page_config(page_title="Fashion & Style", layout="wide", page_icon="👗")

st.markdown("### 👗 Fashion & Style: Express Your Unique Self!", unsafe_allow_html=True)
st.markdown(
    """
    Welcome to your personal style companion! Whether you're looking to develop your unique fashion identity, 
    get outfit suggestions, or learn about building a versatile wardrobe, I'm here to help you express yourself 
    through fashion with confidence and creativity. Let's celebrate your individuality!
    """,
    unsafe_allow_html=True,
)

go_to_home()

key = "messages_fashion_style"
if key not in st.session_state:
    st.session_state[key] = []
    st.session_state[key].append(
        {
            "role": "assistant",
            "avatar": "🤖",
            "content": "Hello! I'm your Fashion & Style Guide. What would you like to explore today?",
        }
    )

llm = get_llm()
memory = get_chat_memory()
open_ai_agent = create_agent(fashionStylePrompt, llm, memory)

for msg in st.session_state[key]:
    st.chat_message(msg["role"], avatar=msg["avatar"]).write(msg["content"])

if user_input := st.chat_input(
    "Ask me about style advice, outfit ideas, or building your wardrobe!"
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

    with st.spinner("Finding the perfect style advice for you..."):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(generate_response(user_input))
        st.session_state[key].append(
            {"role": "assistant", "avatar": "🤖", "content": response}
        )
        st.chat_message("assistant", avatar="🤖").write(response)
