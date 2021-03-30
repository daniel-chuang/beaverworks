# Importing OpenCV and Numpy
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load in the image of messi
img = cv2.imread("../messi.jpeg")
print(img.shape)

# Display Original Image
plt.subplot(231),plt.imshow(img,'gray'),plt.title('Original')

# Image ROI
ball = img[0:40, 0:40]
img[100:140, 100:140] = ball

# Display Image
plt.subplot(232),plt.imshow(img,'gray'),plt.title('ROI Applied')

plt.show()