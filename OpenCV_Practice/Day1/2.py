import numpy as np
import cv2 as cv

img=np.zeros((512,512,3),np.uint8)

cv.line(img,(10,10),(500,10),(255,0,0),10)
cv.line(img,(20,20),(500,20),(0,255,0),10)

cv.rectangle(img,(30,30),(100,100),(255,0,0),3)

cv.circle(img,(200,60),30,(0,0,255),3)

cv.ellipse(img,(150,300),(100,75),0,0,360,(0,255,0),-1)

font=cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'Computer Vision',(10,400),font,2,(255,255,255),2)
cv.imshow('d1',img)

cv.waitKey(0)

