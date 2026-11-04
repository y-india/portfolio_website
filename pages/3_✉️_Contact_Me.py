import streamlit as st
import base64
from utils.theme import apply_theme
# Page setup
st.set_page_config(page_title="Contact Me | Yuvraj", layout="wide")
apply_theme()

# ------------------- Background -------------------
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url('https://raw.githubusercontent.com/y-india/images_hosting/refs/heads/main/SELECTED_background_for_portfolio.png');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------- Contact box styling -------------------
st.markdown("""
<style>
.contact-box, .logo-box {
    background-color: rgba(0,0,0,0.75);
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    width: 380px;
    margin: auto;
    color: white;
}
.contact-box h2 {
    color: #4EC8F4;
    margin-bottom: 15px;
}
.contact-links p {
    font-size: 18px;
    margin: 10px 0;
}
.contact-links a {
    color: #4EC8F4 !important;
    font-weight: bold;
    text-decoration: none;
}
.logo-box img {
    width: 50px;
    margin: 0 15px;
    filter: brightness(0) invert(1);
}
</style>
""", unsafe_allow_html=True)

# ------------------- Contact Info -------------------
st.markdown("""
<div class="contact-box">
    <h2>📬 Contact Me</h2>
    <p>I’m always exploring AI, Python, and data science projects. 
       If you have ideas to collaborate, discuss experiments, or share insights, feel free to reach out!</p>
    <div class="contact-links">
        <p><b>Email:</b> <a href="mailto:y.india.main@gmail.com">y.india.main@gmail.com</a></p>
        <p><b>GitHub:</b> <a href="https://github.com/y-india" target="_blank">github.com/y-india (20+ repos inculding projects , websites , notes and stuff codes)</a></p>
        <p><b>LinkedIn:</b> <a href="https://www.linkedin.com/in/yuvraj-indian" target="_blank">linkedin.com/in/yuvraj-indian (Consistent Posting with Learnings)</a></p>
        <p><b>Streamlit Portfolio:</b> <a href="https://yuvirana.streamlit.app" target="_blank">Self Made Portfolio (View Projects and stuff)</a></p>
    </div>
    <p style="margin-top:15px; font-size:16px;">
        I document everything I build — from small experiments to full projects. Let’s learn together.
    </p>
</div>
""", unsafe_allow_html=True)

# ------------------- Social icons -------------------
st.markdown("""
<div class="logo-box">
    <img src="https://cdn.simpleicons.org/gmail/ffffff" width="32">
    <img src="https://cdn.simpleicons.org/github/ffffff" width="32">
    <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/linkedin.svg" width="34" style="filter: invert(1);">
    <img src="https://cdn.simpleicons.org/streamlit/ffffff" width="32">
</div>
""", unsafe_allow_html=True)

# ------------------- Navigation -------------------
st.markdown("<br>", unsafe_allow_html=True)

nav1, nav2, nav3 , nav4 , nav5 = st.columns(5)
with nav4:
    if st.button("About Me"):
        st.switch_page("pages/1_👤_About_Me.py")
with nav5:
    if st.button("My Projects"):
        st.switch_page("pages/2_📂_My_Projects.py")

# ------------------- Back button -------------------
st.markdown("<br>", unsafe_allow_html=True)
if st.button("⬅️ Back to Home"):
    st.switch_page("portfolio_web.py")
st.markdown("<br><br>", unsafe_allow_html=True)

# ------------------- Footer -------------------
st.markdown("""
<hr style='border: 0.5px solid #ccc;'>
<p style='text-align:center; color:black; font-size:0.9rem;'>
    © 2025 Yuvraj | Built with Streamlit
</p>
""", unsafe_allow_html=True)
