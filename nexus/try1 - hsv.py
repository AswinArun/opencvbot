

import cv2
import math
import numpy as np
import imutils
from shapedetector import ShapeDetector
from colordetHSV import ColorLabeler
from tupleSort import tupleSort


#change frame width and height code
  
cl = ColorLabeler()
sd = ShapeDetector()
ts = tupleSort()

# define a video capture object
vid = cv2.VideoCapture('http://192.168.81.155:4747/video?640*480')

# Check if camera opened successfully
if (vid.isOpened()== False): 
  print("Error opening video stream or file")
  
while(True):
    
    # Capture the video frame by frame
    ret, frame = vid.read()
    
    if ret == True:

        angle = 0 #angle declaration

        frameheight, framewidth = frame.shape[:2]

        min_x, min_y = 0, 0     #for choosing right or left path after encountering obstacle
        max_x, max_y = framewidth, frameheight
        
        path_choose = 0 #0 for straight, 1 for triangle, 2 for rectangle

        resized = imutils.resize(frame, width=300)
        ratio = frame.shape[0] / float(resized.shape[0])

        gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)

        (T,thresh) = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        
        minArea = 400
        maxArea = 5000

        cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        coorList = [] #to store circle coordinates
        
        for i, contour in enumerate(cnts):
            
            if i == 0:
                continue
            area = cv2.contourArea(contour)
            
            if area < minArea or area > maxArea:
                continue
            
            shape = sd.detect(contour)

            # multiply the contour (x, y)-coordinates by the resize ratio,
        	# then draw the contours and the name of the shape on the image
            contour = contour.astype("float")
            contour *= ratio
            contour = contour.astype("int")
            cv2.drawContours(frame, [contour], -1, (255,0,0), 2)
            
            x,y,w,h = cv2.boundingRect(contour)
            x_mid = int(x + w/2)
            y_mid = int(y + h/2)
            color = cl.label(hsv, contour)
            
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 4)

            cv2.putText(frame, color +" "+ shape, (x, y), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
            
            if shape == "circle":
                coorList.append( (x_mid, y_mid))
            
            elif shape == "triangle":
                path_choose = 1
                min_x = x_mid
                min_y = y_mid
                
            elif shape == "rectangle":
                path_choose = 2
                max_x = x_mid
                max_y = y_mid
            
        
        
        coorList = ts.SortY( coorList)
        prev = (0,0)
        for i, coor in enumerate(coorList):
            
            if (coor[1] < min_y or ((coor[0] > min_x) and (coor[0] < max_x))):
            
                if i == 0:
                    prev = coor
                    cv2.line(frame, (int(framewidth/2), frameheight), coor, (255,0,0), 2)
                    if coor[0] - framewidth / 2 != 0:
                        angle = math.atan((frameheight - coor[1]) / (coor[0] - framewidth / 2))
                    else:
                        angle = math.pi / 2
                    continue
                
                cv2.line(frame, prev, coor, (255,0,0), 2)
                prev = coor
            
        if angle < 0:
            angle = angle + math.pi/2
        print(angle)

        
        
        # Display the resulting frame
        cv2.imshow('Frame',frame)
     
        # Press Q on keyboard to  exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
          break
     
      # Break the loop
    else: 
        break
    
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()