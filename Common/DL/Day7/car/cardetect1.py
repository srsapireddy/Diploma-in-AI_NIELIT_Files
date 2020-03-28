import numpy as np
import cv2
print(cv2.__version__)
vcap = cv2.VideoCapture('Car.mp4')
result=vcap.isOpened()
print(result)
cars = cv2.CascadeClassifier('cars.xml')
while(True):
	ret, frame = vcap.read()
	print(ret)
	if frame is not None:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		dcars = cars.detectMultiScale(gray, 1.3, 5)
		for (x,y,w,h) in dcars:
	    		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		cv2.imshow('frame',frame)
		if cv2.waitKey(22) & 0xFF == ord('q'):
			break
	else:
        	print ("Frame is None")
        	break

# When everything done, release the capture
vcap.release()
cv2.destroyAllWindows()
print("Video stop")

