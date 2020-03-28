import numpy as np
import cv2 as cv
img=np.zeros((512,512,3))
img[1:100,1:100]=(0,255,0)

cv.imshow('image1',img)
cv.waitKey(0)

