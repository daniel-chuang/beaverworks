# Example from https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html#py-template-matching
# Annotations by me

# Imports
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Loading in the base image and the image template
img_rgb = cv2.imread('../mario.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) # <- Converts the image from BGR to Gray
template = cv2.imread('../mario_coin.png',0)
w, h = template.shape[::-1] # <- gets the width and height of the template

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) # <- uses OpenCV's template matching
threshold = 0.8 
loc = np.where(res >= threshold) # <- anything above the threshold in similarity is included
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imwrite('res.png',img_rgb)