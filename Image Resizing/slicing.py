import cv2
image = cv2.imread(r"C:\Users\kansa\OneDrive\Desktop\sem 6\OpenCV\download.jpg")

if image is not None:
    # Slicing the image to get a region of interest (ROI)
    roi = image[100:400, 150:450]  # [y1:y2, x1:x2]
    
    cv2.imshow("Original Image", image)
    cv2.imshow("Region of Interest (ROI)", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(r"C:\Users\kansa\OneDrive\Desktop\sem 6\OpenCV\Image Resizing\roi_image.jpg", roi)
    print("ROI image saved successfully.")
else:
    print("Failed to load the image.")