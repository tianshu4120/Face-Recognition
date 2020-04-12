import numpy as np
import cv2
faceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0) 
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
        gray, 
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20)
        )
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
	    
        cv2.imshow('gray',frame)
       # cv2.imshow('My Camera',frame)
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
    else:
        break
out.release()
cap.release()
cv2.destroyAllWindows()

