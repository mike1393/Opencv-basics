import cv2
import numpy as np

def callback(x):
    global ksize, winname,canvas
    ksize = cv2.getTrackbarPos("kernal size",winname)
    if ksize %2 ==0:
        ksize = int(ksize)+1
        cv2.setTrackbarPos("kernal size",winname,ksize)
    canvas[:, :col] = sized_img
    canvas[:, col:2*col] = cv2.Laplacian(sized_img, cv2.CV_64F)
    canvas[:, 2*col:3*col] = cv2.Sobel(sized_img, cv2.CV_64F,dx,dy,ksize=ksize)
    canvas[:, 3*col:4*col] = cv2.Scharr(sized_img, cv2.CV_64F,dx,dy)



src_img = "../src/brick.jpg"
winname = "gradient"
img = cv2.imread(src_img,0)
sized_img = cv2.resize(img,None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
row, col = sized_img.shape
canvas = np.zeros((row,col*4),np.uint8)
cv2.namedWindow(winname)
dx,dy,ksize = 0,1,3
canvas[:, :col] = sized_img
canvas[:, col:2*col] = cv2.Laplacian(sized_img, cv2.CV_64F)
canvas[:, 2*col:3*col] = cv2.Sobel(sized_img, cv2.CV_64F,dx,dy,ksize=ksize)
canvas[:, 3*col:4*col] = cv2.Scharr(sized_img, cv2.CV_64F,dx,dy)
cv2.createTrackbar("kernal size", winname, 0, 10, callback)
cv2.setTrackbarPos("kernal size",winname,ksize)

    
while 1:
    cv2.imshow(winname, canvas)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    elif k == ord('x'):
        dx,dy = dy,dx
        canvas[:, :col] = sized_img
        canvas[:, col:2*col] = cv2.Laplacian(sized_img, cv2.CV_64F)
        canvas[:, 2*col:3*col] = cv2.Sobel(sized_img, cv2.CV_64F,dx,dy,ksize=ksize)
        canvas[:, 3*col:4*col] = cv2.Scharr(sized_img, cv2.CV_64F,dx,dy)

cv2.destroyAllWindows()