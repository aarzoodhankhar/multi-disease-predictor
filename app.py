import numpy as np
import pickle
import streamlit as st

# Load the saved models
diabetes_model = pickle.load(open('diabetes_model.pkl', 'rb'))
heart_model = pickle.load(open('heart_model.pkl', 'rb'))
parkinson_model = pickle.load(open('parkinson_model.pkl', 'rb'))
st.markdown("---")
st.header("📏 BMI Calculator")

weight = st.number_input("Enter your weight (kg)", min_value=1.0)
height = st.number_input("Enter your height (cm)", min_value=1.0)

if height > 0 and weight > 0:
    height_m = height / 100  # convert cm to meters
    bmi = weight / (height_m ** 2)
    st.success(f"Your BMI is: **{bmi:.2f}**")

    # Interpret BMI
    if bmi < 18.5:
        st.warning("You are **Underweight** 😕. Try to eat well and gain healthy weight.")
    elif 18.5 <= bmi < 24.9:
        st.info("You are in **Normal weight** range 💪. Keep it up!")
    elif 25 <= bmi < 29.9:
        st.warning("You are **Overweight** 😬. Consider physical activity.")
    else:
        st.error("You are in **Obese** category 🚨. Please consult a doctor.")

# Title
st.title('🩺 Multi Disease Prediction System')
st.subheader("A Smart Health Assistant Powered by Machine Learning")

# Tabs
selected = st.selectbox("Choose Disease to Predict", ["Heart Disease", "Diabetes", "Parkinson's"])

# ------------------------------------------
# ❤️ HEART DISEASE
if selected == "Heart Disease":
    st.header("❤️ Heart Disease Prediction")

    age = st.number_input("Age")
    sex = st.number_input("Sex (1 = Male, 0 = Female)")
    cp = st.number_input("Chest Pain Type (0–3)")
    trestbps = st.number_input("Resting Blood Pressure")
    chol = st.number_input("Cholesterol")
    fbs = st.number_input("Fasting Blood Sugar (1 = True, 0 = False)")
    restecg = st.number_input("Rest ECG (0–2)")
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
        st.success("🧡 Positive for Heart Disease" if result[0] == 1 else "💚 No Heart Disease Detected")

# ------------------------------------------
# 💉 DIABETES
elif selected == "Diabetes":
    st.header("💉 Diabetes Prediction")

    Pregnancies = st.number_input("Number of Pregnancies")
    Glucose = st.number_input("Glucose Level")
    BloodPressure = st.number_input("Blood Pressure")
    SkinThickness = st.number_input("Skin Thickness")
    Insulin = st.number_input("Insulin Level")
    BMI = st.number_input("BMI")
    DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function")
    Age = st.number_input("Age")

    if st.button("Predict Diabetes"):
        diabetes_input = np.array([Pregnancies, Glucose, BloodPressure, SkinThickness,
                                   Insulin, BMI, DiabetesPedigreeFunction, Age]).reshape(1, -1)
        result = diabetes_model.predict(diabetes_input)
        st.success("🔴 Diabetic" if result[0] == 1 else "🟢 Not Diabetic")

# ------------------------------------------
# 🧠 PARKINSON'S
elif selected == "Parkinson's":
    st.header("🧠 Parkinson's Disease Prediction")

    fo = st.number_input("MDVP:Fo(Hz)")
    fhi = st.number_input("MDVP:Fhi(Hz)")
    flo = st.number_input("MDVP:Flo(Hz)")
    jitter_percent = st.number_input("MDVP:Jitter(%)")
    jitter_abs = st.number_input("MDVP:Jitter(Abs)")
    rap = st.number_input("MDVP:RAP")
    ppq = st.number_input("MDVP:PPQ")
    ddp = st.number_input("Jitter:DDP")
    shimmer = st.number_input("MDVP:Shimmer")
    shimmer_db = st.number_input("MDVP:Shimmer(dB)")
    apq3 = st.number_input("Shimmer:APQ3")
    apq5 = st.number_input("Shimmer:APQ5")
    apq = st.number_input("MDVP:APQ")
    dda = st.number_input("Shimmer:DDA")
    nhr = st.number_input("NHR")
    hnr = st.number_input("HNR")
    rpde = st.number_input("RPDE")
    dfa = st.number_input("DFA")
    spread1 = st.number_input("spread1")
    spread2 = st.number_input("spread2")
    d2 = st.number_input("D2")
    ppe = st.number_input("PPE")

    if st.button("Predict Parkinson's"):
        parkinson_input = np.array([fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp,
                                    shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr,
                                    rpde, dfa, spread1, spread2, d2, ppe]).reshape(1, -1)
        result = parkinson_model.predict(parkinson_input)
        st.success("⚠️ Parkinson's Detected" if result[0] == 1 else "✅ No Parkinson's")

