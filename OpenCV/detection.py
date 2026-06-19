
import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)
smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_smile.xml'
)

cap=cv2.VideoCapture(0)
while True:
    ret, img=cap.read()
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray, 1.1 , 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h, x:x+w]
        roi_color=img[y:y+h, x:x+w]
        eye=eye_cascade.detectMultiScale(roi_gray,1.1,10)
        if len(eye)>0:
            cv2.putText(img, "Eyes Detected", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)

        smile=smile_cascade.detectMultiScale(roi_gray,1.1,10)
        if len(smile)>0:
            cv2.putText(img, "Smile Detected", (x,y-25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)

    cv2.imshow('img',img)
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()