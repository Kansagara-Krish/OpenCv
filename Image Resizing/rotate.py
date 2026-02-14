import cv2

image = cv2.imread(r"C:\Users\kansa\OneDrive\Desktop\sem 6\OpenCV\download.jpg")

if image is not None:
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, 90, 1.0)  # create matrix for rotation (center, angle, scale)
    rotated_image = cv2.warpAffine(image, M, (w, h))
    rotated_image = cv2.resize(rotated_image, (300, 300))  # Resize the rotated image to 300x300
    cv2.imshow("Original Image", image)
    cv2.imshow("Rotated Image", rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(r"C:\Users\kansa\OneDrive\Desktop\sem 6\OpenCV\Image Resizing\rotated_image.jpg", rotated_image)
    print("Rotated image saved successfully.")
else:
    print("Failed to load the image.")