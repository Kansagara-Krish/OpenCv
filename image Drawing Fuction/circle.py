import cv2

image = cv2.imread(r"C:\Users\kansa\OneDrive\Desktop\sem 6\OpenCV\download.jpg")

if image is not None:
    image = cv2.resize(image, (300, 300))  # width is 300, height is 300
    image = cv2.circle(image, (150, 150), 50, (255,0, 0), thickness=-1)  # Draw a green circle with center at (150, 150) and radius of 50    
    cv2.imshow("Circle Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Failed to load the image.")