import cv2
import numpy as np
image = cv2.imread(r"C:\Users\kansa\OneDrive\Desktop\sem 6\OpenCV\Image Flitering\blur_nature.jpg")

if image is not None:
    print("Image loaded successfully.")
    
    sharp_kernel = np.array([[0, -1, 0],
                             [-1, 5, -1],
                             [0, -1, 0]])
    
    cv2.filter2D(image, -1, sharp_kernel, dst=image)
    #image = cv2.resize(image, (500,5000), fx=1.5, fy=1.5)
    cv2.imshow("Original Image", image)
    cv2.imshow("Sharpened Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()