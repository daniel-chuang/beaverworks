"""
Types of Thresholding:
general function - cv2.threshold(img, threshold min, threshold max, flag)

Name             -       FLAG
Thresh Binary - cv2.THRESH_BINARY
Thresh Inverse - cv2.THRESH_BINARY_INV
Thresh Truncated - cv2.THRESH_TRUNC
Thresh toZero - cv2.THRESH_TOZERO
Thresh to Zero Inverse - cv2.THRESH_TOZERO_INV
"""

# Imports
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Loading Gradient Image
img = cv2.imread("../gradient.jpeg", 0) # <-- the 0 flag puts a greyscale read. Anything x<0 returns image as is. Anything x>0 returns 3 channel.

# Thresholding the image
ret, thresh_binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) # <-- runs the thresholding on a greyscale image.
                                                                     # <-- anything that is over halfway (127) is "true"
ret, thresh_binary_inv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV) # <-- same result as above but all "true"s are
                                                                          # <-- inverted and same for all "false"s
ret, thresh_binary_truncated = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC) # <-- does thresh_binary but all originally
                                                                           # <-- "true" values are just the same color as the original
ret, thresh_toZero = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO) # does thresh_binary but all originally "false"
                                                                  # are their original color
ret, thresh_toZero_inv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV) # does thresh_vinary but all true values
                                                                          # keep their original value and all originally
                                                                          # "false" values are inverted to "true"

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh_binary, thresh_binary_inv, thresh_binary_truncated, thresh_toZero, thresh_toZero_inv]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()