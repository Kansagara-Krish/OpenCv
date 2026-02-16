import cv2
import os

# Load cascade classifier from OpenCV data folder
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

if face_cascade.empty():
    raise ValueError("Failed to load cascade classifier")

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5) # scale fector and minNeighbors parameters can be adjusted for better results
    
    # 1.1 is better for smaller faces, 1.3 is better for larger faces.
    # minNeighbors is the number of neighbors each candidate rectangle should have to retain it. Higher
    # if minNeighbors is set to 3 means is loose check and more false positives, if set to 5 means is strict check and less false positives but may miss some faces.

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, 'Face', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        #print(f"Face detected at: x={x}, y={y}, width={w}, height={h}")

    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break