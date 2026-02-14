import cv2
image = cv2.imread(r"C:\Users\kansa\OneDrive\Desktop\sem 6\OpenCV\download.jpg")
if image is not None:
    l = {0: "Flip around x-axis",
         1: "Flip around y-axis",
         -1: "Flip around both axes"}
    
    # 0 means flipping image top to bottom 
    # 1 meand flipping image left to right
    # -1 means flipping image both axes (top to bottom and left to right)
    
    cv2.imshow("Original Image", image)
    for i in l:
        fliped_image = cv2.flip(image,i) 
        cv2.imshow(l[i] ,fliped_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
else:
    print("Failed to load the image.")