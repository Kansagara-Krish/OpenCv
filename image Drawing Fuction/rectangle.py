import cv2

image = cv2.imread(r"C:\Users\kansa\OneDrive\Desktop\sem 6\OpenCV\download.jpg")

if image is not None:
    image = cv2.resize(image, (300, 300))  # width is 300, height is 300
    image = cv2.rectangle(image, (50, 50), (200, 200), (0, 255, 0), thickness=-1)  # Draw a green rectangle from (50, 50) to (200, 200)
    
    cv2.imshow("Rectangle Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Failed to load the image.")