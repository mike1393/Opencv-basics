# This program is allows one to track a specified color and a draw a contour around it
#1. Use the trackbar to specify hsv boundary and preview the mask on the res window
#2. Press s to apply the current mask and visualize the contour
#3. Press q to quit all windows
import cv2
import numpy as np

def callBack(x):
    global h_l, s_l, v_l, h_u,s_u, v_u
    h_l = cv2.getTrackbarPos("H_low", window_name)
    h_u = cv2.getTrackbarPos("H_upper", window_name)
    s_l = cv2.getTrackbarPos("S_low", window_name)
    s_u = cv2.getTrackbarPos("S_upper", window_name)
    v_l = cv2.getTrackbarPos("V_low", window_name)
    v_u = cv2.getTrackbarPos("V_upper", window_name)

src_file = "../src/ball.png"

src_img = cv2.imread(src_file)
sized_img = cv2.resize(src_img,None,fx=1,fy=1,interpolation=cv2.INTER_AREA)
org_img = np.copy(sized_img)
hsv_img = cv2.cvtColor(sized_img, cv2.COLOR_BGR2HSV)
window_name = "control"
cv2.namedWindow(window_name)
h_l, s_l, v_l, h_u,s_u, v_u = 0,0,0,180,255,255
cv2.createTrackbar("H_low", window_name, 0, 180, callBack)
cv2.setTrackbarPos("H_low", window_name,h_l)
cv2.createTrackbar("H_upper", window_name, 0, 180, callBack)
cv2.setTrackbarPos("H_upper", window_name,h_u)
cv2.createTrackbar("S_low", window_name, 0, 255, callBack)
cv2.setTrackbarPos("S_low", window_name,s_l)
cv2.createTrackbar("S_upper", window_name, 0, 255, callBack)
cv2.setTrackbarPos("S_upper", window_name,s_u)
cv2.createTrackbar("V_low", window_name, 0, 255, callBack)
cv2.setTrackbarPos("V_low", window_name,v_l)
cv2.createTrackbar("V_upper", window_name, 0, 255, callBack)
cv2.setTrackbarPos("V_upper", window_name,v_u)

res = cv2.bitwise_and(sized_img,sized_img)

while 1:
    lower = np.array([h_l,s_l,v_l])
    upper = np.array([h_u,s_u,v_u])
    mask = cv2.inRange(hsv_img, lower,upper)
    res = cv2.bitwise_and(sized_img,sized_img,mask=mask)
    # cv2.imshow("mask",mask)
    cv2.imshow("result",res)
    cv2.imshow("org",org_img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        cv2.destroyAllWindows()
        break
    # press 's' to exit
    elif k == ord('s'):
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnt = contours[0] if len(contours) ==2 else contours[1]
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.circle(org_img,(cx,cy),1,(0,255,0),-1)
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(org_img,[box],0,(0,255,0),2)
