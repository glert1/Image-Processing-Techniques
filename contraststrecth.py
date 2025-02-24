import cv2
import numpy as np
import matplotlib.pyplot as plt

def contrast_stretching(image):
    min_val = np.min(image)
    max_val = np.max(image)

    stretched = ((image - min_val) / (max_val - min_val) * 255).astype(np.uint8)
    return stretched

image_path = '/your image path' 
gray_image = cv2.imread(image_path)

stretched_image = contrast_stretching(gray_image)

plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title("Orijinal Görüntü")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.hist(gray_image.ravel(), bins=256, range=[0, 256], color='blue', alpha=0.7)
plt.title("Orijinal Görüntü Histogramı")

plt.subplot(2, 2, 3)
plt.imshow(stretched_image, cmap='gray')
plt.title("Kontrast Gerilmiş Görüntü")
plt.axis('off')

plt.subplot(2, 2, 4)
plt.hist(stretched_image.ravel(), bins=256, range=[0, 256], color='green', alpha=0.7)
plt.title("Kontrast Gerilmiş Görüntü Histogramı")

plt.tight_layout()
plt.show()
