import numpy as np
import cv2
faces=cv2.CascadeClassifier('cats.xml')
img=cv2.imread('cats.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

dfaces =faces.detectMultiScale(gray)
print(len(dfaces))
for (x,y,w,h) in dfaces:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('dst',img)
print(gray.shape)
cv2.waitKey(0)
