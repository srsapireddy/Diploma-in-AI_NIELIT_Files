import numpy as np
import cv2 as cv
img=cv.imread('cat1.jpg')

res=cv.resize(img,None,fx=2,fy=2,interpolation=cv.INTER_CUBIC)

cv.imshow('img1',img)
cv.waitKey(0)
cv.imshow('img1',res)

cv.waitKey(0)
