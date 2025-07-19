import streamlit as st
import numpy as np
import pickle
import os
import datetime
from components.sidebar import show_sidebar
# from components.pdf_generator import generate_pdf_report
from firebase_config import db

# --- Setup ---
st.set_page_config(page_title="Heart Disease", page_icon="❤️")
show_sidebar()

# --- Load model ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "../models/heart_model.pkl")
heart_model = pickle.load(open(model_path, 'rb'))

# --- UI Header ---
st.markdown("""
    <h2 style='color:#e91e63;'>❤️ Heart Disease Prediction</h2>
    <p style='color:#555;'>Answer the questions below to assess your heart health.</p>
    <hr style="border: 1px solid #e0e0e0;">
""", unsafe_allow_html=True)

# --- Input Form in Card Layout ---
with st.form("heart_form"):
    st.markdown("<div style='background-color:#f3e5f5; padding:20px; border-radius:10px;'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("🎂 Age", min_value=1)
        sex = st.radio("👤 Sex", [1, 0], format_func=lambda x: "Male" if x == 1 else "Female")
        cp = st.selectbox("💓 Chest Pain Type", [0, 1, 2, 3])
        trestbps = st.number_input("💉 Resting Blood Pressure")
        chol = st.number_input("🩸 Cholesterol Level")

    with col2:
        fbs = st.radio("🍬 Fasting Blood Sugar > 120 mg/dl", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
        restecg = st.selectbox("🧪 Resting ECG", [0, 1, 2])
        thalach = st.number_input("🏃 Max Heart Rate Achieved")
        exang = st.radio("😓 Exercise Induced Angina", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
        oldpeak = st.number_input("📉 ST Depression")
        slope = st.selectbox("🧭 Slope of ST Segment", [0, 1, 2])
        ca = st.selectbox("🔍 Major Vessels Colored", [0, 1, 2, 3])
        thal = st.selectbox("🧬 Thalassemia Type", [1, 2, 3])

    st.markdown("</div>", unsafe_allow_html=True)
    submitted = st.form_submit_button("🔍 Predict")

# --- Prediction ---
if submitted:
    inputs = np.array([age, sex, cp, trestbps, chol, fbs, restecg,
                       thalach, exang, oldpeak, slope, ca, thal]).reshape(1, -1)
    result = heart_model.predict(inputs)

    if st.session_state.user:
        user_id = st.session_state.user['localId']
        db.child("predictions").child(user_id).push({
            "disease": "Heart Disease",
            "result": int(result[0]),
            "date": str(datetime.datetime.now())
        })

    # --- Show Result ---
    if result[0] == 1:
        st.error("🦡 Positive for Heart Disease. Please consult a cardiologist.")
    else:
        st.success("💚 No Heart Disease Detected. Keep up the healthy lifestyle!")

    # --- Tips & PDF ---
    tips = [
        "Eat a heart-healthy diet (low salt, fat, sugar)",
        "Exercise regularly",
        "Avoid tobacco and limit alcohol",
        "Sleep well & reduce stress",
        "Get periodic heart check-ups"
    ]
    # filename = generate_pdf_report("Heart Disease", result[0], tips)
    st.download_button("📄 Download Your Report", data=open(filename, "rb"), file_name=filename)
