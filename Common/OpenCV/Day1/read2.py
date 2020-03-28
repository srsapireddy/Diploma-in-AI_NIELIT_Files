import numpy as np
import cv2
img=cv2.imread('walking.jpg')

cv2.imshow('dst',img)
cv2.imwrite('m22.png',img)
#print(img)
#print(img.shape)
#cv2.imshow('image',img)
from matplotlib import pyplot as plt
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.xticks([]),plt.yticks([])
plt.show()
'''
k=cv2.waitKey(0)
cv2.destroyAllWindows()
'''
