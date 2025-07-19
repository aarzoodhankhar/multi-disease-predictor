import streamlit as st

st.set_page_config(page_title="Multi Disease Predictor", layout="wide")

# Page Title
st.markdown("""
    <h1 style='text-align: center; color: #d63384; font-size: 3em;'>
        🩺 Multi-Disease Prediction System
    </h1>
""", unsafe_allow_html=True)

# Section Title
st.markdown("""
    <h3 style='text-align: center; color: #495057;'>
        Predict Heart Disease, Diabetes & Parkinson's Disease with AI
    </h3>
""", unsafe_allow_html=True)

st.write("---")

# Info Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div style='padding:20px; border-radius:10px; background-color:#ffe6e6;'>
            <h4 style='color:#c0392b;'>💓 Heart Disease</h4>
            <p>Upload details to check heart disease risk using ML.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style='padding:20px; border-radius:10px; background-color:#e6f7ff;'>
            <h4 style='color:#007acc;'>🍬 Diabetes</h4>
            <p>Analyze blood sugar & other health markers for diabetes prediction.</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div style='padding:20px; border-radius:10px; background-color:#f3e6ff;'>
            <h4 style='color:#8e44ad;'>🧠 Parkinson’s</h4>
            <p>Detect Parkinson's through voice and movement data using AI.</p>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# Footer or Motivation
st.markdown("""
    <p style='text-align: center; font-size: 1.1em; color: #6c757d;'>
        Built with ❤️ using Machine Learning and Python | Secure & Accurate
    </p>
""", unsafe_allow_html=True)
