import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_salt_and_pepper_noise(image, amount=0.02):
    noisy_image = image.copy()
    num_salt = int(amount * image.size * 0.5)
    num_pepper = int(amount * image.size * 0.5)

    
    coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 255


    coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 0

    return noisy_image

def add_gaussian_noise(image, mean=0, var=0.01):
    sigma = var ** 0.5
    gaussian = np.random.normal(mean, sigma, image.shape)
    noisy_image = image + gaussian * 255
    return np.clip(noisy_image, 0, 255).astype(np.uint8)

def add_speckle_noise(image):
    noise = np.random.randn(*image.shape)
    noisy_image = image + image * noise
    return np.clip(noisy_image, 0, 255).astype(np.uint8)

def main():
    image = cv2.imread('your image path', cv2.IMREAD_GRAYSCALE)

    salt_pepper = add_salt_and_pepper_noise(image, amount=0.02)
    gaussian = add_gaussian_noise(image, mean=0, var=0.0)
    speckle = add_speckle_noise(image)

    plt.figure(figsize=(10, 8))

    plt.subplot(2, 2, 1)
    plt.title("Original Image")
    plt.imshow(image, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.title("Salt and Pepper Noise")
    plt.imshow(salt_pepper, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.title("Gaussian Noise")
    plt.imshow(gaussian, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.title("Speckle Noise")
    plt.imshow(speckle, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
