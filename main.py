import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="CommuVerse", layout="wide", page_icon="assets/CommuVerse.png"
)
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

**CommuVerse** is a vibrant online platform where individuals from all walks of life can come together to explore their passions, connect with like-minded people, and engage with communities powered by cutting-edge AI technology. Whether you're looking to expand your hobbies, find study tips, boost your mental wellness, or get personalized meal plans, commuVerse offers a space for it all. Each community is tailored to provide support, resources, and interactions that enhance your everyday life—making it the ultimate hub for personal growth and collaboration.
""",
    unsafe_allow_html=True,
)
