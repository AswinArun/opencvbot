
import cv2
class ShapeDetector:
	def __init__(self):
		pass
	def detect(self, c):
		shape = "unidentified"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)
	
		if len(approx) == 3:
			shape = "triangle"

		elif len(approx) == 4:
			shape = "rectangle"

		else:
			shape = "circle"

		return shape