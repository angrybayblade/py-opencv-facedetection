***This is an older version of script consider using new one**

# Before Running Scripts

Make Sure You Have Installed Numpy , Opencv and    Pyinstaller (For Compiling Scripts),If Not Run Following ..

```bash
pip3 install opencv-python
pip3 install numpy 
pip3 install pyinstaller
```

# Simple Face Training

    Use Face Training Module To Train Faces
    Run face_train in bin folder
    Press S and save the faces
    Press Q to quit
    
# Chek it out.

    Use Face Detection Scirpt To Check Your Trained Faces
    Run face_detect and voilah....

# Optimizing Algo.

```python
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
```
Change **thres** value accordingly, remember less thres faster detection but low acccuracy.

Also uncomment **cv2.rectangle(gray,pt,(pt[0]+w , pt[1]+h),(255,255,255),1)** to drar square around face.

Before Using Modules Compile Them Using Pyinstaller For Better Stability

                or

Use Them Without Compiling And Make Changes According To Your Need
