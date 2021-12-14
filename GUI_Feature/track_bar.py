import cv2
import numpy as np

# Create a black image, a window
image_size = (512,512,3)
window_name = "image"
img = np.zeros(image_size, np.uint8)
cv2.namedWindow(window_name)
# create trackbars for color change
def nothing(x):
    pass
cv2.createTrackbar("R", window_name, 0,255,nothing)
cv2.createTrackbar("G", window_name, 0,255,nothing)
cv2.createTrackbar("B", window_name, 0,255,nothing)

while True:
    cv2.imshow(window_name, img)
    r = cv2.getTrackbarPos("R", window_name)
    g = cv2.getTrackbarPos("G", window_name)
    b = cv2.getTrackbarPos("B", window_name)
    img[:] = [r,g,b]
    k = cv2.waitKey(1)
    if k == ord('q'):
        cv2.destroyAllWindows()
        break