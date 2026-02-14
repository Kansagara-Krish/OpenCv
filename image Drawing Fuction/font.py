import cv2

image = cv2.imread(r"C:\Users\kansa\OneDrive\Desktop\sem 6\OpenCV\download.jpg")

if image is not None:
    image = cv2.putText(image, "OpenCV", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), thickness=2)  # Draw text "OpenCV" at (50, 100) in red color
    
    cv2.imshow("Text Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Failed to load the image.")