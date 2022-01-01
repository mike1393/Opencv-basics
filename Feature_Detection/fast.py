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


src_file = "../src/sudoku.jpg"
img = cv2.imread(src_file)
sized_img = cv2.resize(img,None,fx=0.3,fy=0.3,interpolation=cv2.INTER_AREA)
row,col,bgr = sized_img.shape
m = cv2.getRotationMatrix2D(((col-1)/2.0,(row-1)/2.0),90,1)

fast = cv2.FastFeatureDetector_create()
kp1 = fast.detect(sized_img,None)

img1 = cv2.drawKeypoints(sized_img, kp1, None, color=(255,0,0))

match_img = np.hstack((sized_img,img1))

cv2.imshow("fast",match_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
