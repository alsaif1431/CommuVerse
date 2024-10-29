import streamlit as st
from services.html_css import card_css, tag_line_css
from services.models import Community
from services.footer import display_footer
from streamlit_card import card

st.set_page_config(page_title="CommuVerse", layout="wide", page_icon="🌐")
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



# Sample community data
st.session_state.communities = [
    Community("Hobby Hub", "Explore and share your hobbies with others!", "🎨"),
    Community("Study & Life Hacks", "Boost your productivity with life hacks!", "📚"),
    Community("Mental Health & Wellness", "Find mindfulness practices and self-care tips.", "🧘‍♀️"),
    Community("Meal Planner", "Generate meal plans based on your ingredients!", "🍽️"),
    Community("Mindfulness & Meditation", "Learn mindfulness techniques to stay calm.", "🧘‍♂️"),
    Community("Finance for Beginners", "Start managing your finances smartly.", "💰"),
    Community("Beauty & Skincare", "Explore beauty tips and skincare routines.", "💅"),
    Community("Event Finder", "Discover fun events and activities happening near you.", "🎉"),
    Community("Fashion & Style", "Get personalized fashion advice based on your mood!", "👗"),
]

# Display community cards using streamlit-card
def display_communities():
    st.markdown(tag_line_css, unsafe_allow_html=True)
    
    # Loop through communities in rows of 3
    for i in range(0, len(st.session_state.communities), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(st.session_state.communities):
                community = st.session_state.communities[i + j]
                with cols[j]:
                    if card(
                        title=f"{community.emoji} {community.name}",
                        text=community.description,
                        # image="https://via.placeholder.com/300",
                        key=community.name,
                        styles={
                        "card": {
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                            "padding":'0px',
                            "width":"100%",
                            "margin":"3px",
                            "border-radius": "10px",
                            "background-color": "#f0f2f6",
                        },
                        "text": {
                            "font-family": "Times New Roman",
                        }
                    }
                    ):
                        st.session_state.page = community.name

display_communities()

# Display content based on the selected community
if "page" in st.session_state:
    st.write(f"### Welcome to the {st.session_state.page} page!")
    st.write("This is where you would add your community-specific content.")

display_footer()

