import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Registration Page", layout="centered")

# Custom CSS for background, font, and form styling
page_bg_img = '''
<style>
body {
    background-image: url("https://www.example.com/background.jpg");
    background-size: cover;
    font-family: 'Arial', sans-serif;
}

h1, label {
    color: white;
    text-align: center;
    font-family: 'Verdana', sans-serif;
}

form {
    max-width: 400px;
    margin: 100px auto;
    padding: 30px;
    background: rgba(0, 0, 0, 0.7);
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

input[type="text"], input[type="password"], input[type="email"] {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    border-radius: 5px;
    border: 1px solid #ccc;
}

input[type="submit"] {
    width: 100%;
    padding: 10px;
    border: none;
    background: #4CAF50;
    color: white;
    border-radius: 5px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background: #45a049;
}
</style>
'''

# Apply the custom CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

# Create the registration form
st.markdown("<h1>Register Here</h1>", unsafe_allow_html=True)

with st.form("registration_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    # Add submit button
    submitted = st.form_submit_button("Register")
    
    if submitted:
        st.success(f"Registration successful for {name}")

