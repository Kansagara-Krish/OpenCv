import cv2

# just start the camera to capture 
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read() # True or false frame=images
    
    if not ret:
        print("Could not read the image")
        break
    else:
        cv2.imshow("Capture image is",frame)
        
    #  wait for the 1s and check if q press then close
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Qutting...")
        break

#close the camera    
cap.release()
cv2.destroyAllWindows()
    