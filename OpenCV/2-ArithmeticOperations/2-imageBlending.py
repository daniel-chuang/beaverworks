# Importing OpenCV and Numpy
import cv2
import numpy as np

# Loads in two images with spliced dimensions(messi and a volcano)
img1 = cv2.imread("../messi.jpeg")[0:200, 0:200]
img2 = cv2.imread("../volcano-USGS-unsplash.jpg")[400:600, 400:600]

# Blends the images together with weighted alphas
dst = cv2.addWeighted(img1, 0, img2, 1, 0)

# Displays the image until the 0 key is pressed.
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()