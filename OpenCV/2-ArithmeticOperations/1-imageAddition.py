# Importing OpenCV, Numpy, and MatPlotLib
import cv2
import numpy as np
from matplotlib import pyplot as plt

x = np.uint8([250])
y = np.uint8([10])

print(cv2.add(x,y)) # 250 + 10 = 260 => 255
print(x+y) # 250 + 10 = 260 = 266 % 255 = 4