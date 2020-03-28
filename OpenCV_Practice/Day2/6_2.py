import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('ml.png',0)
edges = cv2.Canny(img,0,200)


pic=np.hstack((img,edges))


cv2.imshow('dst',pic)
cv2.waitKey(0)