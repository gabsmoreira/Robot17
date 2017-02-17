
import numpy as np
import cv2


cap = cv2.VideoCapture(0)
h = 6.5*37.795672
f = 17.75
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cap.read()
    image =cv2.GaussianBlur(img,(5,5),10)
    #output = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,75)
    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)


    if lines is not None:
        for x1,y1,x2,y2 in lines[0]:
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
            #print(x1,y1,x2,y2)


    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            cv2.circle(img, (x, y), r, (0, 255, 0), 4)
            hpix = 2*r
            #print("Distancia em cm:",((f*h/hpix)))
        cv2.putText(img,str((f*h/hpix)),(200,100), font, 2,(255,255,255),2)


    cv2.imshow("output", img)
    #cv2.imshow("edges",edges)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
