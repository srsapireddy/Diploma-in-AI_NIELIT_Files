import numpy as np
import cv2
img=cv2.imread('walking.jpg')
print img.shape
cv2.imshow('image',img)
k=cv2.waitKey(0)


