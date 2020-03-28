import numpy as np
import cv2 as cv
img=cv.imread('apple.jpg')
rows,cols,col=img.shape
M=cv.getRotationMatrix2D(((cols-1)/2,(rows-1)/2),90,0.5)
print(M)

dst=cv.warpAffine(img,M,(cols,rows))
cv.imshow('img1',img)
cv.waitKey(0)
cv.imshow('img2',dst)
cv.waitKey(0)

