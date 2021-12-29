import cv2

def callback(x):
    global thresh1,thresh2,edge_img
    thresh1 = cv2.getTrackbarPos("max_val",winname)
    thresh2 = cv2.getTrackbarPos("min_val",winname)
    edge_img = cv2.Canny(sized_img,thresh1,thresh2)

src_file = "../src/brick.jpg"
img = cv2.imread(src_file,0)
sized_img = cv2.resize(img,None,fx=0.2,fy=0.2,interpolation=cv2.INTER_AREA)
thresh1,thresh2 = 150, 10
winname = "Canny"
cv2.namedWindow(winname,cv2.WINDOW_GUI_EXPANDED)
cv2.createTrackbar("max_val",winname, 0,255, callback)
cv2.createTrackbar("min_val",winname, 0,255, callback)
cv2.setTrackbarPos("max_val",winname,thresh1)
cv2.setTrackbarPos("min_val",winname,thresh2)


edge_img = cv2.Canny(sized_img,thresh1,thresh2)

while 1:
    cv2.imshow(winname, edge_img)

    k = cv2.waitKey(1)
    if k== ord('q'):
        break
cv2.destroyAllWindows()