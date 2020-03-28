import cv2
img1=cv2.imread('ml.png')
img2=cv2.imread('opencv-logo.png')
print(img1.shape)
print(img2.shape)
dst=cv2.addWeighted(img1,0.7,img2,0.3,1)

#dst=cv2.bitwise_or(img1,img2)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

