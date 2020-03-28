
import cv2 as cv
img1=cv.imread('face.jpg')
print(img1.shape)
dst=cv.Canny(img1,0,100)
cv.imshow('face',img1)
cv.waitKey(0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()

