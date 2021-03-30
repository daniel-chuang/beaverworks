# Importing OpenCV and Numpy
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load in the image of messi
img = cv2.imread("../messi.jpeg")

# Padding images
new = cv2.copyMakeBorder(img, 30, 30, 30, 60, cv2.BORDER_CONSTANT, value=[255,0,0])
                  #src, top, bottom, left, right, borderType, value of color (if border type is constant))

# Show plot
plt.subplot(331),plt.imshow(img,'gray'),plt.title('Original')
plt.subplot(232),plt.imshow(new,'gray'),plt.title('Padding Applied')
plt.show()