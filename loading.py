import cv2

image = cv2.imread(r"C:\Users\kansa\OneDrive\Desktop\sem 6\OpenCV\download.jpg")

if image is not None:
    success = cv2.imwrite("output_write.png",image)
    if success:
        print("Image saved succesfully as output_write.png")
   # cv2.imshow("Image showing",image) #open the window
    #cv2.waitKey(0)#wait for a key
    #cv2.destroyAllWindows() #close the window
    else:
        print("Failed to save")


else:
    print("Image load")
    
