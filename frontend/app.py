import streamlit as st

from services import api

st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="centered"
)

# ---- Session state ----
if "access_token" not in st.session_state:
    st.session_state.access_token = None
    st.session_state.user_name = None
    st.session_state.user_email = None


def is_logged_in() -> bool:
    return st.session_state.access_token is not None


def logout():
    st.session_state.access_token = None
    st.session_state.user_name = None
    st.session_state.user_email = None
    st.rerun()


# ---- Logged-in view ----
if is_logged_in():
    st.title("💰 Expense Tracker")
    st.success(f"Logged in as **{st.session_state.user_name}** ({st.session_state.user_email})")

    st.write(
        "Use the sidebar to add expenses, browse your history, "
        "or view your spending dashboard."
    )

    if st.button("Log out"):
        logout()

    st.stop()

# ---- Logged-out view: Login / Register ----
st.title("💰 Expense Tracker")
st.caption("Track your spending, see where your money goes.")

tab_login, tab_register = st.tabs(["Log in", "Sign up"])

with tab_login:
    with st.form("login_form"):
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        submitted = st.form_submit_button("Log in", use_container_width=True)

        if submitted:
            if not email or not password:
                st.error("Please enter both email and password.")
            else:
                with st.spinner("Logging in..."):
                    result = api.login(email, password)

                if result.get("status") == "success":
                    data = result["data"]
                    st.session_state.access_token = data["access_token"]
                    st.session_state.user_name = data["name"]
                    st.session_state.user_email = data["email"]
                    st.rerun()
                else:
                    st.error(result.get("message", "Login failed."))

with tab_register:
    with st.form("register_form"):
        name = st.text_input("Name", key="register_name")
        reg_email = st.text_input("Email", key="register_email")
        reg_password = st.text_input("Password", type="password", key="register_password")
        confirm_password = st.text_input("Confirm password", type="password", key="register_confirm")
        submitted = st.form_submit_button("Create account", use_container_width=True)

        if submitted:
            if not name or not reg_email or not reg_password:
                st.error("Please fill in all fields.")
            elif reg_password != confirm_password:
                st.error("Passwords don't match.")
            elif len(reg_password) < 6:
                st.error("Password should be at least 6 characters.")
            else:
                with st.spinner("Creating account..."):
                    result = api.register(name, reg_email, reg_password)

                if result.get("status") == "success":
                    st.success("Account created! Please log in from the 'Log in' tab.")
                else:
                    st.error(result.get("message", "Registration failed."))
