
import cv2 as cv
img1=cv.imread('ml.png')
img2=cv.imread('opencv-logo.png')
print(img1.shape)
print(img2.shape)
dst=cv.addWeighted(img1,0.7,img2,0.3,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()

