import cv2
import face_recognition
import os
import numpy as np
from flask import Flask, render_template, Response, request
import csv
from datetime import datetime

app = Flask(__name__)

# Load known faces from a folder (you can modify this to your own path)
known_face_encodings = []
known_face_names = []

path = C:\Users\skabu\OneDrive\Desktop\archive (1)\lfw-deepfunneled\lfw-deepfunneled
for filename in os.listdir(path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img = face_recognition.load_image_file("C:\Users\skabu\OneDrive\Desktop\archive (1)\lfw-deepfunneled\lfw-deepfunneled")
        encoding = face_recognition.face_encodings(img)[0]
        known_face_encodings.append(encoding)
        known_face_names.append(os.path.splitext(filename)[0])

# Initialize variables
face_locations = []
face_encodings = []
face_names = []

def gen_frames():
    video_capture = cv2.VideoCapture(0)

    while True:
        success, frame = video_capture.read()
        if not success:
            break

        # Resize frame to speed up the face recognition process
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Find all the faces and face encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

            # Record attendance
            if name != "Unknown":
                with open("attendance.csv", "a") as f:
                    now = datetime.now()
                    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
                    f.write(f"{name},{dt_string}\n")

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
