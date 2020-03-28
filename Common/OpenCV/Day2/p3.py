import numpy as np
import cv2 as cv
img=cv.imread('apple.jpg')
rows,cols,c=img.shape
M=cv.getRotationMatrix2D(((cols-1)/2,(rows-1)/2),45,0.5)
dst=cv.warpAffine(img,M,(cols,rows))
#dst=cv.resize(img,None,fx=2,fy=2,interpolation=cv.INTER_CUBIC)
print(rows,cols)
cv.imshow('img',img)
cv.waitKey(0)
cv.imshow('dst',dst)
cv.waitKey(0)

