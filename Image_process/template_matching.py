# In this script I will be finding targeted object in the mario image

import cv2
import numpy as np

src_file = "../src/mario2.jpg"
target_file = "../src/coin2.jpg"

src_img = cv2.imread(src_file)
# search the target in the gray scale img
src_gray = cv2.cvtColor(src_img,cv2.COLOR_BGR2GRAY)
target_img = cv2.imread(target_file,0)
# get the size of the target
w,h = target_img[::-1].shape
# get the probability map on the src
res = cv2.matchTemplate(src_gray,target_img,cv2.TM_CCOEFF_NORMED)
probability_thresh = 0.85
# get all loc with higher probability
loc = np.where(res >= probability_thresh)
for pt in zip(*loc[::-1]):
    cv2.rectangle(src_img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)

cv2.imshow("src",src_img)
cv2.imshow("target",target_img)
cv2.waitKey(0)
cv2.destroyAllWindows()