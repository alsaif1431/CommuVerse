import streamlit as st
import asyncio
from services.utils import go_to_home
from prompts.mealPlanner import mealPlannerPrompt
from services.llmUtils import get_chat_memory, get_llm, create_agent
from dotenv import load_dotenv

load_dotenv(override=True)

st.set_page_config(page_title="Meal Planner", layout="wide", page_icon="🍽️")

st.markdown(
    "### 🍽️ Meal Planner: Your Personal Culinary Assistant!", unsafe_allow_html=True
)
st.markdown(
    """
    Welcome to your personal meal planning companion! Whether you're looking for recipe ideas, 
    need help planning your weekly meals, or want to make the most of ingredients you have on hand, 
    I'm here to help you create delicious, nutritious, and budget-friendly meal plans.
    """,
    unsafe_allow_html=True,
)

go_to_home()

key = "messages_meal_planner"
if key not in st.session_state:
    st.session_state[key] = []
    st.session_state[key].append(
        {
            "role": "assistant",
            "avatar": "🤖",
            "content": "Hello! I'm your Meal Planning Assistant. What would you like to cook today?",
        }
    )

llm = get_llm()
memory = get_chat_memory()
open_ai_agent = create_agent(mealPlannerPrompt, llm, memory)

for msg in st.session_state[key]:
    st.chat_message(msg["role"], avatar=msg["avatar"]).write(msg["content"])

if user_input := st.chat_input(
    "Tell me what ingredients you have or what you'd like to cook!"
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

    with st.spinner("Cooking up some ideas..."):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(generate_response(user_input))
        st.session_state[key].append(
            {"role": "assistant", "avatar": "🤖", "content": response}
        )
        st.chat_message("assistant", avatar="🤖").write(response)
