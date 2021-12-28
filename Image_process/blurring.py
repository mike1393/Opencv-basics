# This script compares multiple blurring method
# Use the trackbar to change the kernal size for blurring box
# s_color and s_space is used to adjust sigma color and sigma space for Bilaternal Filtering
import cv2
import numpy as np
def callback(x):
    global kernal_size, s_color, s_space, canvas
    # updates the trackbar values
    kernal_size = cv2.getTrackbarPos("kernal_size","control")
    if int(kernal_size) %2 ==0:
        kernal_size=int(kernal_size)+1
        cv2.setTrackbarPos("kernal_size","control",kernal_size)
    s_color = cv2.getTrackbarPos("s_color","control")
    s_space = cv2.getTrackbarPos("s_space","control")
    # rerender the image
    canvas[:row, :col,:] = blurr_img(sized_img,kernal_size,"Average")
    canvas[row:2*row, :col,:] = blurr_img(sized_img,kernal_size,"Gaussian Blurring")
    canvas[:row, col:2*col,:] = blurr_img(sized_img,kernal_size,"Median Blurring")
    canvas[row:2*row, col:2*col,:] = blurr_img(sized_img,kernal_size,"Bilateral Filtering",s_color, s_space)
    canvas[:2*row, 2*col:4*col,:] = blurr_img(sized_img2,kernal_size,"Origin")
    
def blurr_img(src,kernal_size,flag=None,s_color = None, s_space = None):
    # create the new image with a description text beneath it
    h = 40
    font = cv2.FONT_HERSHEY_SIMPLEX
    if flag == "Origin":
        blurr_img = src
        blurr_img[2*row-h:2*row,:2*col] = 0
        cv2.putText(blurr_img,flag,(10,2*row-h//3),font,0.5,(255,255,255),1,cv2.LINE_AA)
        return blurr_img
    elif flag == "Average":
        blurr_img = cv2.blur(src,(kernal_size,kernal_size))
    elif flag == "Gaussian Blurring":
        blurr_img = cv2.GaussianBlur(src,(kernal_size,kernal_size),0)
    elif flag == "Median Blurring":
        blurr_img = cv2.medianBlur(src,kernal_size)
    else:
        blurr_img = cv2.bilateralFilter(src,kernal_size,s_color,s_space)
    
    blurr_img[row-h:row,:col] = 0
    cv2.putText(blurr_img,flag,(10,row-h//3),font,0.5,(255,255,255),1,cv2.LINE_AA)
    return blurr_img

    

src_img = "../src/pearl_earring.jpg"

org_img = cv2.imread(src_img)
sized_img = cv2.resize(org_img,None, fx=0.25,fy=0.25, interpolation=cv2.INTER_AREA)
sized_img2 = cv2.resize(org_img,None, fx=0.5,fy=0.5, interpolation=cv2.INTER_AREA)
print(sized_img.shape)
row,col,bgr = sized_img.shape
cv2.namedWindow("control")
canvas = np.zeros((2*row,4*col,bgr),np.uint8)
kernal_size, s_color, s_space = 5, 75, 75
cv2.createTrackbar("kernal_size","control",0,10,callback)
cv2.createTrackbar("s_color","control",0,180,callback)
cv2.createTrackbar("s_space","control",0,180,callback)
cv2.setTrackbarPos("kernal_size","control",kernal_size)
cv2.setTrackbarPos("s_color","control",s_color)
cv2.setTrackbarPos("s_space","control",s_space)

canvas[:row, :col,:] = blurr_img(sized_img,kernal_size,"Average")
canvas[row:2*row, :col,:] = blurr_img(sized_img,kernal_size,"Gaussian Blurring")
canvas[:row, col:2*col,:] = blurr_img(sized_img,kernal_size,"Median Blurring")
canvas[row:2*row, col:2*col,:] = blurr_img(sized_img,kernal_size,"Bilateral Filtering",s_color, s_space)
canvas[:2*row, 2*col:4*col,:] = blurr_img(sized_img2,kernal_size,"Origin")

while True:
    cv2.imshow("control",canvas)
    k = cv2.waitKey(1)
    if k == ord("q"):
        break
cv2.destroyAllWindows()