import numpy as np
import cv2
cars=cv2.CascadeClassifier('cars.xml')
img=cv2.imread('car.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

dcars =cars.detectMultiScale(gray)
print(len(dcars))
for (x,y,w,h) in dcars:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('dst',img)
print(gray.shape)
cv2.waitKey(0)
