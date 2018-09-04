import cv2
import numpy as np
import matplotlib.pyplot as plt

img  = cv2.imread('img1.png',cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
temp = cv2.imread('img2.png',0)

w,h = temp.shape[::-1]

res = cv2.matchTemplate(gray,temp,cv2.TM_CCOEFF_NORMED)
thres = 0.8

loc = np.where(res>=thres)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w , pt[1]+h),(255,255,255),2)
    
cv2.imshow('',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
