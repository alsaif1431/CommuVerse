import streamlit as st
import asyncio
import os
import json
import uuid
from urllib.parse import urlencode
from services.utils import go_to_home
from prompts.hobbyHub import hobbyHubPrompt
from services.llmUtils import get_chat_memory, get_llm, create_agent
from dotenv import load_dotenv

load_dotenv(override=True)

st.set_page_config(page_title="Hobby Hub", layout="wide", page_icon="🎨")

st.markdown("### 🎨 Hobby Hub: Where Passion Meets Connection!", unsafe_allow_html=True)
st.markdown(
    """
        Whether you're a seasoned enthusiast or just starting out, the Hobby Hub is your space to explore, share, and connect with others who love what you love.
""",
    unsafe_allow_html=True,
)

go_to_home()


# --- Persistent, shareable chat logic ---
def get_chat_id():
    params = st.query_params
    chat_id = params.get("chat_id")
    if not chat_id:
        chat_id = str(uuid.uuid4())
        st.query_params["chat_id"] = chat_id
    return chat_id


def get_chat_file(chat_id):
    return os.path.join("chats", f"chat_{chat_id}.json")


chat_id = get_chat_id()
chat_file = get_chat_file(chat_id)

# Load chat history from file or initialize
if os.path.exists(chat_file):
    with open(chat_file, "r", encoding="utf-8") as f:
        chat_history = json.load(f)
else:
    chat_history = [
        {
            "role": "assistant",
            "avatar": "🤖",
            "content": "Hello there! I'm your Hobby Companion. What's on your mind today?",
        }
    ]

# Display chat history
for msg in chat_history:
    st.chat_message(msg["role"], avatar=msg["avatar"]).write(msg["content"])

# Share chat link button
base_url = "https://community-verse.streamlit.app/🎨%20Hobby%20Hub"
share_url = f"{base_url}?chat_id={chat_id}"
st.button(
    "🔗 Share Chat",
    on_click=st.write,
    args=(f"Link copied! {share_url}",),
    help="Copy this link to invite a friend to this chat.",
)

llm = get_llm()
memory = get_chat_memory()
open_ai_agent = create_agent(hobbyHubPrompt, llm, memory)

if user_input := st.chat_input("Ask me about any hobby or share your thoughts!"):
    st.chat_message("user", avatar="🎃").write(user_input)
    chat_history.append({"role": "user", "avatar": "🎃", "content": user_input})

    async def generate_response(prompt):
        response = open_ai_agent.invoke(
            {"input": prompt, "history": memory.chat_memory.messages}
        )
        return response["output"]

    with st.spinner("Thinking..."):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(generate_response(user_input))
        chat_history.append({"role": "assistant", "avatar": "🤖", "content": response})
        st.chat_message("assistant", avatar="🤖").write(response)

    # Save updated chat history
    with open(chat_file, "w", encoding="utf-8") as f:
        json.dump(chat_history, f, ensure_ascii=False, indent=2)
else:
    # Save chat history on page load (for new chats)
    if not os.path.exists(chat_file):
        with open(chat_file, "w", encoding="utf-8") as f:
            json.dump(chat_history, f, ensure_ascii=False, indent=2)
