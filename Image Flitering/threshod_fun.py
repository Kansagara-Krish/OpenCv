import cv2

image = cv2.imread(r"C:\Users\kansa\OneDrive\Desktop\sem 6\OpenCV\Image Flitering\natural.jpg",cv2.IMREAD_GRAYSCALE)

if image is not None:
    ret , threshold_img = cv2.threshold(image,120,255,cv2.THRESH_BINARY)
    # threshold1 , threshold2 and image should be  in grey scale
    cv2.imshow("Original",image)
    cv2.imshow("Threshold image",threshold_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """
    90 - 0 black
    130 - 255 white
    180 - 255 white
    50 - 0 black
    
    100,120,150
    """