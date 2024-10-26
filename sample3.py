import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(page_title="Face Recognition System", layout="centered", initial_sidebar_state="collapsed")

# Custom CSS for advanced styling
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
            font-family: 'Roboto', sans-serif;
        }
        .main-header {
            color: #333;
            text-align: center;
            font-size: 2.5em;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .sub-header {
            text-align: center;
            font-size: 1.5em;
            color: #555;
            margin-bottom: 40px;
        }
        .cta-button {
            background-color: #ff6b6b;
            color: white;
            font-size: 1.2em;
            padding: 15px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
            display: inline-block;
            text-decoration: none;
        }
        .cta-button:hover {
            background-color: #ff3d3d;
        }
        .features {
            display: flex;
            justify-content: space-around;
            margin-top: 50px;
        }
        .feature-box {
            text-align: center;
            width: 30%;
        }
        .feature-box h2 {
            font-size: 1.8em;
            margin-bottom: 15px;
            color: #333;
        }
        .feature-box p {
            color: #777;
            font-size: 1.1em;
        }
        footer {
            text-align: center;
            color: #666;
            font-size: 0.9em;
            margin-top: 50px;
            padding: 10px;
            background-color: #333;
            color: #fff;
        }
    </style>
    """, unsafe_allow_html=True)

# Main content
st.markdown('<h1 class="main-header">Face Recognition System</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Advanced AI Technology for Real-time Face Recognition and Attendance Tracking</p>', unsafe_allow_html=True)

# Add a "Get Started" button
st.markdown('<a href="#" class="cta-button">Get Started</a>', unsafe_allow_html=True)

# Load an image for the homepage
image = Image.open('face_recognition_image2.jpg')  # Example image
st.image(image, caption='AI-Powered Face Recognition', use_column_width=True)

# Features section
st.markdown("""
<div class="features">
    <div class="feature-box">
        <h2>Real-time Recognition</h2>
        <p>Our system can detect and recognize faces in real-time with a high degree of accuracy.</p>
    </div>
    <div class="feature-box">
        <h2>High Accuracy</h2>
        <p>Achieve over 97% accuracy in detecting and recognizing faces.</p>
    </div>
    <div class="feature-box">
        <h2>Attendance Tracking</h2>
        <p>Automate attendance management and enhance security with our system.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<footer>
    <p>&copy; 2024 Face Recognition System. All rights reserved.</p>
</footer>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("Face Recognition System")
    st.write("Navigate through the options below:")
    st.button("Home")
    st.button("Features")
    st.button("About Us")
    st.button("Contact Us")
