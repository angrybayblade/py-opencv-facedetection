import numpy as np
import cv2
import os
global roi,l

roi = []

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

print ("Press Q To Exit \nAnd S To Save Face")

def vidCap():
    cap = cv2.VideoCapture(0)
    while 1:
        ret, img = cap.read()
        cv2.imshow('img',img)
        key = cv2.waitKey(1) & 0xff
        if key == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            return False
            
        
        elif key == ord('s'):
            cap.release()
            cv2.destroyAllWindows()
            detFace(img)
            return True
            
       
def detFace(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w-10,y+h-10),(255,0,0),2)
        roi_gray = gray[y:y+h-5, x:x+w-5]
        roi.append(roi_gray)


def saveFace():
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
            cv2.imwrite(file,cv2.resize(a,(80,80)))
           

while True:
    if vidCap():
        saveFace()
    else:
        break


  

