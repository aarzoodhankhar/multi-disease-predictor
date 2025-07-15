import streamlit as st

st.set_page_config(
    page_title="Multi Disease Predictor",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("<h1 style='text-align: center; color: #ad1457;'>🩺 Multi Disease Prediction System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>A Smart Health Assistant Powered by Machine Learning</p>", unsafe_allow_html=True)

# Optional: Add a health banner image
st.image("assets/health-banner.png", use_column_width=True)

st.markdown("---")

st.markdown("### 🔍 Features")
st.markdown("""
- 💉 **Diabetes**, ❤️ **Heart Disease**, 🧠 **Parkinson's** prediction  
- 📄 Personalized PDF Report generation  
- 📚 History Tracking via Firebase  
- 🎨 Theme Customization Support  
- 📏 BMI Calculator  
- 🔐 Secure Login & Sign-up System
""")

st.markdown("### 🧑‍⚕️ Get started from the sidebar →")
