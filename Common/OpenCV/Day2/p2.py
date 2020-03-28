import numpy as np
import cv2 as cv
img=cv.imread('messi.jpg',0)
M=np.float32([[2,0,0],[0,2,0]])
rows,cols=img.shape

#dst=cv.warpAffine(img,M,(cols,rows))
#dst=cv.resize(img,None,fx=2,fy=2,interpolation=cv.INTER_CUBIC)
print(rows,cols)
dst=img.resize(342,548)
cv.imshow('img',img)
cv.waitKey(0)
cv.imshow('dst',dst)
cv.waitKey(0)

