import cv2
import numpy as np
import imutils
from scipy.spatial import distance as dist
from shapedetector import ShapeDetector
from colordet import ColorLabeler

  
# define a video capture object
vid = cv2.VideoCapture(0)

# Check if camera opened successfully
if (vid.isOpened()== False): 
  print("Error opening video stream or file")
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    cl = ColorLabeler()
    sd = ShapeDetector()
    if ret == True:

        resized = imutils.resize(frame, width=300)
        ratio = frame.shape[0] / float(resized.shape[0])

        gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        lab = cv2.cvtColor(resized, cv2.COLOR_BGR2LAB)

        (T,thresh) = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        
        minArea = 400

        cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for i, contour in enumerate(cnts):
            
            if i == 0:
                continue
            area = cv2.contourArea(contour)
            
            if area < minArea:
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
            color = cl.label(lab, contour)
            
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 4)

            cv2.putText(frame, color +" "+ shape, (x, y), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
            
            
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