import cv2
import numpy as np
src_file = "../src/sudoku.jpg"
img = cv2.imread(src_file)
sized_img = cv2.resize(img,None, fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
img_gray = cv2.cvtColor(sized_img,cv2.COLOR_BGR2GRAY)
img_edge = cv2.Canny(img_gray,255,100)
lines = cv2.HoughLinesP(img_edge,1,np.pi/180,100,minLineLength=100,maxLineGap=10)


for line in lines:
    x1,y1,x2,y2 = line[0]
    print(line[0])
    cv2.line(sized_img,(x1,y1),(x2,y2),(0,255,0),4)

cv2.imshow("edge",sized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
