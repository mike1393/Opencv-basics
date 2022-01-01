import cv2

def detectAndDisplay(img,cl):
    # convert to gray
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # smoothen lighting exposure
    # img_gray = cv2.equalizeHist(img_gray)
    img_gray = cl.apply(img_gray)

    #-- Detect faces
    faces = face_cascades.detectMultiScale(img_gray,1.3,5)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        # obtain the face region of interest
        faceROI = img_gray[y:y+h,x:x+w]
        #-- In each face, detect eyes
        eyes = eyes_cascades.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            img = cv2.circle(img, eye_center, radius, (255, 0, 0 ), 2)
    cv2.imshow('Capture - Face detection', img)

# create cascade classifier w/training file
face_haarcascades =  "../src/Haarcascades/haarcascade_frontalface_default.xml"
eyes_haarcascades = "../src/Haarcascades/haarcascade_eye.xml"
face_cascades = cv2.CascadeClassifier(face_haarcascades)
eyes_cascades = cv2.CascadeClassifier(eyes_haarcascades)
# if not face_cascades:
#     print('--(!)Error loading face cascade')
#     exit(0)
# if not eyes_cascades:
#     print('--(!)Error loading eyes cascade')
#     exit(0)
#open camera
cap = cv2.VideoCapture(0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)
    
# detect face/eye fram by frame
while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    detectAndDisplay(frame,clahe)
    if cv2.waitKey(10) == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
