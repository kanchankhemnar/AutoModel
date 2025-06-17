import streamlit as st
from backend.auth import login_user, signup_user

def login_page():
    st.title("🔐 Login to AutoModel")

    if "user" not in st.session_state:
        st.session_state.user = None

    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    with tab1:
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login"):
            user = login_user(email, password)
            if user:
                st.session_state.user = user
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Login failed. Please check your credentials.")

    with tab2:
        new_email = st.text_input("New Email", key="signup_email")
        new_password = st.text_input("New Password", type="password", key="signup_password")

        if st.button("Sign Up"):
            user = signup_user(new_email, new_password)
            if user:
                st.success("Sign-up successful. You can now log in!")
            else:
                st.error("Sign-up failed. Try a different email or password.")

def logout_button():
    st.success(f"Logged in as {st.session_state.user['email']}")
    if st.button("Logout"):
        st.session_state.user = None
        st.rerun()

