import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('/your image path', cv2.IMREAD_GRAYSCALE)

histogram, bins = np.histogram(image.ravel(), 256, [0, 256])

_, otsu_threshold = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

manual_threshold_value = 127
_, manual_threshold = cv2.threshold(image, manual_threshold_value, 255, cv2.THRESH_BINARY)

plt.figure(figsize=(10, 7))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.plot(histogram)
plt.title('Histogram')
plt.xlabel('Piksel Değeri')
plt.ylabel('Frekans')

plt.subplot(2, 2, 3)
plt.imshow(otsu_threshold, cmap='gray')
plt.title(f'Otsu Thresholding (T = {int(_)})')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(manual_threshold, cmap='gray')
plt.title(f'Manuel Thresholding (T = {manual_threshold_value})')
plt.axis('off')

plt.tight_layout()
plt.show()
