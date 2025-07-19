import streamlit as st
import numpy as np
import pickle
import os
import datetime
from components.sidebar import show_sidebar
# from components.pdf_generator import generate_pdf_report
from firebase_config import db

# --- Setup ---
st.set_page_config(page_title="Parkinson's Prediction", page_icon="🧠")
show_sidebar()

# --- Load Model ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "../models/parkinson_model.pkl")
parkinson_model = pickle.load(open(model_path, 'rb'))

# --- Header ---
st.markdown("""
    <h2 style='color:#e91e63;'>🧠 Parkinson's Disease Prediction</h2>
    <p style='color:#555;'>Fill in the voice-related biomedical features for prediction.</p>
    <hr style="border: 1px solid #e0e0e0;">
""", unsafe_allow_html=True)

# --- Parkinson’s Feature Inputs ---
fields = [
    "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)",
    "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)",
    "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA", "NHR", "HNR",
    "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"
]

with st.form("parkinsons_form"):
    st.markdown("<div style='background-color:#ede7f6; padding:20px; border-radius:10px;'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    inputs_col1 = []
    inputs_col2 = []

    for i in range(len(fields)):
        if i % 2 == 0:
            inputs_col1.append(col1.number_input(fields[i]))
        else:
            inputs_col2.append(col2.number_input(fields[i]))

    st.markdown("</div>", unsafe_allow_html=True)
    submitted = st.form_submit_button("🔍 Predict")

# --- Prediction ---
if submitted:
    inputs = inputs_col1 + inputs_col2
    result = parkinson_model.predict(np.array(inputs).reshape(1, -1))

    if st.session_state.user:
        user_id = st.session_state.user['localId']
        db.child("predictions").child(user_id).push({
            "disease": "Parkinson's",
            "result": int(result[0]),
            "date": str(datetime.datetime.now())
        })

    # --- Display Result ---
    if result[0] == 1:
        st.error("⚠️ Parkinson's likely. Please consult a neurologist.")
    else:
        st.success("✅ No signs of Parkinson's detected.")

    # --- Tips & Report ---
    tips = [
        "Do regular physical therapy and stretching",
        "Use speech therapy for clarity",
        "Maintain a healthy diet and good sleep routine",
        "Take medications consistently",
        "Follow up with your neurologist"
    ]
    # filename = generate_pdf_report("Parkinson's", result[0], tips)
    # st.download_button("📄 Download Your Report", data=open(filename, "rb"), file_name=filename)
