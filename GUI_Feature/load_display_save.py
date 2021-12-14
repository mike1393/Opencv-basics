# This script opens a jpg file and saved the file as png
import cv2

filename = "../src/starry_night.jpg"
output_name = "../src/starry_night.png"
# read the file
img = cv2.imread(filename)
# if the file does not exist, exit the script
if img is None:
    print("No file exist")
    exit(0)
# Show the image
cv2.imshow(filename, img)
# listens to key input
k = cv2.waitKey(0)
# if s is pressed, save the image as png
if k == ord('s'):
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    cv2.imwrite(output_name,gray)
    print(f"Saved to {output_name}")
    # show the saved image
    img2 = cv2.imread(output_name)
    cv2.imshow(output_name, img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    cv2.destroyWindow(filename)


