import streamlit as st
from firebase_config import auth

st.set_page_config(page_title="Login / Sign Up", page_icon="🔐")

# Page styling
st.markdown("""
<style>
    .login-container {
        max-width: 400px;
        margin: auto;
        padding: 2rem;
        background-color: #fce4ec;
        border-radius: 12px;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
        color: #4a148c;
    }
    input {
        border-radius: 8px !important;
    }
    .stButton>button {
        background-color: #ba68c8;
        color: white;
        font-weight: bold;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="login-container">', unsafe_allow_html=True)

    st.markdown("## 🔐 Welcome")
    st.markdown("Log in or create an account to continue.")

    choice = st.radio("Choose action", ["Login", "Sign Up"])

    email = st.text_input("📧 Email")
    password = st.text_input("🔑 Password", type="password")

    if choice == "Sign Up":
        if st.button("Create Account"):
            try:
                user = auth.create_user_with_email_and_password(email, password)
                st.success("✅ Account created. Please login.")
            except Exception as e:
                st.error("❌ Signup failed. Try different credentials.")
    else:
        if st.button("Login"):
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state.user = user
                st.success(f"✅ Logged in as {email}")
                st.switch_page("pages/1_Home.py")  # redirect to Home page
            except Exception as e:
                st.error("❌ Login failed. Check credentials.")

    st.markdown('</div>', unsafe_allow_html=True)
