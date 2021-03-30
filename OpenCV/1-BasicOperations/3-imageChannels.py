# Importing OpenCV and Numpy
import cv2
import numpy as np

# Load in the image of messi
img = cv2.imread("../messi.jpeg")

# Messing with image channels
# Splits the image up into BGR matrices, and then remerges it
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

# Makes a matrix of only B values (using Numpy indexing)
b = img[:,:,0]

# Sets all of the red channel to be equal to 0 in the image (using Numpy indexing)
img[:,:,2] = 0