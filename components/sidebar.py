import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

def show_sidebar():
    st.sidebar.markdown("## 🧭 Navigation")
    add_vertical_space(1)

    if "user" in st.session_state and st.session_state.user:
        user_email = st.session_state.user.get("email", "User")

        st.sidebar.markdown(f"👤 Logged in as: `{user_email}`")
        add_vertical_space(2)

        if st.sidebar.button("🚪 Logout"):
            st.session_state.user = None
            st.success("Successfully logged out. Please refresh.")
            st.stop()
    else:
        st.sidebar.warning("Please login to continue.")
        st.stop()
