import cv2

image = cv2.imread(r"C:\Users\kansa\OneDrive\Desktop\sem 6\OpenCV\download.jpg")

if image is not None:
    line_image = cv2.line(image, (50, 50), (20, 50), (0, 255, 0), thickness=5)  # Draw a green line from (50, 50) to (200, 200)
    
    print("Line drawn successfully.")
    cv2.imshow("Line Image", line_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("Failed to load the image.")