import streamlit as st

# A dictionary to simulate a database of users
users_db = {"user1": "password1", "user2": "password2"}

# Function to display registration page
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
            st.session_state['page'] = 'login'  # Redirect to login page after registration

# Function to display login page
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
        st.session_state['page'] = 'register'  # Switch to registration page when clicked

# Set up page layout and styles
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f5;
    }
    .stTextInput > label {
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Initialize session state to track pages
if 'page' not in st.session_state:
    st.session_state['page'] = 'login'

# Page navigation based on session state
if st.session_state['page'] == 'login':
    login_page()
else:
    registration_page()
