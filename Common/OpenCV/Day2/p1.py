import numpy as np
import cv2 as cv
img=cv.imread('messi.jpg')
M=np.float32([[1,0,100],[0,1,50]])
rows,cols,c=img.shape
dst=cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',img)
cv.waitKey(0)
cv.imshow('dst',dst)
cv.waitKey(0)

