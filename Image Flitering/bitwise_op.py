"""
1 -- cv2.bitwise_and(img1,img2) --> cut out the images
2 -- cv2.bitwise_or(img1,img2) --> merge the image
3 -- cv2.bitwise_not(img1) --> create the effect

image 1 and image 2 height and width should be same
use only black and white images
"""

import cv2
import numpy as np

image1 = np.zeros((300,300),dtype="uint8")
image2 = np.zeros((300,300),dtype="uint8")

cv2.circle(image1,(150,150),100,255,-1)
cv2.rectangle(image2,(100,100),(250,250),255,-1)

bitwise_and = cv2.bitwise_and(image1,image2)
bitwise_or = cv2.bitwise_or(image1,image2)
bitwise_not = cv2.bitwise_not(image1)

cv2.imshow("Original image1 with circle",image1)
cv2.imshow("Original image2 with rectange",image2)
cv2.imshow("Bitwise And",bitwise_and)
cv2.imshow("Bitwise or",bitwise_or)
cv2.imshow("Bitwise not",bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
