import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="📏")
from components.sidebar import show_sidebar

# 🔒 Show sidebar
show_sidebar()

# --- BMI Calculator Header ---
st.markdown("""
    <h2 style='color:#e91e63;'>📏 BMI (Body Mass Index) Calculator</h2>
    <p style='color:#555;'>Calculate your BMI and learn where you stand.</p>
    <hr style="border: 1px solid #e0e0e0;">
""", unsafe_allow_html=True)

# --- BMI Card Layout ---
with st.container():
    st.markdown("<div style='background-color: #fce4ec; padding: 20px; border-radius: 10px;'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        weight = st.number_input("⚖️ Enter your weight (kg)", min_value=1.0)
    with col2:
        height = st.number_input("📏 Enter your height (cm)", min_value=1.0)

    # Calculate BMI
    if height > 0 and weight > 0:
        bmi = weight / ((height / 100) ** 2)
        st.success(f"🎯 Your BMI is: **{bmi:.2f}**")

        # Result display
        if bmi < 18.5:
            st.warning("🔶 You are **Underweight** 😕. Try to eat well and consult a nutritionist.")
        elif 18.5 <= bmi < 24.9:
            st.info("✅ You are in **Normal weight** range 💪.")
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ You are **Overweight** 😬. Consider a healthier routine.")
        else:
            st.error("🚨 You are in **Obese** category. Please consult a doctor.")

    st.markdown("</div>", unsafe_allow_html=True)
