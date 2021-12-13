# This script captures the camera input and records the video
import cv2

output = "output.avi"
# Create a video capture to capture the camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Camera not found")
    exit(0)
# Get the video spec
width, height, fps = cap.get(cv2.CAP_PROP_FRAME_WIDTH),cap.get(cv2.CAP_PROP_FRAME_HEIGHT),cap.get(cv2.CAP_PROP_FPS)
# Specify the video codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# Create the Videowriter from codec and video spec
out = cv2.VideoWriter(output,fourcc,int(fps),(int(width),int(height)))
start_record =False

while True:
    ret, frame = cap.read()
    if not ret:
        print("No video stream")
        break
    # Pre process the video input by flipping the video
    frame = cv2.flip(frame,1)
    cv2.imshow('frame', frame)
    # if the record flag is true, start record the video
    if start_record:
        out.write(frame)
    # Listens to keyboard input
    k = cv2.waitKey(1)
    # if q is pressed, release the video capture and video write, then exit the script
    if k == ord('q'):
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        break
    # if s is pressed, set the record flag to True
    elif k == ord('s'):
        print("start recording")
        start_record = True

