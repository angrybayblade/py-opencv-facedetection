import cv2
import numpy as np
global pt
import os

print ("Press Q To Quit")
cam = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX

temp_array = os.listdir("templates//")

temps = {a.replace('.png',''):cv2.imread('templates//{}'.format(a),0) for a in temp_array}

while True:
    gray = cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2GRAY)
    for t in temps:
        w,h = temps[t].shape[::-1]
        res = cv2.matchTemplate(gray,temps[t],cv2.TM_CCOEFF_NORMED)
        thres = 0.7

        loc = np.where(res>=thres)
        try:
            pt = max(list(zip(*loc[::-1]))[:-10])
            #cv2.rectangle(gray,pt,(pt[0]+w , pt[1]+h),(255,255,255),1)
            cv2.putText(gray,t,(pt[0],pt[1]), font, 2, (255,255,255), 1, cv2.LINE_AA)
        except:
            pass
    
    cv2.imshow('',gray)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
        

cam.release()
cv2.destroyAllWindows()
