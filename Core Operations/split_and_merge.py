# This script demonstrates how to split channels from a source image
import cv2
src_img = "../src/starry_night.jpg"

img = cv2.imread(src_img)
hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv_img)

cv2.imshow("src", img)
hsv_img = cv2.merge((h,s,v))
cv2.imshow("hsv", hsv_img)
k = cv2.waitKey(0)
if k == ord("q"):
    cv2.imshow("h", h)
    cv2.imshow("s", s)
    cv2.imshow("v", v)
    cv2.waitKey(0)
cv2.destroyAllWindows()