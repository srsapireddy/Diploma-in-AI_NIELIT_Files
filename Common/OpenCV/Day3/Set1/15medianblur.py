import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('face.jpg')

blur = cv2.blur(img,(5,5))
#cv2.imshow('dst',blur)
#cv2.waitKey(0)
blur2 = cv2.GaussianBlur(img,(5,5),0)

median=cv2.medianBlur(img,5)
#blur = cv2.bilateralFilter(img,9,75,75)



h=np.hstack((img,blur,blur2,median))
cv2.imshow('dst',h)
cv2.waitKey(0)
