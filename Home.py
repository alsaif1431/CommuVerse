import os
import streamlit as st
from services.html_css import styles, tag_line_css
from services.models import Community
from services.footer import display_footer
from services.sidebar import display_about_me, display_quick_stats
from streamlit_card import card
from streamlit_extras.switch_page_button import switch_page
from services.utils import page_name_mapping

st.set_page_config(
    page_title="CommuVerse",
    layout="wide",
    page_icon="🌐",
    initial_sidebar_state="collapsed",
)
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
    Community(
        "🎨 Hobby Hub",
        "Explore and share your hobbies with others!",
        "Hobby Hub",
        "https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=400&q=80",
    ),
    Community(
        "📚 Study & Life Hack",
        "Boost your productivity with life hacks!",
        "Study & Life Hack",
        "https://images.unsplash.com/photo-1513258496099-48168024aec0?auto=format&fit=crop&w=400&q=80",
    ),
    Community(
        "🧘‍♀️ Mental Health & Wellness",
        "Find mindfulness practices and self-care tips.",
        "Mental Health & Wellness",
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=400&q=80",
    ),
    Community(
        "🍽️ Meal Planner",
        "Generate meal plans based on your ingredients!",
        "Meal Planner",
        "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=400&q=80",
    ),
    Community(
        "🕴 Stranger Buddy",
        "Learn mindfulness techniques to stay calm.",
        "Stranger Buddy",
        "https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=400&q=80",
    ),
    Community(
        "💰 Finance for Beginners",
        "Start managing your finances smartly.",
        "Finance for Beginners",
        "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=400&q=80",
    ),
    Community(
        "💅 Beauty & Skincare",
        "Explore beauty tips and skincare routines.",
        "Beauty & Skincare",
        "https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?auto=format&fit=crop&w=400&q=80",
    ),
    Community(
        "🎉 Event Finder",
        "Discover fun events and activities happening near you.",
        "Event Finder",
        "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=400&q=80",
    ),
    Community(
        "👗 Fashion & Style",
        "Get personalized fashion advice based on your mood!",
        "Fashion & Style",
        "https://images.unsplash.com/photo-1512436991641-6745cdb1723f?auto=format&fit=crop&w=400&q=80",
    ),
]


# Display About Me section in sidebar
display_about_me()


def display_communities():
    st.markdown(tag_line_css, unsafe_allow_html=True)
    card_style = """
        <style>
        .commuverse-card {
            box-shadow: 0 4px 16px rgba(0,0,0,0.10);
            border-radius: 18px;
            overflow: hidden;
            background: #fff;
            transition: box-shadow 0.2s, transform 0.2s;
            margin-bottom: 24px;
            cursor: pointer;
            position: relative;
        }
        .commuverse-card:hover {
            box-shadow: 0 8px 32px rgba(0,0,0,0.18);
            transform: translateY(-2px) scale(1.03);
        }
        .commuverse-card-img {
            width: 100%;
            height: 180px;
            object-fit: cover;
            display: block;
            filter: brightness(1.18) contrast(1.15) saturate(1.12);
            border: 2px solid #f3f3f3;
            background: #fff;
        }
        .commuverse-card-title {
            font-size: 1.1rem;
            font-weight: 600;
            margin: 12px 0 0 0;
            text-align: center;
            color: #222;
        }
        .commuverse-card-desc {
            font-size: 0.97rem;
            color: #555;
            text-align: center;
            margin: 8px 0 16px 0;
        }
        </style>
    """
    st.markdown(card_style, unsafe_allow_html=True)

    for i in range(0, len(communities), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(communities):
                community = communities[i + j]
                with cols[j]:
                    card_html = f"""
                    <div class="commuverse-card">
                        <img src="{community.image_url}" class="commuverse-card-img" alt="{community.name}" />
                        <div class="commuverse-card-title">{community.name}</div>
                        <div class="commuverse-card-desc">{community.description}</div>
                    </div>
                    """
                    st.markdown(card_html, unsafe_allow_html=True)
                    page_to_navigate = page_name_mapping.get(community.page_name)
                    if page_to_navigate:
                        st.markdown(
                            '<div style="display: flex; justify-content: center; margin-bottom: 16px;">',
                            unsafe_allow_html=True,
                        )
                        if st.button(
                            f"Go to {community.name}", key=f"btn_{community.name}_{i+j}"
                        ):
                            switch_page(page_to_navigate)
                        st.markdown("</div>", unsafe_allow_html=True)


display_communities()
display_footer()
