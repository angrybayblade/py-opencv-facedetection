import cv2
import numpy as np
global pt
import os

print ("Press Q To Quit")
cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

temp_array = os.listdir("templates//")

temps = {a.replace('.png',''):cv2.imread('templates//{}'.format(a),0) for a in temp_array}
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


while True:
    gray = cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(gray,(x,y),(x+w-10,y+h-10),(255,0,0),2)
        face = cv2.resize(gray[y:y+h-5, x:x+w-5],(80,80))
        
        for t in temps:
            w,h = temps[t].shape[::-1]
            res = cv2.matchTemplate(face,temps[t],cv2.TM_CCOEFF_NORMED)
            thres = 0.7
            loc = np.where(res>=thres)
            try:
                pt = max(list(zip(*loc[::-1]))[:-10])
                cv2.putText(gray,t,(x,y), font, 2, (255,255,255), 1, cv2.LINE_AA)
            except:
                pass
    
    cv2.imshow('',gray)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
        

cam.release()
cv2.destroyAllWindows()
