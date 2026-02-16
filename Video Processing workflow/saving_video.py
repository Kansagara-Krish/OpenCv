import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Camera not accessible")
    exit()

success, image = camera.read()
if not success:
    print("Error: Cannot read frame")
    exit()

height, width, _ = image.shape

codec = cv2.VideoWriter_fourcc(*'XVID')
recorder = cv2.VideoWriter("my_video.avi", codec, 20, (width, height))

while True:
    success, image = camera.read()
    if not success:
        break

    recorder.write(image)
    cv2.imshow("Recording Live", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
recorder.release()
cv2.destroyAllWindows()
