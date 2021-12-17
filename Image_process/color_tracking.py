# This program tracks object by specifying hsv values
#1. Use the trackbar to specify hsv boundary
#2. Press s to print current boundary
#3. Press q to quit
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# Create a window for trackbars
window_name = "control"
cv2.namedWindow(window_name,cv2.WINDOW_GUI_EXPANDED)

# the call back function for trackbar, update variables with trackbar position
def callBack(x):
    global h_l, s_l, v_l, h_u,s_u, v_u
    h_l = cv2.getTrackbarPos("H_low", window_name)
    h_u = cv2.getTrackbarPos("H_upper", window_name)
    s_l = cv2.getTrackbarPos("S_low", window_name)
    s_u = cv2.getTrackbarPos("S_upper", window_name)
    v_l = cv2.getTrackbarPos("V_low", window_name)
    v_u = cv2.getTrackbarPos("V_upper", window_name)
# Create trackbars for boundaries of hsv
cv2.createTrackbar("H_low", window_name, 0, 180, callBack)
cv2.createTrackbar("H_upper", window_name, 0, 180, callBack)
cv2.createTrackbar("S_low", window_name, 0, 255, callBack)
cv2.createTrackbar("S_upper", window_name, 0, 255, callBack)
cv2.createTrackbar("V_low", window_name, 0, 255, callBack)
cv2.createTrackbar("V_upper", window_name, 0, 255, callBack)

h_l, s_l, v_l, h_u,s_u, v_u = 0,0,0,180,255,255
while True:
    # Take each frame
    ret, frame = cap.read()
    if not ret:
        print("no stream")
    # Convert BGR to HSV
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower = np.array([h_l,s_l,v_l])
    upper = np.array([h_u,s_u,v_u])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(frame_hsv, lower,upper)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame,mask=mask)
    # show the origin, masked, result
    cv2.imshow("origin",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",res)

    k = cv2.waitKey(1)
    # press 'q' to exit
    if k == ord('q'):
        cv2.destroyAllWindows()
        cap.release()
        break
    # press 's' to print current info
    elif k == ord('s'):
        print(f"lower: {lower}")
        print(f"upper: {upper}")
