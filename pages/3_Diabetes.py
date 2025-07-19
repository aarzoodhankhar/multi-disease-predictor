import streamlit as st
import numpy as np
import pickle
import os
import datetime
# from components.sidebar import show_sidebar
from components.pdf_generator import generate_pdf_report
from firebase_config import db

# --- Setup ---
st.set_page_config(page_title="Diabetes Prediction", page_icon="💉")
show_sidebar()

# --- Load Model ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "../models/diabetes_model.pkl")
diabetes_model = pickle.load(open(model_path, 'rb'))

# --- Header ---
st.markdown("""
    <h2 style='color:#e91e63;'>💉 Diabetes Prediction</h2>
    <p style='color:#555;'>Enter the following details to assess your diabetes risk.</p>
    <hr style="border: 1px solid #e0e0e0;">
""", unsafe_allow_html=True)

# --- Form Layout ---
with st.form("diabetes_form"):
    st.markdown("<div style='background-color:#e0f7fa; padding:20px; border-radius:10px;'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.number_input("🤰 Number of Pregnancies", min_value=0)
        Glucose = st.number_input("🍬 Glucose Level", min_value=0)
        BloodPressure = st.number_input("💉 Blood Pressure", min_value=0)
        SkinThickness = st.number_input("📏 Skin Thickness", min_value=0)

    with col2:
        Insulin = st.number_input("💉 Insulin Level", min_value=0)
        BMI = st.number_input("⚖️ BMI", min_value=0.0)
        DiabetesPedigreeFunction = st.number_input("🧬 Diabetes Pedigree Function", min_value=0.0)
        Age = st.number_input("🎂 Age", min_value=1)

    st.markdown("</div>", unsafe_allow_html=True)
    submitted = st.form_submit_button("🔍 Predict")

# --- Prediction ---
if submitted:
    inputs = np.array([Pregnancies, Glucose, BloodPressure, SkinThickness,
                       Insulin, BMI, DiabetesPedigreeFunction, Age]).reshape(1, -1)
    result = diabetes_model.predict(inputs)

    if st.session_state.user:
        user_id = st.session_state.user['localId']
        db.child("predictions").child(user_id).push({
            "disease": "Diabetes",
            "result": int(result[0]),
            "date": str(datetime.datetime.now())
        })

    # --- Show Result ---
    if result[0] == 1:
        st.error("🔴 You may be diabetic. Please consult a doctor.")
    else:
        st.success("🟢 You are not diabetic. Maintain your lifestyle!")

    # --- Tips & Report ---
    tips = [
        "Eat fiber-rich food and avoid sugary snacks",
        "Exercise daily, at least 30 minutes",
        "Drink plenty of water",
        "Get regular blood sugar tests",
        "Avoid stress & get proper sleep"
    ]
    filename = generate_pdf_report("Diabetes", result[0], tips)
    st.download_button("📄 Download Your Report", data=open(filename, "rb"), file_name=filename)
