import streamlit as st

# Set page title
st.set_page_config(page_title="Login Page", page_icon="🔒")

# Custom CSS for background, fonts, and styling
st.markdown("""
    <style>
    body {
        background-color: 00FFFF;
        font-family: 'Arial', sans-serif;
    }
    .main {
        background-color: Cyan;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        width: 300px;
        margin: 0 auto;
    }
    .login-header {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: #333;
        margin-bottom: 20px;
    }
    .login-btn {
        background-color: #007bff;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
    }
    .login-btn:hover {
        background-color: #04AA6D;
    }
    </style>
    """, unsafe_allow_html=True)

# Create login form
def login_form():
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.markdown("<h2 class='login-header'>Login</h2>", unsafe_allow_html=True)
    
    # Login form inputs
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login", key="login", use_container_width=True):
        if username == "admin" and password == "admin123":
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Display the login form
login_form()
