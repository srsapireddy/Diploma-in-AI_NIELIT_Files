import numpy as np
import cv2 as cv
img=cv.imread('apple.jpg')
M=np.float32([[1,0,200],[0,1,100]])
rows,cols,c=img.shape
dst=cv.warpAffine(img,M,(cols,rows))
cv.imshow('dst',dst)
cv.waitKey(0)

