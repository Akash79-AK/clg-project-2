import streamlit as st

# Custom CSS to style the page
def add_custom_css():
    st.markdown(
        """
        <style>
        /* General page style */
        body {
            font-family: 'Arial', sans-serif;
            background-color: 04AA6D;
            color: #334;
        }

        /* Centering the login box */
        .login-box {
            max-width: 400px;
            margin: 50px auto;
            padding: 20px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }

        /* Input fields */
        .login-box input[type="text"], .login-box input[type="password"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        /* Login button */
        .login-box button {
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            border: none;
            color: white;
            border-radius: 5px;
            cursor: pointer;
        }

        .login-box button:hover {
            background-color: #04AA6D;
        }
        </style>
        """, unsafe_allow_html=True
    )

# Function to handle login logic
def login(username, password):
    # Example: Hardcoded login credentials
    if username == "admin" and password == "password":
        st.success("Login successful!")
        return True
    else:
        st.error("Invalid username or password.")
        return False

def main():
    st.title("Login Page")

    # Add the custom CSS for styling
    add_custom_css()

    # Create login form in a centered box
    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Login button
    if st.button("Login"):
        # Authenticate user
        if login(username, password):
            st.write(f"Welcome, {username}!")

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
