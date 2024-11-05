import os
import streamlit as st
from services.html_css import styles, tag_line_css
from services.models import Community
from services.footer import display_footer
from streamlit_card import card
from streamlit_extras.switch_page_button import switch_page
from services.utils import page_name_mapping

st.set_page_config(page_title="CommuVerse", layout="wide", page_icon="🌐",initial_sidebar_state="collapsed")
st.header(
    "🌐 Welcome to the CommuVerse: A Global Community of Communities!",
    divider=True,
)

st.markdown(
    """
### What is CommuVerse? 🌐

**CommuVerse** is a AI-Powered vibrant online platform where individuals from all walks of life can come together to explore their passions, connect with like-minded people, and engage with communities powered by cutting-edge AI technology. Whether you're looking to expand your hobbies, find study tips, boost your mental wellness, or get personalized meal plans, commuVerse offers a space for it all. Each community is tailored to provide support, resources, and interactions that enhance your everyday life—making it the ultimate hub for personal growth and collaboration.
""",
    unsafe_allow_html=True,
)

communities = [
    Community("🎨 Hobby Hub", "Explore and share your hobbies with others!", "hobby_hub"),
    Community("📚 Study & Life Hack", "Boost your productivity with life hacks!", "study_life_hacks"),
    Community("🧘‍♀️ Mental Health & Wellness", "Find mindfulness practices and self-care tips.", "mental_health_wellness"),
    Community("🍽️ Meal Planner", "Generate meal plans based on your ingredients!", "meal_planner"),
    Community("🧘‍♂️ Mindfulness & Meditation", "Learn mindfulness techniques to stay calm.", "mindfulness_meditation"),
    Community("💰 Finance for Beginners", "Start managing your finances smartly.", "finance_for_beginners"),
    Community("💅 Beauty & Skincare", "Explore beauty tips and skincare routines.", "beauty_skincare"),
    Community("🎉 Event Finder", "Discover fun events and activities happening near you.", "event_finder"),
    Community("👗 Fashion & Style", "Get personalized fashion advice based on your mood!", "fashion_style"),
]


st.sidebar.write("About us?.")

communities = [
    Community("🎨 Hobby Hub", "Explore and share your hobbies with others!", "Hobby Hub", os.path.join("assets", "HobbyHub.jpg")),
    # Community("📚 Study & Life Hack", "Boost your productivity with life hacks!", "Study & Life Hack", "https://example.com/study_life_hack.jpg"),
    # Community("🧘‍♀️ Mental Health & Wellness", "Find mindfulness practices and self-care tips.", "Mental Health & Wellness", "https://example.com/mental_health_wellness.jpg"),
    # Community("🍽️ Meal Planner", "Generate meal plans based on your ingredients!", "Meal Planner", "https://example.com/meal_planner.jpg"),
    # Community("🧘‍♂️ Mindfulness & Meditation", "Learn mindfulness techniques to stay calm.", "Mindfulness & Meditation", "https://example.com/mindfulness_meditation.jpg"),
    # Community("💰 Finance for Beginners", "Start managing your finances smartly.", "Finance for Beginners", "https://example.com/finance_for_beginners.jpg"),
    # Community("💅 Beauty & Skincare", "Explore beauty tips and skincare routines.", "Beauty & Skincare", "https://example.com/beauty_skincare.jpg"),
    # Community("🎉 Event Finder", "Discover fun events and activities happening near you.", "Event Finder", "https://example.com/event_finder.jpg"),
    # Community("👗 Fashion & Style", "Get personalized fashion advice based on your mood!", "Fashion & Style", "https://example.com/fashion_style.jpg"),
]




def display_communities():
    st.markdown(tag_line_css, unsafe_allow_html=True)
    
    for i in range(0, len(communities), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(communities):
                community = communities[i + j]
                with cols[j]:
                    if card(
                        title=community.name,
                        text=community.description,
                         image=None,  ## THIS HAS TO BE DYNAMIC
                        key=community.name,
                        styles=styles
                    ):
                        page_to_navigate = page_name_mapping.get(community.page_name)
                        if page_to_navigate:
                            switch_page(page_to_navigate)

display_communities()
display_footer()