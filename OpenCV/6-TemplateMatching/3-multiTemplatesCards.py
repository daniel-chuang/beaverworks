# Imports
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load base image
base_bgr = cv2.imread("../card.jpeg", 1)
base = cv2.imread("../card.jpeg", 0)
template = cv2.imread("../card-template.png", 0)
w, h = template.shape[::-1]

# Match the template!
res = cv2.matchTemplate(base, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold) # any location where the threshold is greater than 0.8

# Draw a rectangle at all locations
for pt in zip(*loc[::-1]): # <- zips all the locs together
    cv2.rectangle(base_bgr, pt, (pt[0] + w, pt[1] + h), (255,0,0), 2)

cv2.imshow("res", base_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()