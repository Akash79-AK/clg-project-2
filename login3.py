import streamlit as st

# Create a function for the login page
def login():
    st.title("Login Page")
    
    # Set default username and password for demo purposes
    username_correct = "admin"
    password_correct = "password123"

    # Create input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        if username == username_correct and password == password_correct:
            st.success("Logged in successfully!")
            return True
        else:
            st.error("Incorrect Username or Password")
            return False

# Main function to control the app's flow
def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if not st.session_state['logged_in']:
        st.session_state['logged_in'] = login()

    if st.session_state['logged_in']:
        st.write("Welcome to the application!")

# Run the app
if __name__ == '__main__':
    main()
