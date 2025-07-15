import streamlit as st
from datetime import datetime
from components.sidebar import show_sidebar
st.set_page_config(page_title="Dashboard", page_icon="💻")
show_sidebar()
# Stylish heading
st.markdown("""
    <h1 style="text-align:center; color:#e91e63;">🩺 Welcome to Your Health Dashboard</h1>
    <p style="text-align:center; font-size:18px; color:#555;">
        Your smart medical assistant — predicting with machine learning!
    </p>
    <hr style="border: 1px solid #e0e0e0;">
""", unsafe_allow_html=True)

# Layout: Two columns
col1, col2 = st.columns(2)

with col1:
    st.image("https://cdn.pixabay.com/photo/2017/02/01/11/50/heart-2026154_1280.png", use_column_width=True)

with col2:
    st.markdown("""
        <h3 style='color:#9c27b0;'>Features:</h3>
        <ul style='font-size:16px; color:#444;'>
            <li>❤️ Heart Disease Detection</li>
            <li>💉 Diabetes Prediction</li>
            <li>🧠 Parkinson's Analysis</li>
            <li>📏 BMI Calculator</li>
            <li>📊 Prediction History</li>
            <li>📄 Downloadable PDF Reports</li>
        </ul>
    """, unsafe_allow_html=True)

# Motivational Quote
st.markdown("""
    <div style='background:#fff3e0; padding:15px; border-radius:10px; margin-top:20px; font-style:italic;'>
        🌟 <b>"Take care of your body. It’s the only place you have to live."</b>
    </div>
""", unsafe_allow_html=True)

# Current time
st.markdown(f"<p style='text-align:right; font-size:14px; color:#888;'>⏱️ {datetime.now().strftime('%A, %d %B %Y')}</p>", unsafe_allow_html=True)
