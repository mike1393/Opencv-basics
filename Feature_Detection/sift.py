import cv2
import numpy as np

def bruteForceMatcher(des1,des2,thresh):
    # BFMatcher with default params
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2,k=2)
    # Apply ratio test
    good = []
    for m,n in matches:
        if m.distance < thresh*n.distance:
            good.append([m])
    return good


src_file = "../src/pearl_earring.jpg"
img = cv2.imread(src_file)
sized_img = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
row,col,bgr = sized_img.shape
m = cv2.getRotationMatrix2D(((col-1)/2.0,(row-1)/2.0),90,1)
rot_img = cv2.warpAffine(sized_img,m,(col,row))

sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(sized_img,None)
kp2, des2 = sift.detectAndCompute(rot_img,None)

good = bruteForceMatcher(des1,des2,0.75)
match_img = cv2.drawMatchesKnn(sized_img,kp1,rot_img,kp2,good,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv2.imshow("sift",match_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
