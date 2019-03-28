import numpy as np
import cv2
import os
global l

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def saveTemplate(img,name):
    roi = []
    print (img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w-10,y+h-10),(255,0,0),2)
        roi_gray = gray[y:y+h-5, x:x+w-5]
        roi.append(roi_gray)
        
    for a in roi:
        file = os.path.join(os.getcwd(),"templates\\{}.png".format(name))
        #print (file)
        cv2.imwrite(file,a)
            
face_temps = os.listdir("faces//")
faces = {}
for face in face_temps:
    img = cv2.imread('faces//{}'.format(face))
    name = " ".join([i for i in face.split(".") if i not in ['jpg','png','jpeg']])
    faces.update({name:img})

for face in faces:
    saveTemplate(faces[face],face)
