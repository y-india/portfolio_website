import streamlit as st
import base64
from utils.theme import apply_theme  # <- this should now resolve



# https://media.githubusercontent.com/media/y-india/portfolio_website_private/refs/heads/main/assets/full_blur_background.PNG
# Page settings
st.set_page_config(page_title="About | Yuvraj", layout="wide")
 

apply_theme()

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url('https://media.githubusercontent.com/media/y-india/portfolio_website_private/refs/heads/main/assets/SELECTED_background_blur_for_portfolio.PNG');
        background-size: cover;          /* makes it full screen */
        background-position: center;     /* centers the image */
        background-repeat: no-repeat;    /* prevents tiling */
        background-attachment: fixed;    /* stays in place while scrolling */
    }
    </style>
    """,
    unsafe_allow_html=True
)


# # ---------------------- BACKGROUND IMAGE ----------------------
# def set_bg(image_file):
#     with open(image_file,"rb") as f:
#         b64 = base64.b64encode(f.read()).decode()
#     st.markdown(
#         f"""
#         <style>
#         [data-testid="stAppViewContainer"] {{
#             background: url("data:image/png;base64,{b64}");
#             background-size: cover;
#             background-attachment: fixed;
#         }}
#         </style>
# """
#         ,
#         unsafe_allow_html=True
#     )

# set_bg("assets/SELECTED_background_blur_for_portfolio.PNG")


# Set about page background


# ---- ABOUT SECTION ----

# Use columns for picture + text
col1, col2 = st.columns([1,2])

# Styling for circular image
st.markdown("""
<style>
.profile-pic {
    width: 420px;
    border-radius: 50%;
    border: 3px solid rgba(255,255,255,0.7);
}

</style>
""", unsafe_allow_html=True)

# Place new transparent profile picture
with col1:
    st.markdown(
        f"""
        <img src="data:image/png;base64,{base64.b64encode(open("SELECTED_PROFILE_IMG.jpg","rb").read()).decode()}"
        class="profile-pic">
        """,
        unsafe_allow_html=True
    )
# ---- About text ----
with col2:
    st.markdown("""
    <div style="
        background-color: rgba(0,0,0,0.55);
        padding: 25px;
        border-radius: 12px;
        color: white;
        box-shadow: 0 0 20px rgba(0,0,0,0.3);
        font-size:18px;
        line-height:1.6;
    ">
    
    <h2 style="font-weight:800;">About Me</h2>

    <p>
        Hello, I’m <b>Yuvraj Rana</b>.
        I help businesses and new founders figure out 
        <b>what to build, who to build it for, and how to validate the idea</b>
        before investing too much time and money.
    </p>

    <p>
        My work sits at the intersection of 
        <b>business thinking, customer research, experimentation, sales, and technology</b>.
        I focus on reducing assumptions and replacing them with evidence from
        real customers and real-world tests.
    </p>

    <p>
        I use frameworks and principles such as 
        <b>The Mom Test, Skin in the Game, Customer Interviews, Jobs to Be Done,
        Pretotyping, the 6 Phases of Buying, buying emotions, and sales influence</b>
        to understand customer problems, test demand, and improve business ideas.
    </p>

    <p>
        Technically, I am also a <b>self-taught Python and Machine Learning developer</b>.
        I use technology and AI to build experiments, automate processes,
        analyze information, and turn business problems into practical systems.
    </p>

    <p><b>My approach:</b></p>

    <ul>
        <li>Understand the problem</li>
        <li>Identify the riskiest assumptions</li>
        <li>Talk to real customers</li>
        <li>Test demand before building</li>
        <li>Build only after learning</li>
        <li>Measure, iterate, and improve</li>
    </ul>

    <p>
        I believe a good business idea is not something you simply feel confident about.
        It is something you can <b>test, learn from, and improve through evidence</b>.
    </p>

    <p>
        I’m constantly experimenting with <b>business validation, AI systems,
        automation, customer research, and decision-making frameworks</b>
        while documenting what I learn along the way.
    </p>

    </div>
    """, unsafe_allow_html=True)



st.markdown("<br>", unsafe_allow_html=True)

# Back button
if st.button("⬅️ Back to Home"):
    st.switch_page("portfolio_web.py")

st.markdown("<br><br>", unsafe_allow_html=True)

nav1, nav2, nav3 , nav4 , nav5 , nav6 , nav7 , nav8 , nav9= st.columns(9)

with nav8:
    if st.button("Projects"):
        st.switch_page("pages/2_📂_My_Projects.py")
with nav9:
    if st.button("📞 Contact"):
        st.switch_page("pages/3_✉️_Contact_Me.py")



st.markdown("<br><br>", unsafe_allow_html=True)
# Footer
st.markdown("""
    <hr style='border: 0.5px solid #ccc;'>
    <p style='text-align:center; color:black; font-size:0.9rem;'>
        © 2025 Yuvraj | Built with Streamlit HTML
    </p>
""", unsafe_allow_html=True)

