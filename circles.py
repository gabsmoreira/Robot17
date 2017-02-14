
import numpy as np
import cv2
 

cap = cv2.VideoCapture(0)
h = 6.5*37.795672
f = 17.75

while True:
	ret, img = cap.read()
	image =cv2.GaussianBlur(img,(5,5),0)
	output = image.copy()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



	circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
	 
	if circles is not None:
		circles = np.round(circles[0, :]).astype("int")
	 
		for (x, y, r) in circles:
			cv2.circle(img, (x, y), r, (0, 255, 0), 4)
			hpix = 2*r
			print("Distância em cm:",((f*h/hpix))) 


	cv2.imshow("output", img)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()

