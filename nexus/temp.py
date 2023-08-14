import cv2
import numpy as np

vid = cv2.VideoCapture('http://192.168.110.242/mjpegfeed?640x480')

if (vid.isOpened()== False): 
  print("Error opening video stream or file")

