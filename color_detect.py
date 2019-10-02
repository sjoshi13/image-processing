#!/usr/bin/env python
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def redCircleDetect():
      global frame
      (contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#finding contours in "red" range
      #(_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
      for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area>500): #Lower limit on area of detected object
                        x,y,w,h = cv2.boundingRect(contour)
                        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                        cv2.putText(frame,"Red",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
def blueCircleDetect():
        global frame
        (contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #(_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
        for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area>500):
                        x,y,w,h = cv2.boundingRect(contour)
                        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                        cv2.putText(frame,"Blue",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))

def greenCircleDetect():
        global frame
        (contours,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #(_,contours,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
        for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area>500):
                        x,y,w,h = cv2.boundingRect(contour)
                        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                        cv2.putText(frame,"Green",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0)) 

while True:
	ret, frame = cap.read()
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	#defining the HSV Range of Red color
	red_lower=np.array([170,100,100],np.uint8)
	red_upper=np.array([180,255,255],np.uint8)
	#defining the HSV Range of Blue color
	blue_lower=np.array([99,115,150],np.uint8)
	blue_upper=np.array([110,255,255],np.uint8)
	#defining the HSV Range of Green color
	green_lower=np.array([40,40,40],np.uint8)
	green_upper=np.array([70,255,255],np.uint8)
	#finding the range of red,blue and yellow color in the image
	red=cv2.inRange(hsv, red_lower, red_upper)
	blue=cv2.inRange(hsv,blue_lower,blue_upper)
	green=cv2.inRange(hsv,green_lower,green_upper)
	#Defining convolution matrix
	kernal = np.ones((5 ,5), "uint8")
	red=cv2.dilate(red, kernal)
	
	blue=cv2.dilate(blue,kernal)

	green=cv2.dilate(green,kernal)
	
	greenCircleDetect()

	redCircleDetect()

	blueCircleDetect()


	cv2.imshow('frame', frame)

	cv2.waitKey(3)

cap.release()
cv2.destroyAllWindows()
