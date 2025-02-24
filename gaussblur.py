import numpy as np
from scipy.signal import convolve2d
from PIL import Image

def gaussian_kernel(size, sigma):

    ax = np.arange(-(size // 2), size // 2 + 1)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return kernel / np.sum(kernel)

def apply_gaussian_blur(image, kernel_size, sigma):
  
    kernel = gaussian_kernel(kernel_size, sigma)
    
    if len(image.shape) == 2: 
        return convolve2d(image, kernel, mode='same', boundary='symm')
    elif len(image.shape) == 3:  
        blurred_image = np.zeros_like(image)
        for i in range(3):  
            blurred_image[:, :, i] = convolve2d(image[:, :, i], kernel, mode='same', boundary='symm')
        return blurred_image
    else:
        raise ValueError("Unsupported image shape")

def main():
    image = Image.open("/your image path")
    image = np.array(image)

    kernel_size = 5  
    sigma = 1.0

    blurred_image = apply_gaussian_blur(image, kernel_size, sigma)

    blurred_image = np.clip(blurred_image, 0, 255).astype(np.uint8)
    blurred_image = Image.fromarray(blurred_image)
    blurred_image.save("blurred_image.jpg")
    blurred_image.show()

if __name__ == "__main__":
    main()
