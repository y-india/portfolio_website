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
    font-size: 22px;
    font-weight: 700;
    color: white;
    background: rgba(0, 0, 0, 0.55);
    padding: 6px 12px;
    border-radius: 6px;
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
.glow-btn {
    background: rgba(255, 255, 255, 0.95) !important;
    color: #000000 !important;
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


# Background

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url('https://raw.githubusercontent.com/y-india/images_hosting/refs/heads/main/SELECTED_background_blur_for_portfolio.PNG');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Hero section

st.markdown("""
<style>
.hero-wrapper {
    position: fixed;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1;
    pointer-events: none;
}

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


# Main heading

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


# Main positioning line

st.markdown(
    """
    <div style="text-align:center; margin-top:6px;">
        <h2 style='
            color:black;
            font-size:38px;
            font-weight:640;
            margin:0;
        '>
            I DISCOVER PROBLEMS, TEST IDEAS & BUILD SOLUTIONS
        </h2>
    </div>
    """,
    unsafe_allow_html=True,
)


# Introduction

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
I work at the intersection of customer discovery, business experimentation, and technology.

I interview customers, investigate problems, and test business assumptions through real-world experiments before investing heavily in an idea.

So far, I have conducted 100+ customer interviews, reached out to 1,000+ people, and tested 7–9 business ideas using pretotyping techniques, including fake-door experiments.

I also build with Python and Machine Learning, developing practical applications, APIs, computer vision systems, and live websites.

This portfolio is a record of what I research, test, build, and learn along the way.
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


# Navigation buttons

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


# Currently exploring

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
    <li>Customer discovery, Jobs to Be Done, and buying behaviour.</li>
    <li>Pretotyping, fake-door experiments, and demand testing.</li>
    <li>Turning the Prompt Polish demo into a working project.</li>
</ul>
</div>
""", unsafe_allow_html=True)