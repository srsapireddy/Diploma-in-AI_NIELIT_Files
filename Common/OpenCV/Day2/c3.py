import numpy as np
import cv2 as cv
img=cv.imread('face.jpg',0)
dst=cv.Canny(img,0,100)
dst1=cv.Canny(img,100,200)

pic=np.hstack((img,dst,dst1))

cv.imshow('img2',pic)
cv.waitKey(0)

