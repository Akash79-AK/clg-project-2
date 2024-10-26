import streamlit as st
from streamlit.components.v1 import html

# --- Custom CSS for complex design ---
custom_css = """
<style>
    body {
        background-color: #FFF8DC rgb(255, 248, 220);
        font-family: Arial, sans-serif;
    }
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .login-box, .register-box {
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        padding: 40px;
        width: 350px;
        text-align: center;
    }
    .login-box h2, .register-box h2 {
        margin-bottom: 30px;
        color: #333;
    }
    .login-box input[type="text"], .login-box input[type="password"],
    .register-box input[type="text"], .register-box input[type="password"], .register-box input[type="email"] {
        width: 100%;
        padding: 10px;
        margin-bottom: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    .login-box input[type="submit"], .register-box input[type="submit"] {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px;
        cursor: pointer;
        border-radius: 5px;
        width: 100%;
    }
    .login-box input[type="submit"]:hover, .register-box input[type="submit"]:hover {
        background-color: #45a049;
    }
    .toggle-link {
        display: block;
        margin-top: 20px;
        color: #007bff;
        cursor: pointer;
    }
    .toggle-link:hover {
        text-decoration: underline;
    }
</style>
"""

# --- HTML for login form ---
login_html = """
<div class="container">
    <div class="login-box">
        <h2>Login</h2>
        <form action="" method="post">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <input type="submit" value="Login">
        </form>
        <a class="toggle-link" href="#" onclick="switchToRegister()">Don't have an account? Register here</a>
    </div>
</div>
"""

# --- HTML for registration form ---
register_html = """
<div class="container">
    <div class="register-box">
        <h2>Register</h2>
        <form action="" method="post">
            <input type="text" name="username" placeholder="Username" required>
            <input type="email" name="email" placeholder="Email" required>
            <input type="password" name="password" placeholder="Password" required>
            <input type="password" name="confirm_password" placeholder="Confirm Password" required>
            <input type="submit" value="Register">
        </form>
        <a class="toggle-link" href="#" onclick="switchToLogin()">Already have an account? Login here</a>
    </div>
</div>
"""

# --- Javascript to toggle between login and registration ---
toggle_script = """
<script type="text/javascript">
    function switchToRegister() {
        document.querySelector(".login-box").style.display = "none";
        document.querySelector(".register-box").style.display = "block";
    }

    function switchToLogin() {
        document.querySelector(".register-box").style.display = "none";
        document.querySelector(".login-box").style.display = "block";
    }
</script>
"""

# --- Streamlit application ---
def main():
    # Insert custom CSS for styling
    st.markdown(custom_css, unsafe_allow_html=True)

    # Title
    st.title("Complex Login and Registration System")

    # Default to showing login form
    form_type = st.session_state.get('form_type', 'login')

    # Handle login and registration toggling
    if form_type == 'login':
        # Display login form
        html(login_html + toggle_script, height=400)
        st.session_state['form_type'] = 'login'
    else:
        # Display registration form
        html(register_html + toggle_script, height=500)
        st.session_state['form_type'] = 'register'

    # Logic to toggle form type on button clicks
    if st.button("Switch to Register"):
        st.session_state['form_type'] = 'register'
    elif st.button("Switch to Login"):
        st.session_state['form_type'] = 'login'

if __name__ == "__main__":
    main()
