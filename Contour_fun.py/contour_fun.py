import cv2

image = cv2.imread(r"C:\Users\kansa\OneDrive\Desktop\sem 6\OpenCV\Contour_fun.py\triangle.png")

if image is not None:
    # Convert to grayscale for thresholding.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Binary threshold to separate object from background.
    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    # Find contours from the thresholded image.
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    print("Number of contours found = " + str(len(contours)))

    for i in range(len(contours)):
        # Draw each contour in green.
        cv2.drawContours(image, contours, i, (0, 255, 0), 3)

    cv2.imshow("Image with contours",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
