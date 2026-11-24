import streamlit as st
import base64
from utils.theme import apply_theme



# this is not inculded in main screen now #
# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(layout="wide")
apply_theme()

# ---------------------- GLOBAL CSS ----------------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] > .main,
.main > .block-container,
.block-container {
    padding-top: 0 !important;
    margin-top: 0 !important;
}

.highlight-box {
    background-color: black;
    color: white !important;
    padding: 14px;
    border-radius: 8px;
    font-size: 22px;
    line-height: 1.6;
    text-align: left;
}

h1 {
    color: #e6eef5 !important;
    text-shadow: 0px 0px 4px black;
    font-size: 46px !important;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


# ---------------------- BACKGROUND IMAGE ----------------------
def set_bg(image_file):
    with open(image_file,"rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background: url("data:image/png;base64,{b64}");
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg("project_pictures/background_retail_project.png")



# ---------------------- IMAGE BASE URL ----------------------
IMG_BASE = "https://github.com/y-india/images_hosting/blob/main"

# ---------------------- TITLE ----------------------
st.title("Retail Sales Forecasting & Analysis System")
st.markdown("<br>", unsafe_allow_html=True)

# ---------------------- OVERVIEW ----------------------
st.subheader("📘 Overview")
st.markdown("""
<div class="highlight-box">
End-to-end machine learning project that analyzes and forecasts retail store sales using historical daily sales data and store-level metadata. The project demonstrates the complete ML lifecycle including data cleaning, feature engineering, exploratory data analysis, modeling, evaluation, and deployment via a Streamlit dashboard.
</div>
""", unsafe_allow_html=True)

st.image(
    f"{IMG_BASE}/sales_important_graph.png?raw=true",
    caption="Key sales insights discovered during exploratory data analysis"
)

# ---------------------- LINKS ----------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.subheader("🔗 Project Links")
st.markdown(f"""
<div class="highlight-box">
<b>GitHub Repository:</b><br>
<a href="https://github.com/y-india/retail-sales-analysis-project" target="_blank">
https://github.com/y-india/retail-sales-analysis-project
</a>
</div>
""", unsafe_allow_html=True)

# ---------------------- PROBLEM STATEMENT ----------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.subheader("🚨 Problem Statement")
st.markdown("""
<div class="highlight-box">
Retail businesses face challenges in accurately forecasting daily sales due to seasonality, promotions, competition, and store-level variability. Traditional forecasting methods fail to capture complex patterns, leading to inventory inefficiencies and revenue loss.
</div>
""", unsafe_allow_html=True)

# ---------------------- SOLUTION OVERVIEW ----------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.subheader("✅ Solution Overview")
st.markdown("""
<div class="highlight-box">
A scalable ML pipeline was developed to preprocess raw retail data, engineer meaningful features, perform deep exploratory analysis, and train multiple regression models. The best-performing model (XGBoost) is deployed through an interactive Streamlit dashboard for real-time sales forecasting.
</div>
""", unsafe_allow_html=True)

# ---------------------- PROJECT TIMELINE ----------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.subheader("📆 7-Day Project Timeline")
st.markdown("""
<div class="highlight-box">
<b>Day 1:</b> Data loading, merging, inspection<br>
<b>Day 2:</b> Data cleaning & feature engineering<br>
<b>Day 3:</b> Exploratory Data Analysis (EDA)<br>
<b>Day 4:</b> Model training & tuning (Linear, HGB, XGBoost)<br>
<b>Day 5:</b> Evaluation, diagnostics & error analysis<br>
<b>Day 6:</b> Production-ready prediction pipeline<br>
<b>Day 7:</b> Interactive Streamlit dashboard deployment
</div>
""", unsafe_allow_html=True)

# ---------------------- MODEL RESULTS ----------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.subheader("📊 Model Performance & Results")
st.markdown("""
<div class="highlight-box">
✅ Best Model: Tuned XGBoost Regressor<br>
✅ RMSE: ~870 | Accuracy Score: ~93.6%<br>
✅ Sales–Customer Correlation: 0.82<br>
✅ Promotions increased sales by ~39%
</div>
""", unsafe_allow_html=True)

st.image(
    f"{IMG_BASE}/actual_vs_predicted_sales.png?raw=true",
    caption="Actual vs Predicted Retail Sales"
)

st.image(
    f"{IMG_BASE}/distribution_of_prediction_errors.png?raw=true",
    caption="Distribution of prediction errors"
)

st.image(
    f"{IMG_BASE}/learning_curve.png?raw=true",
    caption="Learning curve showing model generalization"
)

# ---------------------- MODEL & PIPELINE SNAPSHOTS ----------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.subheader("🧠 Model & Pipeline Snapshots")
st.image(
    f"{IMG_BASE}/checking_unique_values_code.png?raw=true",
    caption="Data validation & integrity checks"
)

st.image(
    f"{IMG_BASE}/data_selection_code.png?raw=true",
    caption="Feature selection & preprocessing logic"
)

st.image(
    f"{IMG_BASE}/code_example_frpom_projects.png?raw=true",
    caption="Production-ready prediction pipeline implementation"
)

# ---------------------- TECH STACK ----------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.subheader("🛠 Skills & Tools Used")
st.markdown("""
<div class="highlight-box">
Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost, Joblib, Jupyter Notebook, Streamlit, Git & GitHub
</div>
""", unsafe_allow_html=True)

# ---------------------- FUTURE WORK ----------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.subheader("🚀 Future Enhancements")
st.markdown("""
<div class="highlight-box">
• Advanced feature engineering (lags & rolling windows)<br>
• Multi-step time series forecasting<br>
• Deep learning models (LSTM, Prophet, CatBoost)<br>
• Cloud deployment & performance optimization
</div>
""", unsafe_allow_html=True)

# ---------------------- CONCLUSION ----------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.subheader("🏁 Conclusion")

st.markdown("""
<div class="highlight-box">
This project showcases strong data science and machine learning engineering skills by transforming raw retail data into a production-ready forecasting system. It highlights real-world business insights, robust pipelines, and deployment readiness.
</div>
""", unsafe_allow_html=True)

# ---------------------- NAVIGATION ----------------------
st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("⬅️ Back to Home"):
    st.switch_page("portfolio_web.py")

# ---------------------- FOOTER ----------------------
st.markdown("""
<hr style='border: 0.5px solid #ccc;'>
<p style='text-align:center; color:gray; font-size:0.9rem;'>
© 2025 Yuvraj | Built with Streamlit & Machine Learning
</p>
""", unsafe_allow_html=True)


