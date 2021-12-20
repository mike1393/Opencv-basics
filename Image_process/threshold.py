import cv2
from matplotlib import pyplot as plt
import numpy as np
def callback(x):
    global thresh
    thresh = cv2.getTrackbarPos("threshold","control")
    
def threshold_img(src,thresh,flag=None):
    h = 40
    font = cv2.FONT_HERSHEY_SIMPLEX
    if flag == cv2.THRESH_BINARY:
        s = "THRESH_BINARY"
    elif flag == cv2.THRESH_BINARY_INV:
        s = "THRESH_BINARY_INV"
    elif flag == cv2.THRESH_TRUNC:
        s = "THRESH_TRUNC"
    elif flag == cv2.THRESH_TOZERO:
        s = "THRESH_TOZERO"
    elif flag == cv2.THRESH_TOZERO_INV:
        s = "THRESH_TOZERO_INV"
    else:
        s = "origin"
        thresh_img = src
        thresh_img[row-h:row,:col] = 0
        cv2.putText(thresh_img,s,(10,row-h//3),font,0.5,(255,255,255),1,cv2.LINE_AA)
        return thresh_img
        
    ret,thresh_img = cv2.threshold(src,thresh,255,flag)
    thresh_img[row-h:row,:col] = 0
    cv2.putText(thresh_img,s,(10,row-h//3),font,0.5,(255,255,255),1,cv2.LINE_AA)
    return thresh_img


src_img = "../src/pearl_earring.jpg"

org_img = cv2.imread(src_img,0)
sized_img = cv2.resize(org_img,None, fx=0.25,fy=0.25, interpolation=cv2.INTER_AREA)
row,col = sized_img.shape
cv2.namedWindow("control")

cv2.createTrackbar("threshold","control",0,255,callback)
thresh = 172
canvas = np.zeros((2*row,3*col),np.uint8)

while True:
    canvas[:row, :col] = threshold_img(sized_img,thresh)
    canvas[row:2*row, :col] = threshold_img(sized_img,thresh,cv2.THRESH_BINARY)
    canvas[:row, col:2*col] = threshold_img(sized_img,thresh,cv2.THRESH_BINARY_INV)
    canvas[row:2*row, col:2*col] = threshold_img(sized_img,thresh,cv2.THRESH_TRUNC)
    canvas[:row, 2*col:3*col] = threshold_img(sized_img,thresh,cv2.THRESH_TOZERO)
    canvas[row:2*row, 2*col:3*col] = threshold_img(sized_img,thresh,cv2.THRESH_TOZERO_INV)
    cv2.imshow("control",canvas)
    k = cv2.waitKey(1)
    if k == ord("q"):
        break
cv2.destroyAllWindows()