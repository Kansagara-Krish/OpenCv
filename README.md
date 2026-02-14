# OpenCV Learning Projects

A comprehensive collection of Python scripts demonstrating fundamental concepts in **OpenCV (Computer Vision)** for image processing and manipulation.

## 📋 Table of Contents

- [Overview](#overview)
- [Concepts Covered](#concepts-covered)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [File Descriptions](#file-descriptions)
- [Quick Start](#quick-start)
- [Learning Outcomes](#learning-outcomes)

---

## 🎯 Overview

This repository contains practical Python scripts that cover essential OpenCV concepts including:
- Image loading and saving
- Color space conversions
- Drawing geometric shapes
- Image transformations (resize, rotate, flip)
- Image manipulation and slicing

Perfect for beginners learning computer vision fundamentals!

---

## 📚 Concepts Covered

### 1. **Image I/O Operations**
   - Loading images using `cv2.imread()`
   - Displaying images using `cv2.imshow()`
   - Saving images using `cv2.imwrite()`

### 2. **Image Properties**
   - Getting image dimensions (height, width, channels)
   - Understanding BGR color format
   - Working with image shape and data types

### 3. **Color Space Conversion**
   - Converting images from BGR to Grayscale
   - Using `cv2.cvtColor()` for color transformations

### 4. **Drawing on Images**
   - Drawing lines (`cv2.line()`)
   - Drawing rectangles (`cv2.rectangle()`)
   - Drawing circles (`cv2.circle()`)
   - Adding text (`cv2.putText()`)

### 5. **Image Transformations**
   - Resizing images (`cv2.resize()`)
   - Rotating images (`cv2.getRotationMatrix2D()`, `cv2.warpAffine()`)
   - Flipping images (`cv2.flip()`)
   - Image slicing (Region of Interest - ROI)

---

## 📁 Project Structure

```
OpenCV/
├── README.md                          # This file
├── download.jpg                       # Sample image for processing
├── grey_scale.py                      # Convert image to grayscale
├── image_dimension.py                 # Get image dimensions and properties
├── loading.py                         # Basic image loading and saving
├── Mini_project_1.py                  # Interactive grayscale converter
│
├── image Drawing Function/            # Drawing shapes on images
│   ├── circle.py                      # Draw circles
│   ├── rectangle.py                   # Draw rectangles
│   ├── line.py                        # Draw lines
│   ├── font.py                        # Add text to images
│   └── Mini_project_2.py              # Interactive shape drawing tool
│
└── Image Resizing/                    # Image transformations
    ├── resize.py                      # Resize images
    ├── rotate.py                      # Rotate images
    ├── flip.py                        # Flip images
    └── slicing.py                     # Extract Region of Interest (ROI)
```

---

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Install OpenCV

```bash
pip install opencv-python
```

### Step 2: Clone or Download Repository

```bash
git clone <repository-url>
cd OpenCV
```

### Step 3: Verify Installation

```bash
python -c "import cv2; print(cv2.__version__)"
```

---

## 📄 File Descriptions

### Core Concepts

#### `grey_scale.py`
Converts a colored image to grayscale format.
```
Concepts: Color space conversion, BGR to GRAY
Input: Any image file
Output: Grayscale image displayed on screen
```

#### `image_dimension.py`
Extracts and displays image properties (height, width, channels).
```
Concepts: Image shape, dimensions, color channels (BGR)
Input: Any image file
Output: Console output with H, W, C values
```

#### `loading.py`
Basic image loading and saving operations.
```
Concepts: imread(), imwrite(), file I/O
Input: Any image file
Output: Saved image (output_write.png)
```

#### `Mini_project_1.py` ⭐
Interactive grayscale converter with save/view options.
```
Concepts: File path handling, conditional operations, user input
Input: User-provided image path
Output: Grayscale image (saved or displayed)
Features: Error handling, flexible file paths
```

### Drawing Shapes

#### `circle.py`
Draws a filled circle on an image.
```
Concepts: Drawing primitives, circle() function
Input: Image file
Output: Image with circle drawn
```

#### `rectangle.py`
Draws a filled rectangle on an image.
```
Concepts: Drawing primitives, rectangle() function
Input: Image file
Output: Image with rectangle drawn
```

#### `line.py`
Draws a line between two points on an image.
```
Concepts: Drawing primitives, line() function, coordinates
Input: Image file
Output: Image with line drawn
```

#### `font.py`
Adds text to an image with specified font and color.
```
Concepts: Text rendering, putText() function, fonts
Input: Image file
Output: Image with text overlay
```

#### `Mini_project_2.py` ⭐⭐
Interactive tool to draw multiple shapes on images with save/view options.
```
Concepts: Multiple drawing operations, user interaction, file I/O
Input: User-provided image path and shape parameters
Output: Modified image (saved or displayed)
Features: User-friendly interface, dynamic shape selection
```

### Image Transformations

#### `resize.py`
Resizes an image to specified dimensions.
```
Concepts: Image resizing, aspect ratio handling
Input: Image file
Output: Resized image (300x300 px)
```

#### `rotate.py`
Rotates an image by a specified angle.
```
Concepts: Rotation matrix, warpAffine(), geometric transformations
Input: Image file
Output: Rotated image (90 degrees)
```

#### `flip.py`
Flips an image horizontally, vertically, or both.
```
Concepts: Image flipping, flip() function
Input: Image file
Output: Different flip variations displayed
```

#### `slicing.py`
Extracts a Region of Interest (ROI) from an image.
```
Concepts: Array slicing, ROI selection, image cropping
Input: Image file
Output: Extracted ROI region
```

---

## 🚀 Quick Start

### Example 1: Convert Image to Grayscale

```bash
python grey_scale.py
```

### Example 2: Draw Shapes Interactively

```bash
python image\ Drawing\ Fuction\Mini_project_2.py
# Enter image path when prompted
# Select shape type (line/circle/rectangle/text)
# Provide coordinates and parameters
# Choose to save or view the result
```

### Example 3: Resize and Rotate

```bash
python Image\ Resizing\resize.py
python Image\ Resizing\rotate.py
```

### Example 4: Extract Region of Interest

```bash
python Image\ Resizing\slicing.py
```

---

## 💡 Learning Outcomes

After working through these projects, you will understand:

✅ **Image I/O**: Loading, displaying, and saving images  
✅ **Image Properties**: Understanding dimensions and color channels  
✅ **Color Spaces**: Converting between BGR and Grayscale  
✅ **Drawing Operations**: Creating geometric shapes and text overlays  
✅ **Transformations**: Resizing, rotating, flipping, and cropping images  
✅ **ROI Extraction**: Selecting and working with regions of interest  
✅ **Error Handling**: Validating file paths and handling exceptions  
✅ **User Interaction**: Creating interactive image processing tools  

---

## 🎓 Key OpenCV Functions Reference

| Function | Purpose |
|----------|---------|
| `cv2.imread()` | Read image from file |
| `cv2.imshow()` | Display image in window |
| `cv2.imwrite()` | Save image to file |
| `cv2.cvtColor()` | Convert color space |
| `cv2.resize()` | Resize image |
| `cv2.rotate()` / `cv2.warpAffine()` | Rotate image |
| `cv2.flip()` | Flip image |
| `cv2.line()` | Draw line |
| `cv2.circle()` | Draw circle |
| `cv2.rectangle()` | Draw rectangle |
| `cv2.putText()` | Add text to image |
| `cv2.waitKey()` | Wait for keyboard input |
| `cv2.destroyAllWindows()` | Close all image windows |

---

## 📝 Color Format Notes

OpenCV uses **BGR** (Blue, Green, Red) format, not RGB!

- `(255, 0, 0)` = Blue
- `(0, 255, 0)` = Green
- `(0, 0, 255)` = Red

---

## 🤝 Contributing

Feel free to:
- Add more examples
- Improve documentation
- Fix bugs
- Add advanced concepts

---

## 📚 Additional Resources

- [OpenCV Official Documentation](https://docs.opencv.org/)
- [OpenCV Python Tutorials](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)
- [Real Python OpenCV Guide](https://realpython.com/image-processing-with-the-python-pillow-library/)

---

## 📄 License

This project is open source and available for educational purposes.

---

## 👨‍💻 Author

Semester 6 Practical Projects

---

## 🎉 Happy Learning!

Start with the basic concepts and progressively work through the mini-projects for hands-on experience with computer vision!

**Last Updated**: February 2026
