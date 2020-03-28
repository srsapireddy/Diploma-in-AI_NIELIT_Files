import numpy as np
import cv2 as cv

img=np.zeros((512,512,3),np.uint8)
cv.line(img,(0,0),(200,250),(255,255,0),5)
cv.rectangle(img,(100,100),(200,200),(0,255,255),3)
cv.circle(img,(300,300),50,(0,255,255),-1)
cv.ellipse(img,(350,100),(100,50),0,30,320,(0,255,255))
font=cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'Computer Vision',(10,500),font,2,(255,0,255),2)
cv.imshow('img1',img)
cv.waitKey(0)
