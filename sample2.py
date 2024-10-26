import streamlit as st

users_db = {"user1": "password1", "user2": "password2"}

def registration_page():
    st.title("Register")
    
    new_username = st.text_input("Enter new username")
    new_password = st.text_input("Enter new password", type="password")
    
    if st.button("Register"):
        if new_username in users_db:
            st.error("Username already exists! Please choose a different one.")
        else:
            users_db[new_username] = new_password
            st.success("Registration successful! Please log in.")
            st.session_state['page'] = 'login'  

def login_page():
    st.title("Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username in users_db and users_db[username] == password:
            st.success(f"Welcome {username}!")
        else:
            st.error("Invalid username or password")
    
    st.markdown("Don't have an account? [Register here](#)")
    if st.button("Go to Registration"):
        st.session_state['page'] = 'register'  

st.markdown("""
    <style>
    body {
        background-color: #7FFF00;   
        font-family: 'Arial', sans-serif;
        color: black;    
    }
    .main {
        background-color: Chartreuse;    
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
        color: white;
        margin-bottom: 20px;
    }
    .login-btn {
        background-color: #007bff;
        color: black;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
    }
    .login-btn:hover {
        background-color: #04AA6D;
    }
    </style>
    """, unsafe_allow_html=True
)

if 'page' not in st.session_state:
    st.session_state['page'] = 'login'

if st.session_state['page'] == 'login':
    login_page()
else:
    registration_page()
