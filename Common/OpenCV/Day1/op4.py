import cv2 as cv

img =cv.imread("messi.jpg")
print(img)
ball=img[280:340,330:390]

img[273:333,100:160]=ball
cv.imshow('image',img)
cv.waitKey(0)

