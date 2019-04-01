import numpy as np
import cv2
import os
global l

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
font = cv2.FONT_HERSHEY_SIMPLEX


cap = cv2.VideoCapture(0)
cap.set(3,1378)
cap.set(4,768)

save = False
saveCount = 0
saveName = ""

warning = False
warningText = ""
warningCount = 0

while 1:
    ret, gray = cap.read(0)
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    cv2.putText(gray,"Press q to exit",(30,30), font, 1, (255,255,255), 1, cv2.LINE_AA)
    cv2.imshow('img',gray)
    key = cv2.waitKey(1) & 0xff

    if not save:
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(gray,(x,y),(x+w-10,y+h-10),(255,0,0),2)

    if save:
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w-10,y+h-10),(255,0,0),2)
            roi_gray = gray[y:y+h-5, x:x+w-5]
            roi.append(roi_gray)

    if warning:
        if count < 100:
            cv2.putText(gray,"Press q to exit",(30,30), font, 1, (255,255,255), 1, cv2.LINE_AA)
            count += 1
        else:
            count = 0
            warning = False
        
    if key == ord('q'):
        break
    elif key == ord('s'):
        save = True
    
       
def detFace(img):
    roi = []
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w-10,y+h-10),(255,0,0),2)
        roi_gray = gray[y:y+h-5, x:x+w-5]
        roi.append(roi_gray)
    return roi

def saveFace(roi):
    for a in roi:
        cv2.imshow('',a)
        print ("Press Any Key To Exit Preview")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        name = input("Enter Name For The Face (Type None to ignore face) : ")
        if name == "None":
            print ("Face Ignored")
        else:
            file = os.path.join(os.getcwd(),"templates\\{}.png".format(name))
            print (file)
            cv2.imwrite(file,a)
           



cv2.destroyAllWindows()
cap.release()  

