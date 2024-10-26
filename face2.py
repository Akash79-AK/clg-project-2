import streamlit as st
import sqlite3
import hashlib
# Custom CSS for styling
def custom_css():
    st.markdown("""
        <style>
        body{
            background-color: #7FFFD4;
            color: Aquamarine; 
         }
        /* Center the form */
        .stTextInput, .stPasswordInput {
            max-width: 400px;
            margin: 0 auto;
        }
        /* Customize buttons */
        .stButton button {
            background-color: #6C63FF;
            color: white;
            border-radius: 5px;
            padding: 10px;
            border: none;
        }
        /* Hover effect */
        .stButton button:hover {
            background-color: #7FFFD4;
            color: Aquamarine;    
        }
        /* Titles styling */
        h2 {
            font-family: 'Arial', sans-serif;
            font-size: 36px;
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)



# Hash password for security
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Database initialization
def create_user_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       username TEXT UNIQUE, 
                       password TEXT)''')
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

def check_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

# Create user table
create_user_table()

# Login Page
def login_page():
    st.markdown("<h2 style='text-align: center; color: #6C63FF;'>Login</h2>", unsafe_allow_html=True)
    st.write("Please log in to access the dashboard.")

    with st.form(key='login_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        submit_button = st.form_submit_button(label='Login')

    if submit_button:
        hashed_password = hash_password(password)
        if check_user(username, hashed_password):
            st.success(f"Welcome, {username}!")
        else:
            st.error("Incorrect username or password")

# Registration Page
def registration_page():
    st.markdown("<h2 style='text-align: center; color: #6C63FF;'>Register</h2>", unsafe_allow_html=True)
    st.write("Create a new account.")

    with st.form(key='registration_form'):
        new_username = st.text_input("Choose a Username")
        new_password = st.text_input("Choose a Password", type='password')
        confirm_password = st.text_input("Confirm Password", type='password')
        submit_button = st.form_submit_button(label='Register')

    if submit_button:
        if new_password == confirm_password:
            hashed_password = hash_password(new_password)
            try:
                add_user(new_username, hashed_password)
                st.success("Registration successful! Please log in.")
            except sqlite3.IntegrityError:
                st.error("Username already taken, please choose another one.")
        else:
            st.error("Passwords do not match!")

# Main Page Layout
def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Login", "Register"])

    if selection == "Login":
        login_page()
    else:
        registration_page()

if __name__ == "__main__":
    main()

# Call custom CSS
custom_css()