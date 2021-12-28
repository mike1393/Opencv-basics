# This program is a modification of color_tracking.py
#1. Use the trackbar to specify hsv boundary and preview the mask on the mask window
#2. Press s to add and apply the current mask to the result window
#3. Press q to quit all windows
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# Create windows for trackbar
window_name = "control"
cv2.namedWindow(window_name,cv2.WINDOW_GUI_EXPANDED)
# Update variables with trackbar values
def callBack(x):
    global h_l, s_l, v_l, h_u,s_u, v_u
    h_l = cv2.getTrackbarPos("H_low", window_name)
    h_u = cv2.getTrackbarPos("H_upper", window_name)
    s_l = cv2.getTrackbarPos("S_low", window_name)
    s_u = cv2.getTrackbarPos("S_upper", window_name)
    v_l = cv2.getTrackbarPos("V_low", window_name)
    v_u = cv2.getTrackbarPos("V_upper", window_name)

# create trackbars for hsv value
h_l, s_l, v_l, h_u,s_u, v_u = 0,0,0,180,255,255
cv2.createTrackbar("H_low", window_name, 0, 180, callBack)
cv2.createTrackbar("H_upper", window_name, 0, 180, callBack)
cv2.createTrackbar("S_low", window_name, 0, 255, callBack)
cv2.createTrackbar("S_upper", window_name, 0, 255, callBack)
cv2.createTrackbar("V_low", window_name, 0, 255, callBack)
cv2.createTrackbar("V_upper", window_name, 0, 255, callBack)

cv2.setTrackbarPos("H_low", window_name,h_l)
cv2.setTrackbarPos("S_low", window_name,s_l)
cv2.setTrackbarPos("V_low", window_name,v_l)
cv2.setTrackbarPos("H_upper", window_name,h_u)
cv2.setTrackbarPos("S_upper", window_name,s_u)
cv2.setTrackbarPos("V_upper", window_name,v_u)
# create a list to store current saved mask
masks = []
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
    # if there are no mask saved
    if len(masks) == 0:
        res = cv2.bitwise_and(frame,frame,mask=mask)
    else:
        # loop over saved mask, and perform bitwise or on top of each mask
        for i,pack in enumerate(masks):
            m = cv2.inRange(frame_hsv,pack[0],pack[1])
            if i!=0:
                new_m = cv2.bitwise_or(new_m,m)
            else:
                new_m = m
        cv2.imshow("mask_new",new_m)
        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame,frame,mask=new_m)
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
    # press 's' to exit
    elif k == ord('s'):
        masks.append((lower,upper))
        print(f"lower: {lower}")
        print(f"upper: {upper}")
