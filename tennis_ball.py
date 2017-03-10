
import numpy as np
import cv2
import cv2.cv as cv

import rospy

from geometry_msgs.msg import Twist

import sys, select, termios, tty


def check_tennis_ball(camera):
	
	lower_green = np.array([25,60,100])
	upper_green = np.array([100,255,255])
	ret, img = camera.read()
	blur =cv2.GaussianBlur(img,(5,5),10)
	gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
	hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, lower_green, upper_green)
	mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
	circles = cv2.HoughCircles(gray, cv.CV_HOUGH_GRADIENT, 1.4, 100)


	if circles is not None:
		circles = np.round(circles[0, :]).astype("int")
		for (x, y, r) in circles:
			if mask_rgb[y][x][0] == 255:
				if mask_rgb[y][x][1] == 255:
					if mask_rgb[y][x][2] == 255:
						cv2.circle(img, (x, y), r, (0, 255, 0), 4)
						cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
						return [x,r]

	cv2.imshow("output",img)




def turn_right():
	print("Direita")
'''	rospy.init_node("tennis_ball")
	pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)
	speed = rospy.get_param("~speed", 0.5)
	turn = rospy.get_param("~turn", 1.0)
	twist = Twist()
	twist.linear.x = 0*speed; twist.linear.y = 0*speed; twist.linear.z = 0*speed;
	twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = -1*turn
	pub.publish(twist)'''


def turn_left():
	print("Esquerda")
'''	rospy.init_node("tennis_ball")
	pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)
	speed = rospy.get_param("~speed", 0.5)
	turn = rospy.get_param("~turn", 1.0)
	twist = Twist()
	twist.linear.x = 0*speed; twist.linear.y = 0*speed; twist.linear.z = 0*speed;
	twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 1*turn
	pub.publish(twist)'''


def forward():
	print("Frente")
'''	rospy.init_node("tennis_ball")
	pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)
	speed = rospy.get_param("~speed", 0.5)
	turn = rospy.get_param("~turn", 1.0)
	twist = Twist()
	twist.linear.x = 1*speed; twist.linear.y = 0*speed; twist.linear.z = 0*speed;
	twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 1*turn
	pub.publish(twist)'''

def position(x,r,camera):
	ret, img = camera.read()
	if  438>x>410:
		if r < 130:
			forward()
		if r>=120:
			return 1
	elif x < 404:
		turn_right()
	else:
		turn_left()
	


def main():
	
	cap = cv2.VideoCapture(0)
	while True:
		returns = check_tennis_ball(cap)
		if returns != None:
			x = returns[0]
			r = returns[1]
			if position(x,r,cap) == 1:
				print("EH TETRA")
				break
			else:
				check_tennis_ball(cap)



if __name__ == "__main__":
	main()
