import streamlit as st
import base64
from utils.theme import apply_theme


st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Page setup
st.set_page_config(page_title="Yuvraj | Portfolio", layout="wide")
apply_theme()
# Custom top header bar
st.markdown("""
<style>
.header-title {
    font-size: 22px; /* decreased size */
    font-weight: 700;
    color: white; /* white text */
    background: rgba(0, 0, 0, 0.55); /* black transparent background */
    padding: 6px 12px; /* some spacing around text */
    border-radius: 6px; /* smooth corners */
    position: fixed;
    top: 10px;
    left: 20px;
    z-index: 999;
}
</style>

<div class="header-title">
    Yuvraj Rana <span style="font-weight:400;">Portfolio</span>
</div>
""", unsafe_allow_html=True)
import os













st.markdown("""
<style>
/* White button with soft white glow + black text */
.glow-btn {
    background: rgba(255, 255, 255, 0.95) !important;
    color: #000000 !important;               /* black text */
    border: 2px solid rgba(255,255,255,0.6) !important;
    border-radius: 16px !important;
    padding: 16px 20px !important;
    font-size: 17px !important;
    font-weight: 800 !important;
    width: 100% !important;
    height: 100% !important;
    cursor: pointer !important;
    box-shadow: 0 4px 20px rgba(0,0,0,0.25) !important;
    transition: all 0.4s ease !important;
    position: relative !important;
    overflow: hidden !important;
    backdrop-filter: blur(10px);
}

/* Beautiful white glow + lift on hover */
.glow-btn:hover {
    transform: translateY(-5px) !important;
    background: white !important;
    box-shadow: 
        0 0 30px rgba(255, 255, 255, 0.7),
        0 0 60px rgba(255, 255, 255, 0.4),
        0 15px 40px rgba(0,0,0,0.3) !important;
}
</style>
""", unsafe_allow_html=True)










#check 




st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url('https://raw.githubusercontent.com/y-india/images_hosting/refs/heads/main/SELECTED_background_blur_for_portfolio.PNG');
        background-size: cover;          /* makes it full screen */
        background-position: center;     /* centers the image */
        background-repeat: no-repeat;    /* prevents tiling */
        background-attachment: fixed;    /* stays in place while scrolling */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ⬇️ tweak: adjust padding to center text more naturally on most screens
st.markdown("""
<style>
/* full-viewport wrapper that centers content exactly in middle */
.hero-wrapper {
    position: fixed;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1;
    pointer-events: none;
}

/* force viewport height for Streamlit container */
body, [data-testid="stAppViewContainer"] {
    height: 100vh;
    overflow: hidden;
}

.hero-inner {
    width: 90%;
    max-width: 1100px;
    pointer-events: auto;
}

.css-1v3fvcr.e16nr0p30 {padding-top:0px;}
</style>

<div class="hero-wrapper">
<div class="hero-inner" style="text-align:center;">
""", unsafe_allow_html=True)















# Headline text



# st.markdown(
#     """
#     <div style="
#         display:flex;
#         flex-direction:column;
#         align-items:center;
#         justify-content:center;
#         text-align:center;
#         margin-bottom:25px;
#     ">
#         <h1 style='
#             color:black;
#             text-shadow: 2px 2px 8px rgba(255,255,255,0.3);
#             font-size:56px;
#             font-weight:800;
#             margin:0;
#         '>
#             HI, I’M YUVRAJ
#         </h1>

#         <h2 style='
#             color:black;
#             font-size:38px;
#             font-weight:640;
#             margin-top:6px;
#         '>
#             I BUILD AND STUDY INTELLIGENT SYSTEMS
#         </h2>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )





st.markdown(
    """
    <div style='text-align:center; margin-top:-65px;'>
        <h1 style='
            color:black;
            text-shadow: 2px 2px 8px rgba(255,255,255,0.3);
            font-size:56px;
            font-weight:800;
            margin:0;
        '>
            HI, I’M YUVRAJ
        </h1>
    </div>
    """,
    unsafe_allow_html=True,
)





st.markdown(
    """
    <div style="text-align:center; margin-top:6px;">
        <h2 style='
            color:black;
            font-size:38px;
            font-weight:640;
            margin:0;
        '>
            I BUILD AND STUDY INTELLIGENT SYSTEMS
        </h2>
    </div>
    """,
    unsafe_allow_html=True,
)






















st.markdown("""
<div style="
    margin-top:20px;
    background-color: rgba(0,0,0,0.55);
    padding: 20px 28px;
    border-radius: 12px;
    max-width: 850px;
    margin-left:auto;
    margin-right:auto;
">
<p style="color:white; font-size:20px; line-height:1.6;">
I’m interested in how businesses can make better decisions before committing significant time, money, and resources.

I spend my time learning, testing, and building systems around business validation, customer research, experimentation, sales, and technology.

This site is a living record of what I test, what fails, what works, and what I learn along the way.
</p>
</div>
""", unsafe_allow_html=True)













slide = """
<script>
function slideOut(){
    document.body.style.transition = "transform 0.5s ease-in-out";
    document.body.style.transform = "translateX(-100%)";
}
</script>
"""
st.markdown(slide, unsafe_allow_html=True)

# — BEAUTIFUL 4 buttons that look identical + Hire Me stands out just the right amount —
# — 4 buttons with CSS glow magic —
col1, col2, col3, col4, col5 = st.columns(5)


with col2:
    if st.button("👤 About", use_container_width=True, key="about_btn"):
        st.switch_page("pages/1_👤_About_Me.py")

with col3:
    if st.button("📂 Projects", use_container_width=True, key="projects_btn"):
        st.switch_page("pages/2_📂_My_Projects.py")

with col4:
    if st.button("✉️ Contact", use_container_width=True, key="contact_btn"):
        st.switch_page("pages/3_✉️_Contact_Me.py")


st.markdown("""
<div style="
    margin-top:30px;
    background: rgba(0,0,0,0.55);
    padding:20px 26px;
    border-radius:14px;
    max-width:700px;
    margin-left:auto;
    margin-right:auto;
    box-shadow: 0 0 20px rgba(0,0,0,0.3);
">
<h3 style="color:white; margin-bottom:12px; text-align:center;">
Currently exploring
</h3>

<ul style="color:white; font-size:18px; line-height:1.6; list-style-type:disc; padding-left:20px;">
    <li>Validation techniques for product development .</li>
    <li>Reading idea validation books and implementing them .</li>
    <li>Changing Prompt Polish tool demo into project .</li>
</ul>
</div>
""", unsafe_allow_html=True)












