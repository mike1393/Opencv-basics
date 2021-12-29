# In this script I will perform histograms equalizations to a gray scale image

import cv2
import numpy as np
from matplotlib import pyplot as plt

src_file = "../src/corgy1.jpg"
src_img = cv2.imread(src_file,0)
sized_img = cv2.resize(src_img,None, fx=0.2,fy=0.2,interpolation=cv2.INTER_AREA)
# global histogram equalization
equ_img = cv2.equalizeHist(sized_img)
# adaptive histogram equalization
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
adaptive_hist_img = clahe.apply(sized_img)

hist_org = cv2.calcHist([sized_img],[0],None,[256],[0,256])
hist_equ = cv2.calcHist([equ_img],[0],None,[256],[0,256])
adaptive_hist = cv2.calcHist([adaptive_hist_img],[0],None,[256],[0,256])

plt.subplot(321), plt.imshow(sized_img, 'gray')
plt.subplot(322), plt.plot(hist_org)
plt.subplot(323), plt.imshow(equ_img, 'gray')
plt.subplot(324), plt.plot(hist_equ)
plt.subplot(325), plt.imshow(adaptive_hist_img, 'gray')
plt.subplot(326), plt.plot(adaptive_hist)
plt.show()
