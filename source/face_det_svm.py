import cv2
import numpy as np
global pt
import os
import cv2
from sklearn.svm import SVC
from pandas import DataFrame


print ("Press Q To Quit")
cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

temp_array = os.listdir("templates//")
temps = {a.replace('.png', ''): cv2.resize(cv2.imread('templates//{}'.format(a), 0), (80, 80)) for a in temp_array}
Temps = [[i] for i in temps]
for i in range(len(Temps)):
    Temps[i] = Temps[i]+temps[Temps[i][0]].reshape(1, 6400).tolist()[0]

df = DataFrame(Temps, columns=['face']+list(range(6400)))

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

svm = SVC()
svm.fit(df.drop(columns=['face']),df.face)


roi_gray = []

while True:
    gray = cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2GRAY)
    #cv2.rectangle(gray,pt,(pt[0]+w , pt[1]+h),(255,255,255),1)
    #cv2.putText(gray,t,(pt[0],pt[1]), font, 2, (255,255,255), 1, cv2.LINE_AA)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(gray,(x,y),(x+w-10,y+h-10),(255,0,0),2)
        print(svm.predict(cv2.resize(gray[y:y+h-5, x:x+w-5],(80,80)).reshape(1,6400)[0].reshape(1,-1))[0])

        
    cv2.imshow('',gray)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
        

cam.release()
cv2.destroyAllWindows()
