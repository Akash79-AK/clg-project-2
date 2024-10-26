import streamlit as st
import face_recognition
import cv2
import numpy as np
import os
from datetime import datetime

# Load known faces and their names
def load_known_faces():
    known_face_encodings = []
    known_face_names = []
    
    # Load images from the 'faces' directory
    for filename in os.listdir("faces"):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image = face_recognition.load_image_file(f"faces/{filename}")
            encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(encoding)
            known_face_names.append(os.path.splitext(filename)[0])
    
    return known_face_encodings, known_face_names

# Mark attendance in a file
def mark_attendance(name):
    with open("attendance.csv", "r+") as file:
        attendance_list = file.readlines()
        names = [line.split(",")[0] for line in attendance_list]
        
        if name not in names:
            now = datetime.now()
            dt_string = now.strftime('%H:%M:%S')
            file.write(f'{name},{dt_string}\n')

# Streamlit app
st.title("Face Recognition Attendance System")

# CSS styling
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

# Upload a photo for face recognition
uploaded_image = st.file_uploader("Upload an Image for Attendance", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Load known faces
    known_face_encodings, known_face_names = load_known_faces()
    
    # Load the uploaded image
    img = face_recognition.load_image_file(uploaded_image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Find faces and encodings in the uploaded image
    face_locations = face_recognition.face_locations(img)
    face_encodings = face_recognition.face_encodings(img, face_locations)
    
    # Initialize variable to store attendance results
    attendance_result = []

    # Process each face found in the uploaded image
    for face_encoding, face_location in zip(face_encodings, face_locations):
        # Compare the uploaded face with the known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            attendance_result.append(name)
            mark_attendance(name)
            
            # Display attendance status
            st.success(f"{name} is present!")
        else:
            st.error("Face not recognized!")

    # Show the processed image
    st.image(img, caption="Processed Image")

else:
    st.write("Please upload an image.")

