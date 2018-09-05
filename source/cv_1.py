import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img1.png',1)

cv2.line(img,(0,0),(200,200),(0,0,0),3)
cv2.rectangle(img,(10,10),(210,210),(5,6,87),4)
cv2.circle(img,(100,100),50,(20,10,100),4)

pts = np.array([[100,90],[45,63],[14,67]],np.int32)

cv2.polylines(img,[pts],True,(1,2,3),1)


cv2.imshow('img 1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
