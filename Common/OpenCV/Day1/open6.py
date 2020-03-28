import cv2 as cv
img=cv.imread('messi.jpg')
ball=img[280:340,330:390]
print(ball.shape)
img[273:333,100:160]=ball
cv.imshow('img1',img)
cv.waitKey(0)
