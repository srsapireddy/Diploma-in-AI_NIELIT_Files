import cv2 as cv
img1=cv.imread('opencv-logo.png')
img2=cv.imread("ml.png")
img3=cv.addWeighted(img1,0.3,img2,0.7,0)
img3=cv.add(img1,img2)
cv.imshow('img1',img3)
cv.waitKey(0)
