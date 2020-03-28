import numpy as np
import cv2 as cv
img=np.zeros((512,512,3))

cv.line(img,(0,0),(511,511),(255,0,0),5)
cv.rectangle(img,(200,60),(510,128),(0,255,0),3)
cv.circle(img,(200,60),20,(0,0,255),-1)
cv.ellipse(img,(250,250),(100,50),0,0,360,255,3)

font=cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,400),font,4,(255,255,255),2)
cv.imshow('im',img)
cv.waitKey(0)


