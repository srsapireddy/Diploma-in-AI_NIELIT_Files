import cv2
import numpy as np

img = cv2.imread('chessboard.png',0)
kernel = np.ones((2,2),np.uint8)
erosion = cv2.erode(img,kernel)
dilation = cv2.dilate(img,kernel)
img=np.hstack((erosion,dilation))
cv2.imshow('dst',img)
cv2.waitKey(0)