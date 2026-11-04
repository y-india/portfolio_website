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
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)


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
        Hello, I'm <b>Yuvraj Rana</b>.
        I work at the intersection of 
        <b>customer discovery, business experimentation, and technology</b>.
        I am interested in understanding real customer problems, testing business
        assumptions, and figuring out what is worth building before investing
        significant time and resources.
    </p>

    <p>
        My focus is on reducing uncertainty through evidence rather than relying
        on assumptions. I believe the best way to understand a business opportunity
        is to get out of the building, talk to people, observe their behaviour,
        and run experiments.
    </p>

    <p>
        So far, I have:
        <br><br>
        <b>100+ customer interviews</b> to understand customer problems,
        needs, and behaviour.
        <br>
        <b>1,000+ people reached</b> through customer discovery outreach.
        <br>
        <b>7–9 business ideas tested</b> using pretotyping techniques,
        including fake-door experiments.
    </p>

    <p>
        My approach to customer research and business experimentation is influenced
        by books and frameworks such as <b>The Mom Test, Influence, Skin in the Game,
        Jobs to Be Done, Pretotyping, the 6 Phases of Buying, buying psychology,
        and sales influence</b>.
    </p>

    <p>
        Alongside business experimentation, I am a
        <b>self-taught Python and Machine Learning developer</b>.
        I use technology to turn ideas into working prototypes,
        automate processes, analyze information, and solve practical problems.
    </p>

    <p>
        My technical experience includes:
        <br><br>
        <b>Programming:</b> Python, Dart
        <br>
        <b>Libraries:</b> Pandas, NumPy, Matplotlib, Scikit-learn, Joblib, OpenCV
        <br>
        <b>Frameworks & Tools:</b> Streamlit, FastAPI, Docker
        <br>
        <b>Technical Domains:</b> Machine Learning, Computer Vision, Data Analysis,
        API Development, and Software Development.
    </p>

    <p>
        I have built <b>10+ technical projects</b>, including 4–5 live websites,
        machine learning applications, computer vision projects using OpenCV,
        Streamlit applications, and API-based projects.
        I am also exploring LLMs, AI systems, and automation.
    </p>

    <p><b>How I approach problems:</b></p>

    <ul>
        <li>Understand the customer and the problem.</li>
        <li>Identify the riskiest assumptions.</li>
        <li>Talk to real people and gather evidence.</li>
        <li>Test demand before committing to development.</li>
        <li>Build practical solutions using technology.</li>
        <li>Measure results, learn, and iterate.</li>
    </ul>

    <p>
        My philosophy is simple:
        <b>Think → Test → Learn → Build → Iterate.</b>
    </p>

    <p>
        I don't believe confidence in an idea makes it a good idea.
        What matters is whether real people need it, whether they are willing
        to act on it, and whether evidence supports building it.
    </p>

    <p>
        I continuously experiment with business ideas, customer research,
        AI systems, automation, and technical projects while documenting
        what I learn along the way.
    </p>

    </div>
    """, unsafe_allow_html=True)



st.markdown("<br>", unsafe_allow_html=True)

# Back button
if st.button("⬅️ Back to Home"):
    st.switch_page("portfolio_web.py")

st.markdown("<br><br>", unsafe_allow_html=True)

nav1, nav2, nav3, nav4, nav5, nav6, nav7, nav8, nav9 = st.columns(9)

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