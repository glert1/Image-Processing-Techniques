# 📷 Image Processing Techniques in Python

This repository contains Python scripts demonstrating various image processing techniques using popular libraries such as OpenCV, NumPy, Matplotlib, SciPy, and PIL. Each script applies specific image processing operations including blurring, color conversion, contrast stretching, noise addition, and morphological operations.

---

## 📁 Project Structure

The repository consists of the following Python scripts:

- **`blur.py`**  
  Applies different types of blurring techniques to an image:
  - Gaussian Blur
  - Median Blur
  - Bilateral Blur

- **`colorconvertionmatplot.py`**  
  Converts images into different color spaces and displays them:
  - Grayscale
  - HSV (Hue, Saturation, Value)
  - RGB (for visualization)

- **`contraststrecth.py`**  
  Performs contrast stretching to enhance the dynamic range of an image and visualizes the histograms.

- **`gaussblur.py`**  
  Applies a custom Gaussian blur using a manually created kernel and saves the blurred image.

- **`colorconver.py`**  
  Converts an image to grayscale and HSV, then combines the images side by side for comparison.

- **`morfolojik.py`**  
  Implements morphological operations:
  - Erosion
  - Dilation  
  These operations are visualized with corresponding histograms.

- **`noise.py`**  
  Adds different types of noise to an image:
  - Salt and Pepper Noise
  - Gaussian Noise
  - Speckle Noise

---

## 🔧 Requirements

Make sure you have Python 3.x installed. Then, install the required libraries using:

```bash
pip install opencv-python numpy matplotlib scipy pillow
```
## 🚀 How to Run

### 🔄 Update Image Path:
Replace `'/your image path'` in each script with the actual path to your input image.

### 💻 Execute Scripts:
Run the scripts using the terminal:

```bash
python script_name.py
```


### 👁️ View Output

- Some scripts will display output images using **Matplotlib**.
- Others will save the processed images directly to your working directory.

---

## 💡 Features Explained

### 🌀 Blurring Techniques (`blur.py`, `gaussblur.py`)
Smoothens the image using various blurring filters to reduce noise and detail:
- **Gaussian Blur**
- **Median Blur**
- **Bilateral Filter**

### 🌈 Color Space Conversions (`colorconvertionmatplot.py`, `colorconver.py`)
Transforms images to different color spaces for visualization and preprocessing:
- **Grayscale**: Converts the image to shades of gray.
- **HSV (Hue, Saturation, Value)**: Converts the image to a color space better suited for color-based segmentation.

### 🌟 Contrast Enhancement (`contraststrecth.py`)
Improves the contrast of the image by stretching the intensity values. This enhancement is visualized using histograms:
- **Before Stretching**: Shows the original pixel intensity distribution.
- **After Stretching**: Displays the enhanced contrast distribution.

### 🔍 Morphological Transformations (`morfolojik.py`)
Applies morphological operations commonly used in image preprocessing:
- **Erosion**: Shrinks objects in a binary image, useful for removing small noise.
- **Dilation**: Expands objects, which can fill small holes and enhance features.

### 🎭 Noise Addition (`noise.py`)
Introduces various noise types into an image for testing the robustness of filters and denoising algorithms:
- **Salt and Pepper Noise**: Randomly adds black and white pixels.
- **Gaussian Noise**: Adds values from a Gaussian distribution to simulate sensor noise.
- **Speckle Noise**: Multiplies random noise to simulate granular disturbances.



## 🤝 Contributing

Contributions are welcome! If you'd like to contribute, please:
- Fork the repository.
- Create a feature branch.
- Submit a pull request.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---




