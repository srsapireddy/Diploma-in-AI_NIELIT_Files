import cv2 as cv
import numpy as np
img=np.zeros([512,512,3])
img[0:150,0:150]=(0,255,0)
print(img)
print(img.shape)
cv.imshow('img1',img)
cv.waitKey(0)


