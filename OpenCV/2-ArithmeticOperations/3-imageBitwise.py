# Importing OpenCV and Numpy
import cv2
import numpy as np

# Load two images
volcano = cv2.imread("../volcano-USGS-unsplash.jpg")
messi = cv2.imread("../messi.jpeg")
print(volcano.shape, messi.shape)
cv2.imshow('background original',volcano)
cv2.imshow('foreground original',messi)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Creating an ROI at the top left corner with a size of the smaller image (messi)
rows,cols,channels = messi.shape
roi = volcano[0:rows, 0:cols] # <-- creates an ROI in the volcano picture of the messi dimensions
cv2.imshow('roi',roi)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Creating a mask and inverse mask for smaller image (messi)
messigray = cv2.cvtColor(messi,cv2.COLOR_BGR2GRAY) # Convert to greyscale first
cv2.imshow('greyscale foreground',messigray)
cv2.waitKey(0)
cv2.destroyAllWindows()
#############################
ret, mask = cv2.threshold(messigray, 10, 255, cv2.THRESH_BINARY) # Converts greyscale to binary event (black or empty) using a threshold
mask_inv = cv2.bitwise_not(mask) # Uses inversion to inverse mask
cv2.imshow('foreground mask',mask)
cv2.imshow('foreground mask inversion',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Now black-out the area of logo in ROI
volcano_bg = cv2.bitwise_and(roi,roi,mask = mask_inv) # Uses inverted mask to delete area in volcano (background)
cv2.imshow('background with inverse mask applied',volcano_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Take only region of logo from logo image.
messi_fg = cv2.bitwise_and(messi,messi,mask = mask)
cv2.imshow('foreground with mask clipped',messi_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Put logo in ROI and modify the main image
dst = cv2.add(volcano_bg,messi_fg)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Apply dst to original background top left corner part
volcano[0:rows, 0:cols ] = dst
cv2.imshow('foreground after',volcano)
cv2.waitKey(0)
cv2.destroyAllWindows()