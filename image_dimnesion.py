# height , width , color dimension// image.shape (Height,Width,channel)

#channel is 3 then R G B 

import cv2

image = cv2.imread(r"C:\Users\kansa\OneDrive\Desktop\sem 6\OpenCV\download.jpg")

if image is not None:
    h,w,c = image.shape
    print(f"Image is loaded :{h}\n {w}\n {c}")