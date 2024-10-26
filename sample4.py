import streamlit as st

# Advanced CSS styling
st.markdown("""
    <style>
        body {
            background-color: #f7f7f7;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .container {
            max-width: 400px;
            margin: 0 auto;
            padding: 50px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        .title {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: #333;
        }
        .input-text {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
            font-size: 16px;
        }
        .button {
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }
        .button:hover {
            background-color: #45a049;
        }
        .link {
            display: block;
            text-align: center;
            margin-top: 10px;
            font-size: 14px;
            color: #007BFF;
            text-decoration: none;
        }
        .link:hover {
            text-decoration: underline;
        }
        .error {
            color: red;
            font-size: 14px;
        }
    </style>
    """, unsafe_allow_html=True)

# Login/Registration form logic
def show_login_form():
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    st.markdown("<div class='title'>Login</div>", unsafe_allow_html=True)
    username = st.text_input("Username", "", placeholder="Enter your username", key="login_username")
    password = st.text_input("Password", "", type="password", placeholder="Enter your password", key="login_password")
    if st.button("Login", key="login_button"):
        if username == "user" and password == "pass":
            st.success("Login successful!")
        else:
            st.markdown("<div class='error'>Invalid credentials</div>", unsafe_allow_html=True)
    st.markdown("<a class='link' href='#' onclick='window.location.reload();'>Forgot Password?</a>", unsafe_allow_html=True)
    st.markdown("<a class='link' href='#' onclick='show_registration_form()'>Create a new account</a>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def show_registration_form():
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    st.markdown("<div class='title'>Register</div>", unsafe_allow_html=True)
    new_username = st.text_input("Username", "", placeholder="Enter your username", key="reg_username")
    new_password = st.text_input("Password", "", type="password", placeholder="Enter your password", key="reg_password")
    confirm_password = st.text_input("Confirm Password", "", type="password", placeholder="Confirm your password", key="reg_confirm_password")
    if st.button("Register", key="reg_button"):
        if new_password == confirm_password:
            st.success("Registration successful! You can now log in.")
            st.session_state["page"] = "login"
        else:
            st.markdown("<div class='error'>Passwords do not match</div>", unsafe_allow_html=True)
    st.markdown("<a class='link' href='#' onclick='show_login_form()'>Already have an account? Log in</a>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Manage page state
if "page" not in st.session_state:
    st.session_state["page"] = "login"

# Show appropriate page
if st.session_state["page"] == "login":
    show_login_form()
else:
    show_registration_form()
