#!/usr/bin/env python
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
_width  = 400.0
_height = 420.0
_margin = 0.0
corners = np.array([[[_margin, _margin]],[[_margin, _height + _margin  ]],[[ _width + _margin, _height + _margin  ]],[[ _width + _margin, _margin]],])

pts_dst = np.array( corners, np.float32 )
def circleDetect():
       frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
       frame_gray = cv2.medianBlur(cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY),5)
       detected_circles = cv2.HoughCircles(frame_gray,cv2.HOUGH_GRADIENT, 1, 50, param1 = 50, param2 = 30, minRadius = 10, maxRadius = 50) 
       if detected_circles is not None: 
             detected_circles = np.uint16(np.around(detected_circles)) 
             for pt in detected_circles[0, :]: 
                 a, b, r = pt[0], pt[1], pt[2]
                 cv2.circle(frame, (a, b), r, (0, 255, 0), 2) 
                 cv2.circle(frame, (a, b), 1, (0, 0, 255), 3) #center red dot
       

def squareDetect():
        global frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred_img=cv2.GaussianBlur(gray,(5,5),0)
        r,thresh = cv2.threshold(blurred_img, 60, 255, cv2.THRESH_BINARY)
        contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
        for cnt in contours:
               if cv2.contourArea(cnt)>50:
                  perimeter = cv2.arcLength( cnt, True )

                  curve = cv2.approxPolyDP(cnt, 0.05 * perimeter, closed=True)
                  if len(curve)==4:
                        x,y,w,h = cv2.boundingRect(curve)
                        #print(x,y,w,h)
                        if(w/h)>.8 and (w/h)<1.1:
                           frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                           cv2.putText(frame,"Square",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
while True:
	ret, frame = cap.read()

	circleDetect()

	squareDetect()

	cv2.imshow('frame', frame)

	cv2.waitKey(3)

cap.release()
cv2.destroyAllWindows()
