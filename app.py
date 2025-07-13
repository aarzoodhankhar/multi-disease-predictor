import streamlit as st
import numpy as np
import pickle
from fpdf import FPDF
import datetime
from firebase_config import auth, db  # Make sure firebase_config.py has `auth` and `db`

# --- Session ---
if "user" not in st.session_state:
    st.session_state.user = None

# --- Authentication ---
st.title("🔐 User Authentication")

choice = st.selectbox("Login / Sign Up", ["Login", "Sign Up"])
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if choice == "Sign Up":
    if st.button("Create Account"):
        try:
            user = auth.create_user_with_email_and_password(email, password)
            st.success("✅ Account created. Please login.")
        except:
            st.error("❌ Signup failed. Try different credentials.")
elif choice == "Login":
    if st.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.session_state.user = user
            st.success(f"✅ Logged in as {email}")
        except:
            st.error("❌ Login failed. Check credentials.")

# --- Show app only if logged in ---
if st.session_state.user:

    # --- Theme Toggle ---
    theme = st.sidebar.selectbox("🎨 Select Theme", ["Light", "Dark"])
    if theme == "Dark":
        st.markdown("""
            <style>
            body, .stApp { background-color: #0e1117; color: #FAFAFA; }
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
            h1, h2, h3 { color: #ad1457; }
            .stButton>button {
                background-color: #ec407a;
                color: white;
                border-radius: 8px;
                padding: 8px 16px;
                font-weight: bold;
            }
            </style>
        """, unsafe_allow_html=True)

    # --- Load ML Models ---
    diabetes_model = pickle.load(open('diabetes_model.pkl', 'rb'))
    heart_model = pickle.load(open('heart_model.pkl', 'rb'))
    parkinson_model = pickle.load(open('parkinson_model.pkl', 'rb'))

    # --- PDF Report ---
    def generate_pdf_report(disease, result, tips):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="🩺 Multi Disease Prediction Report", ln=True, align='C')
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

    # --- BMI Calculator ---
    st.markdown("---")
    st.header("📏 BMI Calculator")
    weight = st.number_input("Enter your weight (kg)", min_value=1.0)
    height = st.number_input("Enter your height (cm)", min_value=1.0)
    if height > 0 and weight > 0:
        bmi = weight / ((height / 100) ** 2)
        st.success(f"Your BMI is: **{bmi:.2f}**")
        if bmi < 18.5:
            st.warning("You are **Underweight** 😕. Try to eat well.")
        elif 18.5 <= bmi < 24.9:
            st.info("You are in **Normal weight** range 💪.")
        elif 25 <= bmi < 29.9:
            st.warning("You are **Overweight** 😬.")
        else:
            st.error("You are in **Obese** category 🚨. Please consult a doctor.")

    # --- App Main Title ---
    st.title('🩺 Multi Disease Prediction System')
    st.subheader("A Smart Health Assistant Powered by Machine Learning")

    # --- Disease Selection ---
    selected = st.selectbox("Choose Disease to Predict", ["Heart Disease", "Diabetes", "Parkinson's"])

    # --- Heart Disease ---
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
        thal = st.number_input("Thal (1 = Normal, 2 = Fixed, 3 = Reversible)")

        if st.button("Predict Heart Disease"):
            inputs = np.array([age, sex, cp, trestbps, chol, fbs, restecg,
                               thalach, exang, oldpeak, slope, ca, thal]).reshape(1, -1)
            result = heart_model.predict(inputs)
            user_id = st.session_state.user['localId']
            db.child("predictions").child(user_id).push({
                "disease": "Heart Disease",
                "result": int(result[0]),
                "date": str(datetime.datetime.now())
            })
            st.success("🦡 Positive for Heart Disease" if result[0] == 1 else "💚 No Heart Disease Detected")
            tips = [
                "Follow a heart-healthy diet",
                "Exercise daily",
                "Avoid smoking and alcohol",
                "Sleep well and manage stress",
                "Get regular checkups"
            ]
            filename = generate_pdf_report("Heart Disease", result[0], tips)
            st.download_button("📄 Download Report", data=open(filename, "rb"), file_name=filename)

    # --- Diabetes ---
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
            inputs = np.array([Pregnancies, Glucose, BloodPressure, SkinThickness,
                               Insulin, BMI, DiabetesPedigreeFunction, Age]).reshape(1, -1)
            result = diabetes_model.predict(inputs)
            user_id = st.session_state.user['localId']
            db.child("predictions").child(user_id).push({
                "disease": "Diabetes",
                "result": int(result[0]),
                "date": str(datetime.datetime.now())
            })
            st.success("🔴 Diabetic" if result[0] == 1 else "🟢 Not Diabetic")
            tips = [
                "Eat fiber-rich food",
                "Avoid sugar and junk",
                "Walk or exercise daily",
                "Drink more water",
                "Monitor sugar regularly"
            ]
            filename = generate_pdf_report("Diabetes", result[0], tips)
            st.download_button("📄 Download Report", data=open(filename, "rb"), file_name=filename)

    # --- Parkinson's ---
    elif selected == "Parkinson's":
        st.header("🧠 Parkinson's Disease Prediction")
        fields = [
            "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)",
            "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)",
            "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA", "NHR", "HNR",
            "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"
        ]
        inputs = [st.number_input(field) for field in fields]

        if st.button("Predict Parkinson's"):
            result = parkinson_model.predict(np.array(inputs).reshape(1, -1))
            user_id = st.session_state.user['localId']
            db.child("predictions").child(user_id).push({
                "disease": "Parkinson's",
                "result": int(result[0]),
                "date": str(datetime.datetime.now())
            })
            st.success("⚠️ Parkinson's Detected" if result[0] == 1 else "✅ No Parkinson's")
            tips = [
                "Exercise regularly",
                "Use speech therapy",
                "Sleep properly",
                "Take medicines on time",
                "Follow neurologist guidance"
            ]
            filename = generate_pdf_report("Parkinson's", result[0], tips)
            st.download_button("📄 Download Report", data=open(filename, "rb"), file_name=filename)

    # --- History ---
    st.markdown("---")
    st.header("📚 Your Prediction History")
    user_id = st.session_state.user['localId']
    history = db.child("predictions").child(user_id).get()
    if history.each():
        for record in reversed(history.each()):
            item = record.val()
            st.markdown(f"""
            **🕒 Date:** {item['date']}  
            **🦠 Disease:** {item['disease']}  
            **🧪 Result:** {"🟥 Positive" if item['result'] == 1 else "🟩 Negative"}
            ---""")
    else:
        st.info("No predictions found yet.")
