# imports
import cv2

# These are the flags that can be used for
# cv2.cvtColor(input_image, flag)
flags = [i for i in dir(cv2) if i.startswith("COLOR_")]
print(flags)

# example - before
img = cv2.imread("../messi.jpeg")
cv2.imshow("original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# example - after greyscale conversion
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("greyscale",grey)
cv2.waitKey(0)
cv2.destroyAllWindows()