import streamlit as st
import numpy as np
import joblib
# UI Customization
st.markdown("""
    <style>
    .main {
        background-color: #fff5f8;
    }
    h1 {
        color: #e91e63;
        text-align: center;
    }
    .stButton > button {
        background-color: #e91e63;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🩺 Multi Disease Prediction System")
st.markdown("<h4 style='text-align: center;'>A Smart Health Assistant Powered by Machine Learning</h4>", unsafe_allow_html=True)

# Load Models
heart_model = joblib.load('heart_model.pkl')
diabetes_model = joblib.load('diabetes_model.pkl')
parkinson_model = joblib.load('parkinson_model.pkl')

# App Title
st.title("🩺 Multi Disease Prediction System")
st.sidebar.title("Choose Disease")

# Sidebar Selection
option = st.sidebar.radio("Select:", ["Heart Disease", "Diabetes", "Parkinson"])

# Heart Prediction
if option == "Heart Disease":
    st.header("❤️ Heart Disease Prediction")
    age = st.number_input("Age", min_value=1, max_value=120)
    sex = st.selectbox("Sex (1 = Male, 0 = Female)", [1, 0])
    cp = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure")
    chol = st.number_input("Cholesterol")
    thalach = st.number_input("Max Heart Rate")

    if st.button("Predict Heart Disease"):
        input_data = np.array([[age, sex, cp, trestbps, chol, thalach]])
        prediction = heart_model.predict(input_data)
        st.success("🟢 No Heart Disease") if prediction[0] == 0 else st.error("🔴 Heart Disease Detected!")

# Diabetes Prediction
elif option == "Diabetes":
    st.header("🧪 Diabetes Prediction")
    pregnancies = st.number_input("Pregnancies")
    glucose = st.number_input("Glucose Level", help="Enter your blood glucose level in mg/dL")

    bp = st.number_input("Blood Pressure")
    bmi = st.number_input("BMI")
    age = st.number_input("Age")

    if st.button("Predict Diabetes"):
        input_data = np.array([[pregnancies, glucose, bp, bmi, age]])
        prediction = diabetes_model.predict(input_data)
        st.success("🟢 No Diabetes") if prediction[0] == 0 else st.error("🔴 Diabetes Detected!")

# Parkinson Prediction
elif option == "Parkinson":
    st.header("🧠 Parkinson Prediction")
    fo = st.number_input("MDVP:Fo(Hz)")
    jitter = st.number_input("MDVP:Jitter(%)")
    shimmer = st.number_input("MDVP:Shimmer")
    hnr = st.number_input("HNR")
    rpde = st.number_input("RPDE")
    dfa = st.number_input("DFA")

    if st.button("Predict Parkinson"):
        input_data = np.array([[fo, jitter, shimmer, hnr, rpde, dfa]])
        prediction = parkinson_model.predict(input_data)
        st.success("🟢 No Parkinson") if prediction[0] == 0 else st.error("🔴 Parkinson Detected!")
