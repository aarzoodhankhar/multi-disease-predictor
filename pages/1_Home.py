import streamlit as st
from datetime import datetime
from components.sidebar import show_sidebar

st.set_page_config(page_title="Dashboard", page_icon="💻", layout="wide")
show_sidebar()

# Global style overrides
st.markdown("""
    <style>
        body {
            background-color: #f9f9f9;
            font-family: 'Segoe UI', sans-serif;
        }
        .title {
            text-align: center;
            color: #e91e63;
            font-size: 40px;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #555;
            margin-bottom: 30px;
        }
        .features-box {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0px 2px 15px rgba(0, 0, 0, 0.1);
        }
        ul.features-list li {
            font-size: 16px;
            color: #444;
            margin-bottom: 10px;
        }
        .quote-box {
            background: #fff3e0;
            padding: 18px;
            border-radius: 10px;
            font-style: italic;
            font-size: 16px;
            color: #333;
            box-shadow: 0px 1px 10px rgba(0, 0, 0, 0.05);
        }
        .date-text {
            text-align: right;
            font-size: 14px;
            color: #888;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Heading
st.markdown("<div class='title'>🩺 Welcome to Your Health Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Your smart medical assistant — predicting with machine learning!</div>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Columns
col1, col2 = st.columns([1, 1.2])

with col1:
    st.image("https://cdn.pixabay.com/photo/2017/08/06/10/29/stethoscope-2598823_1280.jpg", use_column_width=True)

with col2:
    st.markdown("""
        <div class="features-box">
            <h3 style='color:#9c27b0;'>Features:</h3>
            <ul class='features-list'>
                <li>❤️ Heart Disease Detection</li>
                <li>💉 Diabetes Prediction</li>
                <li>🧠 Parkinson's Analysis</li>
                <li>📏 BMI Calculator</li>
                <li>📊 Prediction History</li>
                <li>📄 Downloadable PDF Reports</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# Motivational Quote
st.markdown("""
    <div class='quote-box'>
        🌟 <b>"Take care of your body. It’s the only place you have to live."</b>
    </div>
""", unsafe_allow_html=True)

# Date
st.markdown(f"<div class='date-text'>⏱️ {datetime.now().strftime('%A, %d %B %Y')}</div>", unsafe_allow_html=True)
