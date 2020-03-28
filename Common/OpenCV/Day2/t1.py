import numpy as np
import cv2 as cv
img=cv.imread('cat1.jpg',0)
rows,cols=img.shape
M=np.float32([[1.2,0,0],[0,1.2,0]])
dst=cv.warpAffine(img,M,(cols,rows))
cv.imshow('img1',img)
cv.waitKey(0)
cv.imshow('img2',dst)
cv.waitKey(0)

