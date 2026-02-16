import cv2

# Load the Haar cascade for face detection.
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Load the Haar cascade for eye detection.
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
# Load the Haar cascade for smile detection.
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Capture video from webcam (0 is the default camera)
cap = cv2.VideoCapture(0)

# Main loop for continuous video processing
while True:
    # Read frame from the video capture
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for cascade detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect all faces in the current frame
    # Scale factor: 1.3 means the image size is reduced by 30% at each scale
    # minNeighbors: 5 means each region is accepted only if 5+ neighbors approve
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Process each detected face
    for (x, y, w, h) in faces:
        # Draw rectangle around the face (blue color - BGR format)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # Add label "Face" above the rectangle
        cv2.putText(frame, 'Face', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        
        # Extract the face region (Region of Interest - ROI) for eye and smile detection
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Detect eyes within the face region
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            # Draw rectangle around eyes (green color)
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            # Add label "Eye" above the eye rectangle
            cv2.putText(roi_color, 'Eye', (ex, ey - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Detect smiles within the face region
        smiles = smile_cascade.detectMultiScale(roi_gray)
        for (sx, sy, sw, sh) in smiles:
            # Draw rectangle around smile (red color)
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)
            # Add label "Smile" above the smile rectangle
            cv2.putText(roi_color, 'Smile', (sx, sy - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the processed frame in a window
    cv2.imshow('Face Detection with Eyes and Smile', frame)

    # Exit the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break