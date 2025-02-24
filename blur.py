import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('/your image path')

Gaussian = cv2.GaussianBlur(image, (7, 7), 0)

median = cv2.medianBlur(image, 5)

bilateral = cv2.bilateralFilter(image, 9, 75, 75)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(Gaussian)
plt.title("Gaussian Blurring")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(median)
plt.title("Median Blurring")
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(bilateral)
plt.title("Bilateral Blurring")
plt.axis('off')

plt.tight_layout()
plt.show()
