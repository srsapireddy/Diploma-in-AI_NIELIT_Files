import numpy as np
import cv2 as cv
img = cv.imread('messi.jpg')
res = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)
#OR
res = cv.resize(img,None,fx=2, fy=2)
#height, width = img.shape[:2]
#res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)

cv.imshow('img',res)
cv.waitKey(0)
