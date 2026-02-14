#  "C:\Users\kansa\OneDrive\Desktop\sem 6\OpenCV\download.jpg"
# Script to draw shapes (line, circle, rectangle, text) on an image using OpenCV

import cv2  # OpenCV library for image processing
import os   # OS library to check file path existence

# Get image path from user
path = input("Enter the path of the image: ")
path = path.strip('"').strip("'")  # Remove quotes from path if present

# Check if the image file exists
if os.path.exists(path):
    image = cv2.imread(path)  # Read the image from the given path
    
    if image is not None:  # Check if image was loaded successfully
        print("Image loaded successfully.")
        # Get the shape to draw from user
        shape = input("What do you want to draw on the image? (line/circle/rectangle/text): ")
        
        # Draw a line on the image
        if shape.lower() == "line":
            x11 = int(input("Enter the first point X axis of line:- "))
            x12 = int(input("Enter the first point Y axis of line:- "))
            x21 = int(input("Enter the second point X axis of line:- "))
            x22 = int(input("Enter the second point Y axis of line:- "))
            x1 = (x11,x12)  # First endpoint
            x2 = (x21,x22)  # Second endpoint
            # Draw line with blue color (255,0,0 in BGR) and thickness 5
            new_image = cv2.line(image,x1,x2,(255,0,0),thickness=5)
        
        # Draw a rectangle on the image
        if shape.lower() == "rectangle":
            x11 = int(input("Enter the first point X axis of rectangle:- "))
            x12 = int(input("Enter the first point Y axis of rectangle:- "))
            x21 = int(input("Enter the second point X axis of rectangle:- "))
            x22 = int(input("Enter the second point Y axis of rectangle:- "))
            x1 = (x11,x12)  # Top-left corner
            x2= (x21,x22)   # Bottom-right corner
            # Draw rectangle with blue color and thickness 5
            new_image = cv2.rectangle(image,x1,x2,(255,0,0),thickness=5)
            
        # Draw a circle on the image
        if shape.lower() == "circle":
            center_x = int(input("Enter the X axis of point of circle:- "))
            center_y = int(input("Enter the Y axis of point of circle:- "))
            center = (center_x,center_y)  # Center coordinates
            radius = int(input("Enter the radius of circle:- "))
            # Draw filled circle (thickness=-1 means fill) with blue color
            new_image = cv2.circle(image,center,radius,(255,0,0),thickness=-1)
            
        # Add text on the image
        if shape.lower() == "text":
            text = input("What to you want to write?:- ")
            x1_x = int(input("Enter the X axis of position of the text:- "))
            x1_y = int(input("Enter the Y axis of position of the text:- "))
            x1 = (x1_x,x1_y)  # Text position
            # Add text with red color (0,0,255 in BGR) and thickness 2
            new_image = cv2.putText(image,text,x1,cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),thickness=2)
        else:
            # If invalid shape is chosen, keep original image
            print("Invalid shape choice.")
            new_image = image
        
        # Ask user whether to save or display the modified image
        ans = input("Image updated do you want to save ? (yes/no) or directly open it:- " )
        
        if ans.lower() == "yes":
            # Save the modified image
            cv2.imwrite(r"C:\Users\kansa\OneDrive\Desktop\sem 6\OpenCV\image Drawing Fuction\output.jpg",new_image)
            print("Image store!!")
        else:
            # Display the modified image
            cv2.imshow("Updated image",new_image)
            cv2.waitKey(0)  # Wait for key press to close
            cv2.destroyAllWindows()  # Close all image windows
        
else:
    # Error message if image file doesn't exist
    print("Image not found or inaccessible.")