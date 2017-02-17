
import numpy as np
import cv2


cap = cv2.VideoCapture(0)
h = 6.5*37.795672
f = 17.75
font = cv2.FONT_HERSHEY_SIMPLEX
range_x = 10
range_y = 10

while True:
	ret, img = cap.read()
	image =cv2.GaussianBlur(img,(5,5),10)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)



	if circles is not None:
		circles = np.round(circles[0, :]).astype("int")
		range_x = np.arange(circles[0][0]-10,circles[0][0]+10,1)
		range_y = np.arange(circles[0][1]-10,circles[0][1]+10,1)
		for (x, y, r) in circles:
			for i in range (len(circles)):
				for j in range (len(circles[i])):
					if circles[i][1] in (range_y):
						posicao = "Horizontal"
					elif circles[i][0] in (range_x):
						posicao = "Vertical"
					else:
						posicao = "Diagonal"


			cv2.circle(img, (x, y), r, (0, 255, 0), 4)
			cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
			hpix = 2*r
			#print("Distancia em cm:",((f*h/hpix)))
		cv2.putText(img,str((f*h/hpix)),(100,100), font, 1,(255,255,255),2)
		cv2.putText(img,posicao,(650,450), font, 1,(0,0,255),2)


	cv2.imshow("output", img)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()
