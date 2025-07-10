import streamlit as st
import numpy as np
import pickle
from fpdf import FPDF
import datetime

# ---- PAGE CONFIG & STYLING ----
st.set_page_config(page_title="Multi Disease Predictor", layout="wide", page_icon="🩺")

# Theme Toggle
theme = st.sidebar.selectbox("🎨 Select Theme", ["Light", "Dark"])
if theme == "Dark":
    st.markdown("""
        <style>
        body, .stApp {
            background-color: #0e1117;
            color: #FAFAFA;
        }
        </style>
        """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        body, .stApp {
            background: linear-gradient(to right, #fce4ec, #f8bbd0);
            color: black;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3 {
            color: #ad1457;
        }
        .stButton>button {
            background-color: #ec407a;
            color: white;
            border-radius: 8px;
            padding: 8px 16px;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True)

# ---- SIDEBAR ----
with st.sidebar:
    st.title("🩺 Health Predictor")
    st.markdown("""
    A ML-powered assistant to predict:

    - ❤️ Heart Disease  
    - 💉 Diabetes  
    - 🧠 Parkinson's  

    _Developed by Aarzoo Dhankhar_
    """)
    st.markdown("[📬 Contact Me](https://www.linkedin.com/in/aarzoodhankhar)")

# ---- Load Models ----
diabetes_model = pickle.load(open('diabetes_model.pkl', 'rb'))
heart_model = pickle.load(open('heart_model.pkl', 'rb'))
parkinson_model = pickle.load(open('parkinson_model.pkl', 'rb'))

# ---- PDF Generator ----
def generate_pdf_report(disease, result, tips):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Multi Disease Prediction Report", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Date: {datetime.datetime.now().strftime('%d-%m-%Y')}", ln=True)
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Prediction: {disease} - {'Positive' if result == 1 else 'Negative'}", ln=True)
    pdf.ln(10)
    pdf.set_font("Arial", size=11)
    pdf.cell(200, 10, txt="Tips:", ln=True)
    for tip in tips:
        pdf.cell(200, 8, txt=f"- {tip}", ln=True)
    filename = f"{disease.replace(' ', '_')}_report.pdf"
    pdf.output(filename)
    return filename

# ---- BMI CALCULATOR ----
st.markdown("---")
st.header("📏 BMI Calculator")
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Enter your weight (kg)", min_value=1.0)
with col2:
    height = st.number_input("Enter your height (cm)", min_value=1.0)

if height > 0 and weight > 0:
    bmi = weight / ((height / 100) ** 2)
    st.success(f"Your BMI is: **{bmi:.2f}**")
    if bmi < 18.5:
        st.warning("You are **Underweight**. Try to eat well and gain healthy weight.")
    elif 18.5 <= bmi < 24.9:
        st.info("You are in **Normal weight** range. Keep it up!")
    elif 25 <= bmi < 29.9:
        st.warning("You are **Overweight**. Consider physical activity.")
    else:
        st.error("You are in **Obese** category. Please consult a doctor.")

# ---- DISEASE SELECTION ----
st.title('🩺 Multi Disease Prediction System')
st.subheader("A Smart Health Assistant Powered by Machine Learning")
selected = st.selectbox("Choose Disease to Predict", ["Heart Disease", "Diabetes", "Parkinson's"])

# ---- HEART DISEASE ----
if selected == "Heart Disease":
    st.header("❤️ Heart Disease Prediction")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age")
        sex = st.number_input("Sex (1 = Male, 0 = Female)")
        cp = st.number_input("Chest Pain Type (0–3)")
        trestbps = st.number_input("Resting Blood Pressure")
        chol = st.number_input("Cholesterol")
        fbs = st.number_input("Fasting Blood Sugar (1 = True, 0 = False)")
        restecg = st.number_input("Rest ECG (0–2)")
    with col2:
        thalach = st.number_input("Max Heart Rate Achieved")
        exang = st.number_input("Exercise Induced Angina (1 = Yes, 0 = No)")
        oldpeak = st.number_input("ST Depression")
        slope = st.number_input("Slope (0–2)")
        ca = st.number_input("Number of Major Vessels (0–3)")
        thal = st.number_input("Thal (1 = Normal, 2 = Fixed defect, 3 = Reversible)")

    if st.button("Predict Heart Disease"):
        heart_input = np.array([age, sex, cp, trestbps, chol, fbs, restecg,
                                thalach, exang, oldpeak, slope, ca, thal]).reshape(1, -1)
        result = heart_model.predict(heart_input)
        st.success("Positive for Heart Disease" if result[0] == 1 else "No Heart Disease Detected")
        tips = [
            "Follow a heart-healthy diet (low fat, low salt)",
            "Do regular exercise (30 min/day)",
            "Avoid smoking and alcohol",
            "Manage stress and sleep well",
            "Regular BP & cholesterol checkups"
        ]
        filename = generate_pdf_report("Heart Disease", result[0], tips)
        st.download_button("📄 Download Report", data=open(filename, "rb"), file_name=filename)

# ---- DIABETES ----
elif selected == "Diabetes":
    st.header("💉 Diabetes Prediction")
    col1, col2 = st.columns(2)
    with col1:
        Pregnancies = st.number_input("Number of Pregnancies")
        Glucose = st.number_input("Glucose Level")
        BloodPressure = st.number_input("Blood Pressure")
        SkinThickness = st.number_input("Skin Thickness")
    with col2:
        Insulin = st.number_input("Insulin Level")
        BMI = st.number_input("BMI")
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function")
        Age = st.number_input("Age")

    if st.button("Predict Diabetes"):
        diabetes_input = np.array([Pregnancies, Glucose, BloodPressure, SkinThickness,
                                   Insulin, BMI, DiabetesPedigreeFunction, Age]).reshape(1, -1)
        result = diabetes_model.predict(diabetes_input)
        st.success("Diabetic" if result[0] == 1 else "Not Diabetic")
        tips = [
            "Eat high-fiber low-carb food",
            "Track blood sugar levels",
            "Exercise regularly",
            "Avoid sugary/processed food",
            "Drink more water"
        ]
        filename = generate_pdf_report("Diabetes", result[0], tips)
        st.download_button("📄 Download Report", data=open(filename, "rb"), file_name=filename)

# ---- PARKINSON'S ----
elif selected == "Parkinson's":
    st.header("🧠 Parkinson's Disease Prediction")
    inputs = [
        "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)", "MDVP:RAP", "MDVP:PPQ",
        "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)", "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ",
        "Shimmer:DDA", "NHR", "HNR", "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"
    ]
    values = [st.number_input(label) for label in inputs]

    if st.button("Predict Parkinson's"):
        parkinson_input = np.array(values).reshape(1, -1)
        result = parkinson_model.predict(parkinson_input)
        st.success("Parkinson's Detected" if result[0] == 1 else "No Parkinson's")
        tips = [
            "Exercise regularly and stay active",
            "Take medications on time",
            "Practice speech and balance training",
            "Get adequate sleep",
            "Consult neurologist regularly"
        ]
        filename = generate_pdf_report("Parkinson's", result[0], tips)
        st.download_button("📄 Download Report", data=open(filename, "rb"), file_name=filename)
