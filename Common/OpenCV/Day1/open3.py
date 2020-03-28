import cv2 as cv
img=cv.imread('walking.jpg')
print(img)
img2=cv.bitwise_not(img)
print(img.shape)
cv.imshow('img1',img2)
cv.imwrite('w2.png',img2)
cv.waitKey(0)
