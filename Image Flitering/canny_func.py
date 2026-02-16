import cv2

image = cv2.imread(r"C:\Users\kansa\OneDrive\Desktop\sem 6\OpenCV\Image Flitering\natural.jpg",cv2.IMREAD_GRAYSCALE)

if image is not None:
    edges = cv2.Canny(image,50,150)
    # threshold1 , threshold2 and image should be  in grey scale
    cv2.imshow("Original",image)
    cv2.imshow("fliter",edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    