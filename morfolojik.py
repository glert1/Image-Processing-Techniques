
import cv2 
import numpy as np 
from matplotlib import pyplot as plt

img = cv2.imread('your image path', 0) 

kernel = np.ones((5, 5), np.uint8) 

img_erosion = cv2.erode(img, kernel, iterations=1) 
img_dilation = cv2.dilate(img, kernel, iterations=1) 

plt.figure(figsize=(12, 6))

plt.subplot(3, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Orijinal Görüntü")
plt.axis('off')

plt.subplot(3, 2, 2)
plt.hist(img.ravel(), bins=256, range=[0, 256], color='blue', alpha=0.7)
plt.title("Orijinal Görüntü Histogramı")

plt.subplot(3, 2, 3)
plt.imshow(img_erosion, cmap='gray')
plt.title("Erozyon Görüntü")
plt.axis('off')

plt.subplot(3, 2, 4)
plt.hist(img_erosion.ravel(), bins=256, range=[0, 256], color='green', alpha=0.7)
plt.title("Erozyon Görüntü Histogramı")

plt.subplot(3, 2, 5)
plt.imshow(img_dilation, cmap='gray')
plt.title("Dilation Görüntü")
plt.axis('off')

plt.subplot(3, 2, 6)
plt.hist(img_dilation.ravel(), bins=256, range=[0, 256], color='green', alpha=0.7)
plt.title("Dilation Görüntü Histogramı")

plt.tight_layout()
plt.show()
