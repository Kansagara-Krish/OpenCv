import cv2

image = cv2.imread(r"C:\Users\kansa\OneDrive\Desktop\sem 6\OpenCV\Image Flitering\natural.jpg")

blurred_image = cv2.medianBlur(image, 15)

cv2.imshow("Original Image", image)
cv2.imshow("Median Blurred Image", blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()