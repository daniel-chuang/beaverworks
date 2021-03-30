# Imports
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load in images
img = cv2.imread("../newspaper.png", 0)
# img = cv2.medianBlur(img, 5) # <-- blurs the image

# Thresholding
ret, thresh_binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# adaptiveThreshold(src, dst, maxValue, adaptiveMethod, thresholdType, blockSize, C)
adaptive_thresh_mean = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2) # Uses mean
adaptive_thresh_gaussian = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2) # Uses gaussian

titles = ("Original", "Binary", "Adaptive Mean", "Adaptive Gaussian")
images = (img, thresh_binary, adaptive_thresh_mean, adaptive_thresh_gaussian)

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()