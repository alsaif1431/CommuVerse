import streamlit as st
from services.html_css import styles, tag_line_css
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

#NEED TO ADD IMAGES ALONG W THE 2 THINGS
communities = [
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

st.sidebar.write("Here are some of our communities. Click on a community to get started.")

def display_communities():
    st.markdown(tag_line_css, unsafe_allow_html=True)
    
    for i in range(0, len(communities), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(communities):
                community =communities[i + j]
                with cols[j]:
                    if card(
                        title=f"{community.emoji} {community.name}",
                        text=community.description,
                        # image="https://via.placeholder.com/300",
                        key=community.name,
                        styles=styles
                    ):
                        # Set query parameters to navigate to the selected page
                        st.experimental_set_query_params(page=community.name.replace(" ", "_"))


display_communities()
display_footer()

