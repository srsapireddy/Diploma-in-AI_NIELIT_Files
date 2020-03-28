import cv2 as cv

img =cv.imread("walking.jpg")
print(img)

img=cv.bitwise_not(img)
#cv.imshow('image',img)
#cv.waitKey(0)
cv.imwrite('invertedwalk.jpg',img)
