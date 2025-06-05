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
    Community("🕴 Stranger Buddy", "Learn mindfulness techniques to stay calm.", "stranger_buddy"),
    Community("💰 Finance for Beginners", "Start managing your finances smartly.", "finance_for_beginners"),
    Community("💅 Beauty & Skincare", "Explore beauty tips and skincare routines.", "beauty_skincare"),
    Community("🎉 Event Finder", "Discover fun events and activities happening near you.", "event_finder"),
    Community("👗 Fashion & Style", "Get personalized fashion advice based on your mood!", "fashion_style"),
] 


st.sidebar.write("About us?.")

communities = [
    Community("🎨 Hobby Hub", "Explore and share your hobbies with others!", "Hobby Hub","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpPLjjA_zzqTrJwIRjAMuKvxN9PFB-rUwvVw&s"),
    Community("📚 Study & Life Hack", "Boost your productivity with life hacks!", "Study & Life Hack", "https://media.istockphoto.com/id/895791500/photo/life-hacks-text-on-a-display-on-blue-and-pink-bright-background.jpg?s=612x612&w=0&k=20&c=lDzCbYlQEmVXrvKoosI8_WENsGyMXUrjq7ca074e7LI="),
    Community("🧘‍♀️ Mental Health & Wellness", "Find mindfulness practices and self-care tips.", "Mental Health & Wellness", "https://3.files.edl.io/10ec/20/10/19/162749-95b87ddf-eae5-436c-a278-06f1bbba1019.jpg"),
    Community("🍽️ Meal Planner", "Generate meal plans based on your ingredients!", "Meal Planner", "https://cdn.prod.website-files.com/602eb6861cd59a7ac7908779/64ef83859029c31799e2330b_Meal%20Plan.png"),
    Community("🕴 Stranger Buddy", "Learn mindfulness techniques to stay calm.", "Stranger Buddy", "https://i.pinimg.com/736x/2a/c0/8d/2ac08dcb7e4db5f6cb11a85678f250e4.jpg"),
    Community("💰 Finance for Beginners", "Start managing your finances smartly.", "Finance for Beginners", "https://www.shutterstock.com/image-vector/finance-text-creative-drawing-charts-260nw-321267758.jpg"),
    Community("💅 Beauty & Skincare", "Explore beauty tips and skincare routines.", "Beauty & Skincare", "https://www.shutterstock.com/image-vector/skin-care-hand-drawn-lettering-260nw-1600297144.jpg"),
    Community("🎉 Event Finder", "Discover fun events and activities happening near you.", "Event Finder", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMZQXbwqYppE5-4KgHWLj6SioYP07o3xPmSQ&s"),
    Community("👗 Fashion & Style", "Get personalized fashion advice based on your mood!", "Fashion & Style", "https://www.shutterstock.com/image-vector/fashion-style-logo-260nw-378088279.jpg"),
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
                        title='',
                        text='',
                        key=community.name,
                        image=community.image_url, 
                        # styles=styles,
                    ):
                        page_to_navigate = page_name_mapping.get(community.page_name)
                        if page_to_navigate:
                            switch_page(page_to_navigate)

display_communities()
display_footer()
