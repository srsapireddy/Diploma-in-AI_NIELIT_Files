import cv2
import numpy as np

A = cv2.imread('apple.jpg')
G = A.copy()

for i in range(3):
    G = cv2.pyrUp(G)
    cv2.imshow('d1',G)
    cv2.waitKey(0)



