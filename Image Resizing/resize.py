import cv2

image = cv2.imread(r"C:\Users\kansa\OneDrive\Desktop\sem 6\OpenCV\download.jpg")

if image is not None:
    resized_image = cv2.resize(image, (300, 300))  # width is 300, height is 300
    cv2.imshow("Original Image", image)
    cv2.imshow("Resized Image", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    cv2.imwrite(r"C:\Users\kansa\OneDrive\Desktop\sem 6\OpenCV\Image Resizing\resized_image.jpg", resized_image)
    print("Resized image saved successfully.")
else:
    print("Failed to load the image.")