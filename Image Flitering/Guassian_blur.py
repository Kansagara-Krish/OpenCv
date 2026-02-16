import cv2

image = cv2.imread(r"C:\Users\kansa\OneDrive\Desktop\sem 6\OpenCV\Image Flitering\natural.jpg")

if image is not None:
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
    
    cv2.imshow("Original Image", image)
    cv2.imshow("Gaussian Blurred Image", blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Image not found or cannot be loaded.")
    