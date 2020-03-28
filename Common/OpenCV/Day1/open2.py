import cv2 as cv
img=cv.imread('walking.jpg',0)
cv.imshow('img1',img)
print(img)

print(img.shape)
cv.waitKey(0)

