# Imports
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../messi.jpeg',0)
edges = cv2.Canny(img,100,200) # <-- applies the ENTIRE canny algorithm!

cv2.imshow("original", img)
cv2.imshow("edges", edges)
cv2.waitKey(0)