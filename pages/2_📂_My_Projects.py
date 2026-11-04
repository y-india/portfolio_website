

import streamlit as st
import base64

import os

print("Current working directory:", os.getcwd())

from utils.theme import apply_theme
apply_theme()

def card(img, title):
    if img.startswith("http"):
        img_src = img
    else:
        img_src = f"data:image/png;base64,{img}"

    return f"""
    <div class="proj-card">
        <img src="{img_src}" class="proj-img"/>
        <div class="proj-title">{title}</div>
    </div>
    """


# CSS for overlay buttons
st.markdown("""
<style>
.stButton button {
    position: relative;
    top: -70px; /* lift button over image */
    width: 80%;
    padding: 14px;
    font-size: 15px;
    border: 1px solid rgba(255,255,255,0.5);
    background: rgba(0,0,0,0.25);
    color: white;
    border-radius: 12px;
    backdrop-filter: blur(4px);
    cursor: pointer;
}

.stButton button:hover {
    background: rgba(255,255,255,0.2);
}

.proj-card {
    position: relative;
    width: 100%;
    max-width: 370px;
    height: 240px;
    overflow: hidden;
    border-radius: 16px;
    cursor: pointer;
}
.proj-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: brightness(60%);
    border-radius: 16px;
}
.proj-title {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -70%);
    color: white;
    font-weight: bold;
    font-size: 18px;
    text-align: center;
}
.proj-btn {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    padding: 14px 18px;
    transition: 0.3s;
    background: rgba(0,0,0,0.18);
    border: 1px solid rgba(255,255,255,0.4);
    color: white;
    border-radius: 14px;
    font-size: 15px;
    cursor: pointer;
}
.proj-btn:hover {
    background-color: rgba(255,255,255,0.18);
}
</style>
""", unsafe_allow_html=True)


# Convert background to base64
def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()






st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url('https://raw.githubusercontent.com/y-india/images_hosting/refs/heads/main/full_blur_background.png');
        background-size: cover;          /* makes it full screen */
        background-position: center;     /* centers the image */
        background-repeat: no-repeat;    /* prevents tiling */
        background-attachment: fixed;    /* stays in place while scrolling */
    }
    </style>
    """,
    unsafe_allow_html=True
)

projects = [
    {
        "title": "Prompt Polish Tool",
        "img": "https://github.com/y-india/images_hosting/blob/main/banner.png?raw=true",
        "page": "pages/10.2_📝_Prompt_Polish_Tool.py"
    },
    {
        "title": "AI Based Crop Predictor for Haryana Farmers",
        "img": img_to_base64("project_data/aicrop_project1/front_aicropdetection_project.png"),
        "page": "pages/10.1_🌾_AI_Crop_Predictor.py"
    },
    {
        
        "title": "🚀 My Product Journey",
        "img": "https://github.com/y-india/images_hosting/blob/main/ChatGPT%20Image%20Jul%206,%202026,%2004_15_20%20PM.png?raw=true",
        "page": "pages/10.10_🚀_My_Product_Journey.py"

    }
    
]



projects_second = [
    {
        "title": "Road Accident Severity Prediction System",
        "img": img_to_base64("project_pictures/road_accident_project/104385221.png"),
        "page": "pages/10.4_🚗_Road_Accident_Severity.py"
    ,
    },
    {
        "title": "Machine Learning Notes",
        "img": img_to_base64("concept-technology-development-phrase-words-text-machine-learning-notebook-old-backgroun____.jpg"),
        "page": "pages/10.5_📝_Machine_Learning_Notes.py"
    },
    {

        "title": "Attendance System Using Face Recognition",
        "img": img_to_base64("project_data/opencvattandance_project3/front_attandancesystem_project.png"),
        "page": "pages/10.3_🧑‍🕵️_Attendance_Face.py"


    }
]

# project_data\aicrop_project1\front_aicropdetection_project.png
projects_third = [
    {
        "title": "My Portfolio Website",
        "img": img_to_base64("website_portfolio_monotone_icon_in_powerpoint_pptx_png_and_editable_eps_format_slide01.jpg"),
        "page": "pages/10.7_💼_My_Portfolio.py"
    },
    {
        "title": "Retail Sales Analysis & Forecasting System",
        "img": img_to_base64("project_pictures/EXCEL of Store Sales.png"),
        "page": "pages/10.8_📊_Retail_Sales_Analysis.py"
    }
]


st.set_page_config(layout="wide", page_title="Projects")

st.markdown("""
<div style="
    text-align:center;
    margin-top:-40px; /* lift upward */
">
    <h1 style="
        color:black;
        background: rgba(0,0,0,0.00);
        padding: 14px 30px;
        border-radius: 10px;
        display: inline-block;
    ">
        🚀 My Projects
    </h1>
</div>
""", unsafe_allow_html=True)




st.markdown("<br>", unsafe_allow_html=True)

cols = st.columns(3)

for col, proj in zip(cols, projects):
    with col:
        st.markdown(card(proj["img"], proj["title"]), unsafe_allow_html=True)

        # actual clickable button
        if st.button(proj["title"], key=proj["page"]):
            st.switch_page(proj["page"])


cols_second = st.columns(3)

for col, proj in zip(cols_second, projects_second):
    with col:
        st.markdown(card(proj["img"], proj["title"]), unsafe_allow_html=True)

        # actual clickable button
        if st.button(proj["title"], key=proj["page"]):
            st.switch_page(proj["page"])

cols_third = st.columns(3)
for col, proj in zip(cols_third, projects_third):
    with col:
        st.markdown(card(proj["img"], proj["title"]), unsafe_allow_html=True)

        # actual clickable button
        if st.button(proj["title"], key=proj["page"]):
            st.switch_page(proj["page"])




# Back button

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)
with col1:
    if st.toggle("About Me"):
        st.switch_page("pages/1_👤_About_Me.py")

with col9:
    if st.toggle("📞 Contact"):
        st.switch_page("pages/3_✉️_Contact_Me.py")

st.markdown("<br><br>", unsafe_allow_html=True)







st.markdown("<br><br>", unsafe_allow_html=True)
# Footer
st.markdown("""
    <hr style='border: 0.5px solid #ccc;'>
    <p style='text-align:center; color:black; font-size:0.9rem;'>
        © 2025 Yuvraj | Built with Streamlit HTML
    </p>
""", unsafe_allow_html=True)



# for adding new project, just add a new dictionary in the 'projects' list above with keys: title, img, page


# example:
#     {
#         "title": "Project Title Here",
#         "img": img_to_base64("path_to_image_here.PNG"),
#         # "page": "/Page_Name_Here"
#     # },

# # also create the page in the main app file to link it properly.

# # keep in mind 

# # image is 7:5
