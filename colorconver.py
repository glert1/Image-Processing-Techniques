import cv2
import numpy as np

image = cv2.imread('/your image path')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


gray_3channel = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
combined_image = np.hstack((image, gray_3channel, hsv_image))

cv2.imshow('Combined Image', combined_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
