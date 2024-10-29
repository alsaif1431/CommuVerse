import streamlit as st
from services.html_css import card_css, tag_line_css
from services.models import Community
from services.footer import display_footer

st.set_page_config(page_title="CommuVerse", layout="wide", page_icon="🌐" )
st.header(
    "🌐 Welcome to the CommuVerse: A Global Community of Communities!",
    divider=True,
)
st.markdown(
    """
    <style>
    .description {
        font-size: 20px;
        color: white;
        text-align: center;
        margin-top: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
### What is CommuVerse? 🌐

**CommuVerse** is a AI-Powered vibrant online platform where individuals from all walks of life can come together to explore their passions, connect with like-minded people, and engage with communities powered by cutting-edge AI technology. Whether you're looking to expand your hobbies, find study tips, boost your mental wellness, or get personalized meal plans, commuVerse offers a space for it all. Each community is tailored to provide support, resources, and interactions that enhance your everyday life—making it the ultimate hub for personal growth and collaboration.
""",
    unsafe_allow_html=True,
)


# Sample community data
st.session_state.communities = [
    Community("Hobby Hub", "Explore and share your hobbies with others!", "🎨"),
    Community("Study & Life Hacks", "Boost your productivity with life hacks!", "📚"),
    Community(
        "Mental Health & Wellness",
        "Find mindfulness practices and self-care tips.",
        "🧘‍♀️",
    ),
    Community("Meal Planner", "Generate meal plans based on your ingredients!", "🍽️"),
    Community(
        "Mindfulness & Meditation", "Learn mindfulness techniques to stay calm.", "🧘‍♂️"
    ),
    Community("Finance for Beginners", "Start managing your finances smartly.", "💰"),
    Community("Beauty & Skincare", "Explore beauty tips and skincare routines.", "💅"),
    Community(
        "Event Finder", "Discover fun events and activities happening near you.", "🎉"
    ),
    Community(
        "Fashion & Style", "Get personalized fashion advice based on your mood!", "👗"
    ),
]


def display_communities():
    st.markdown(
        tag_line_css,
        unsafe_allow_html=True,
    )

    st.markdown(card_css, unsafe_allow_html=True)

    for i in range(0, len(st.session_state.communities), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(st.session_state.communities):
                community = st.session_state.communities[i + j]
                with cols[j]:
                    button_id = f"card-button-{community.name.replace(' ', '-')}"
                    card_html = f"""
                    <button class='card-button' id='{button_id}' onclick="window.location.reload(true);">
                        <h3>{community.emoji} {community.name}</h3>
                        <p>{community.description}</p>
                    </button>
                    <script>
                    document.getElementById('{button_id}').onclick = function() {{
                        window.parent.postMessage({{"type": "setSessionState", "key": "page", "value": "{community.name}"}}, "*");
                    }};
                    </script>
                    """
                    st.markdown(card_html, unsafe_allow_html=True)


display_communities()

if "page" in st.session_state:
    st.write(f"### Welcome to the {st.session_state.page} page!")
    st.write("This is where you would add your community-specific content.")


display_footer()
