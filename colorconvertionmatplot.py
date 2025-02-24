import cv2
from matplotlib import pyplot as plt

image = cv2.imread('/your image path')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(rgb_image)
plt.title('Original')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(hsv_image)
plt.title('HSV (Hue Visualization)')
plt.axis('off')

plt.tight_layout()
plt.show()   
