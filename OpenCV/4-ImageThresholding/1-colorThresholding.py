# Code from https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#converting-colorspaces
# Comment annotations from me
import cv2
import numpy as np

# Use my webcam as the video input
cap = cv2.VideoCapture(0)

while(True): # Keep on repeating

    # Take each frame
    _, frame = cap.read() # _ is a boolean value, returns True if the frame was successfully read

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # uses the cvtColor using the cv2.COLOR_BGR2HSV flag (look at previous file)

    # define range of blue color in HSV
    lower_blue = np.array([90,50,50]) # lowest blue color range
    upper_blue = np.array([150,255,255]) # highest blue color range

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue) # makes a boolean mask with TRUE for a pixel IF the color is in range

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask) # makes a mask over the original image

    cv2.imshow('frame',frame) # shows the frame
    cv2.imshow('hsv',hsv) # shows the frame
    cv2.imshow('mask',mask) # shows the mask
    cv2.imshow('res',res) #shows the final
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()