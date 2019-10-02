#!/usr/bin/env python
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def circleDetect():
       frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
       frame_gray = cv2.blur(frame_gray, (3, 3)) 
       detected_circles = cv2.HoughCircles(frame_gray,cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 40) 
       if detected_circles is not None: 
             detected_circles = np.uint16(np.around(detected_circles)) 
             for pt in detected_circles[0, :]: 
                 a, b, r = pt[0], pt[1], pt[2] 
                 cv2.circle(frame, (a, b), r, (0, 255, 0), 2) 
                 cv2.circle(frame, (a, b), 1, (0, 0, 255), 3) 
       

def squareDetect():
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret,thresh = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)

        contours,h = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
              approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
              if len(approx)==4:
                   cv2.drawContours(img, [approx], 0, (0), 5)
                   x = approx.ravel()[0]
                   y = approx.ravel()[1]
                   cv2.putText(img, "Rectangle", (x, y), font, 1, (0))

    

while True:
	ret, frame = cap.read()

	circleDetect()

	#squareDetect()

	cv2.imshow('frame', frame)

	cv2.waitKey(3)

cap.release()
cv2.destroyAllWindows()
