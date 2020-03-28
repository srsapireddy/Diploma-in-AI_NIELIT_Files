import  cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('building2.jpg',0)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=1)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=1)

dst= np.hstack((sobelx,sobely))

cv2.imshow('dsti1',img)

cv2.waitKey(0)

cv2.imshow('dst',dst)
cv2.waitKey(0)


