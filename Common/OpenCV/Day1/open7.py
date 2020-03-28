import cv2 as cv
img1=cv.imread('apple.jpg')
print(img1.shape)
img2=cv.imread("orange.jpg")
print(img2.shape)
img3=cv.addWeighted(img1,0.5,img2,0.5,0)
img3=cv.add(img1,img2)
cv.imshow('img1',img3)
cv.waitKey(0)
