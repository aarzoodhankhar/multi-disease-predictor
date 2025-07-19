import streamlit as st
from datetime import datetime
from components.sidebar import show_sidebar

st.set_page_config(page_title="Dashboard", page_icon="💻")
show_sidebar()

# Top heading
st.markdown("""
    <div style="text-align:center; padding:20px 0;">
        <h1 style="color:#e91e63; font-size:42px; margin-bottom:10px;">🩺 Health Prediction Dashboard</h1>
        <p style="font-size:18px; color:#444;">
            Your Smart Medical Assistant — Powered by Machine Learning
        </p>
    </div>
    <hr style="border: 1px solid #ccc;">
""", unsafe_allow_html=True)

# Layout in two columns
col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown("""
        <div style="background-color:#f8f9fa; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05);">
            <h3 style='color:#6a1b9a;'>🔍 Explore Features</h3>
            <ul style='font-size:16px; color:#333; line-height:1.8; padding-left:20px;'>
                <li>❤️ Heart Disease Detection</li>
                <li>💉 Diabetes Prediction</li>
                <li>🧠 Parkinson's Analysis</li>
                <li>📏 BMI Calculator</li>
                <li>📊 Prediction History</li>
                <li>📄 PDF Report Downloads</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style="background-color:#fff3e0; padding:25px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05);">
            <h4 style="color:#e65100;">✨ Empowering Health, One Prediction at a Time</h4>
            <p style="color:#444; font-size:15px; margin-top:10px;">
                Make proactive decisions with the help of predictive AI models. Monitor your health status, download reports, and keep everything in check — all in one dashboard.
            </p>
            <p style='font-style:italic; color:#5e35b1; margin-top:20px;'>
                🌟 "Take care of your body. It’s the only place you have to live."
            </p>
        </div>
    """, unsafe_allow_html=True)

# Footer: date and time
st.markdown(f"""
    <p style='text-align:right; font-size:14px; color:#888; margin-top:30px;'>
        ⏱️ {datetime.now().strftime('%A, %d %B %Y')}
    </p>
""", unsafe_allow_html=True)
