import os
import cv2

path = input("Enter the path of the image: ")
path = path.strip('"').strip("'")

if os.path.exists(path):
    image = cv2.imread(path)

    if image is not None:
        grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print("Image is successfully converted to grayscale.")

        response = input("Do you want to save the grey image? or want to see it (yes/no): ")

        if response.lower() == "yes":
            save_dir = input("Enter the folder path where you want to save the grey image: ")
            save_dir = save_dir.strip('"').strip("'")

            if os.path.exists(save_dir):
                save_path = os.path.join(save_dir, "grey_image.jpg")
                success = cv2.imwrite(save_path, grey_image)

                if success:
                    print(f"Grey image saved successfully at:\n{save_path}")
                else:
                    print("Failed to save grey image.")
            else:
                print("Save directory does not exist.")

        else:
            cv2.imshow("Grey Image", grey_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    else:
        print("Failed to load the image.")

else:
    print(f"Path does not exist: {path}")
    
# work is complete!!
