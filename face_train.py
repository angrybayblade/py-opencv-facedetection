import numpy as np
import cv2
import os

face_cascade = cv2.CascadeClassifier("C:\opencv\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml")
file = os.path.join(os.getcwd(),"templates\\temp.png")
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w-10,y+h-10),(255,0,0),2)
        roi_gray = gray[y:y+h-5, x:x+w-5]       

    cv2.imshow('img',img)
    key = cv2.waitKey(1) & 0xff
    if key == ord('q'):
        break
    
    elif key == ord('s'):
        cv2.imwrite(file,roi_gray)
        print ("Face Saved")
       
cap.release()
cv2.destroyAllWindows()
