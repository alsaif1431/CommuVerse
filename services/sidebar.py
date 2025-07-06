import streamlit as st
from services.profile_config import PROFILE_CONFIG


def display_about_me():
    """
    Display About Me section in the sidebar with social media links and professional information
    """

    # About Me Section
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"### 👨‍💻 About {PROFILE_CONFIG['name']}")

    # Profile image placeholder (you can replace with your actual image)
    if PROFILE_CONFIG["profile_image"]["image_url"]:
        st.sidebar.image(PROFILE_CONFIG["profile_image"]["image_url"], width=80)
    else:
        st.sidebar.markdown(
            f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="width: 80px; height: 80px; border-radius: 50%; background: linear-gradient(45deg, #667eea 0%, #764ba2 100%); 
                            display: flex; align-items: center; justify-content: center; margin: 0 auto 10px auto; color: white; font-size: 24px; font-weight: bold;">
                    {PROFILE_CONFIG['profile_image']['emoji']}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Professional Summary
    st.sidebar.markdown(
        f"""
        **{PROFILE_CONFIG['title']}** 🚀
        
        {PROFILE_CONFIG['summary']}
        """
    )

    # Key Skills
    st.sidebar.markdown("**🛠️ Skills & Technologies:**")
    skills_text = f"""
    • **Languages:** {', '.join(PROFILE_CONFIG['skills']['languages'])}
    • **Frameworks:** {', '.join(PROFILE_CONFIG['skills']['frameworks'])}
    • **Cloud:** {', '.join(PROFILE_CONFIG['skills']['cloud'])}
    • **AI/ML:** {', '.join(PROFILE_CONFIG['skills']['ai_ml'])}
    • **Databases:** {', '.join(PROFILE_CONFIG['skills']['databases'])}
    • **Tools:** {', '.join(PROFILE_CONFIG['skills']['tools'])}
    """
    st.sidebar.markdown(skills_text)

    # Current Focus
    st.sidebar.markdown("**🎯 Currently Working On:**")
    focus_text = "\n".join([f"• {item}" for item in PROFILE_CONFIG["current_focus"]])
    st.sidebar.markdown(focus_text)

    # About Me Paragraph
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🌟 About Me")
    st.sidebar.markdown(
        f"""
        {PROFILE_CONFIG['about_paragraph']}
        """
    )

    # Contact
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📧 Get In Touch")
    st.sidebar.markdown(
        f"""
        **Email:** {PROFILE_CONFIG['contact']['email']}  
        **Location:** {PROFILE_CONFIG['contact']['location']}  
        **Available for:** {PROFILE_CONFIG['contact']['availability']}
        """
    )


def display_quick_stats():
    """
    Display quick statistics in the sidebar
    """
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 Quick Stats")

    col1, col2 = st.sidebar.columns(2)

    with col1:
        st.metric("Years Experience", PROFILE_CONFIG["stats"]["years_experience"])
        st.metric("Projects Built", PROFILE_CONFIG["stats"]["projects_built"])

    with col2:
        st.metric("Communities", PROFILE_CONFIG["stats"]["communities"])
        st.metric("Happy Users", PROFILE_CONFIG["stats"]["happy_users"])
