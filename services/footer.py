import streamlit as st


def display_footer():
    # Custom HTML for the footer
    st.markdown(
        """
        <hr style="border:1px solid #e0e0e0; margin-top: 50px;">
        <div style="text-align: center; padding: 10px; color: #4a4a4a;">
            <p style="font-size: 16px; font-weight: bold;">Connect with me</p>
            <a href="https://www.instagram.com/_al_sxif_/" target="_blank" style="margin-right: 15px;">
                <img src="https://img.icons8.com/ios-filled/50/4a4a4a/instagram-new.png" alt="Instagram" style="width:30px; height:30px;">
            </a>
            <a href="https://snapchat.com/t/wNqTJk9Q" target="_blank" style="margin-right: 15px;">
                <img src="https://img.icons8.com/ios-filled/50/4a4a4a/snapchat.png" alt="Snapchat" style="width:30px; height:30px;">
            </a>
            <a href="https://www.linkedin.com/in/saif-pasha-59643b197/" target="_blank" style="margin-right: 15px;">
                <img src="https://img.icons8.com/ios-filled/50/4a4a4a/linkedin.png" alt="LinkedIn" style="width:30px; height:30px;">
            </a>
            <a href="mailto:yourmail@example.com" target="_blank">
                <img src="https://img.icons8.com/ios-filled/50/4a4a4a/gmail.png" alt="Email" style="width:30px; height:30px;">
            </a>
            <p style="font-size: 14px; margin-top: 10px;">&copy; 2023 commuVerse. All rights reserved.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
