import cv2
import numpy as np


class ColorLabeler:
    def __init__(self):
        self.red_lower = np.array([136, 87, 111], np.uint8)
        self.red_upper = np.array([180, 255, 255], np.uint8)
        
        self.green_lower = np.array([25, 52, 72], np.uint8)
        self.green_upper = np.array([102, 255, 255], np.uint8)
        
        self.blue_lower = np.array([94, 80, 2], np.uint8)
        self.blue_upper = np.array([120, 255, 255], np.uint8)
        
        self.color = ""
        
        
    def label(self, image, c):
        # construct a mask for the contour, then compute the
        # average L*a*b* value for the masked region
        mask = np.zeros(image.shape[:2], dtype="uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)
        mask = cv2.erode(mask, None, iterations=2)
        mean = cv2.mean(image, mask=mask)[:3]
        
        if (np.all(mean > self.red_lower) and np.all(mean < self.red_upper)):
            self.color = "red"
            
        elif (np.all(mean > self.green_lower) and np.all(mean < self.green_upper)):
            self.color = "green"
            
        elif (np.all(mean > self.blue_lower) and np.all(mean < self.blue_upper)):
            self.color = "blue"

        return self.color
  