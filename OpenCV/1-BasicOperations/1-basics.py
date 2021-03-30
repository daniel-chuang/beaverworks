# Importing OpenCV and loading an image in.
import cv2
import numpy as numpy
img = cv2.imread("../messi.jpeg")

# Accessing a pixel value
px = img[100,100]
print("pixel value of image at 100, 100:", px)

# Accessing a color value of a pixel
blue = img[100, 100, 2]
print("blue pixel value of image at 100, 100:", blue)

# Modifying a color value of a pixel (BAD AND SLOW)
img[100, 100] = [255, 255, 255]
print("new pixel value of image at 100, 100:", img[100, 100])

# Modifying a color value of a pixel (FAST AND GOOD)
img.item(10,10,2) # <-- gets the RED value. OpenCV is in BGR
img.itemset((10,10,2), 100) # <--- replaces the RED value with 100
print("new blue pixel value of image at 100, 100:", img.item(10,10,2)) # <-- should be different now

# Returning the shape of an image
print("Tuple of rows, columns, and channels of image:", img.shape) # <--- returns a tuple of number of rows, columns, and channels
print("Pixel size of image:", img.size) # <--- returns the pixel size of an image
print("Image datatype:", img.dtype) # <--- returns the image datatype (useful for debugging)
