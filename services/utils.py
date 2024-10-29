import streamlit as st
from streamlit_extras.switch_page_button import switch_page

page_name_mapping = {
    "Hobby Hub": "Hobby Hub",
    "Study & Life Hack": "Study & Life Hack",
    "Mental Health & Wellness": "Mental Health & Wellness",
    "Meal Planner": "Meal Planner",
    "Mindfulness & Meditation": "Mindfulness & Meditation",
    "Finance for Beginners": "Finance for Beginners",
    "Beauty & Skincare": "Beauty & Skincare",
    "Event Finder": "Event Finder",
    "Fashion & Style": "Fashion & Style",
    "Home": "Home"
}


def go_to_home():
    page_to_navigate = page_name_mapping.get("Home")
    Home = st.button("🏠 Home")
    if Home:
        switch_page(page_to_navigate)