import cv2
import numpy as np

cam = cv2.VideoCapture(0)
temp = cv2.imread('temp.png',0)

while True:
    gray = cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2GRAY)
    w,h = temp.shape[::-1]
    res = cv2.matchTemplate(gray,temp,cv2.TM_CCOEFF_NORMED)
    thres = 0.7

    loc = np.where(res>=thres)

    for pt in list(zip(*loc[::-1]))[:-5]:
        cv2.rectangle(gray,pt,(pt[0]+w , pt[1]+h),(255,255,255),2)
    cv2.imshow('',gray)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
        

cam.release()
cv2.destroyAllWindows()
