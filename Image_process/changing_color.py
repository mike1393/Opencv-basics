import cv2

filename = "../src/pearl_earring.jpg"
img = cv2.imread(filename)
if img is None:
    print("No file exist")
    exit(0)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow("gray",img_gray)
cv2.imshow("hsv",img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()