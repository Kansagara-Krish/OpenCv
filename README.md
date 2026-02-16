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

### 6. **Image Filtering & Enhancement**
   - Bitwise operations (`cv2.bitwise_and()`, `cv2.bitwise_or()`, etc.)
   - Gaussian blur for smoothing (`cv2.GaussianBlur()`)
   - Median blur for noise removal (`cv2.medianBlur()`)
   - Image sharpening using kernels
   - Thresholding techniques (`cv2.threshold()`, `cv2.adaptiveThreshold()`)
   - Canny edge detection (`cv2.Canny()`)

### 7. **Contour Detection & Analysis**
   - Finding contours in images (`cv2.findContours()`)
   - Drawing contours (`cv2.drawContours()`)
   - Contour properties and analysis

### 8. **Object Detection - Cascade Classifiers**
   - Haar Cascade Classifiers for face detection
   - Eye detection using cascades
   - Smile detection and recognition
   - Loading and applying pre-trained classifiers

### 9. **Video Processing**
   - Capturing video from webcam using `cv2.VideoCapture()`
   - Reading and processing video files
   - Saving video using `cv2.VideoWriter()`
   - Real-time frame processing

---

## 📁 Project Structure

```
OpenCV/
├── README.md                          # This file
│
├── Introduction/                      # Basic concepts and fundamentals
│   ├── grey_scale.py                  # Convert image to grayscale
│   ├── image_dimnesion.py             # Get image dimensions and properties
│   ├── loading.py                     # Basic image loading and saving
│   └── Mini_project_1.py              # Interactive grayscale converter
│
├── Image Drawing Function/            # Drawing shapes and text on images
│   ├── circle.py                      # Draw circles
│   ├── rectangle.py                   # Draw rectangles
│   ├── line.py                        # Draw lines
│   ├── font.py                        # Add text to images
│   └── Mini_project_2.py              # Interactive shape drawing tool
│
├── Image Resizing/                    # Image transformations
│   ├── resize.py                      # Resize images
│   ├── rotate.py                      # Rotate images
│   ├── flip.py                        # Flip images
│   └── slicing.py                     # Extract Region of Interest (ROI)
│
├── Image Filtering/                   # Image filtering and enhancement
│   ├── bitwise_op.py                  # Bitwise operations on images
│   ├── canny_func.py                  # Canny edge detection
│   ├── Guassian_blur.py               # Gaussian blur filter
│   ├── median.py                      # Median blur filter
│   ├── sharpning.py                   # Image sharpening
│   └── threshod_fun.py                # Image thresholding techniques
│
├── Contour_fun.py/                    # Contour detection and analysis
│   └── contour_fun.py                 # Detect and draw contours
│
├── Face detection/                    # Face, eye, and smile detection
│   ├── app.py                         # Basic face detection
│   ├── Face_smile_eyes.py             # Detect faces, eyes, and smiles with labels
│   ├── haarcascade_eye.xml            # Cascade classifier for eyes
│   ├── haarcascade_frontalcatface.xml # Cascade classifier for cat faces
│   └── haarcascade_smile.xml          # Cascade classifier for smiles
│
└── Video Processing workflow/         # Video capture and processing
    ├── reading_video.py               # Read and display video from file or webcam
    └── saving_video.py                # Capture video from webcam and save to file
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

### Introduction (Fundamentals)

#### `grey_scale.py`
Converts a colored image to grayscale format.
```
Concepts: Color space conversion, BGR to GRAY
Input: Any image file
Output: Grayscale image displayed on screen
```

#### `image_dimnesion.py`
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
Output: Saved image
```

#### `Mini_project_1.py` ⭐
Interactive grayscale converter with save/view options.
```
Concepts: File path handling, conditional operations, user input
Input: User-provided image path
Output: Grayscale image (saved or displayed)
Features: Error handling, flexible file paths
```

### Image Drawing Functions

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

### Image Resizing & Transformations

#### `resize.py`
Resizes an image to specified dimensions.
```
Concepts: Image resizing, aspect ratio handling
Input: Image file
Output: Resized image
```

#### `rotate.py`
Rotates an image by a specified angle.
```
Concepts: Rotation matrix, warpAffine(), geometric transformations
Input: Image file
Output: Rotated image
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

### Image Filtering & Enhancement

#### `bitwise_op.py`
Performs bitwise operations on images (AND, OR, XOR, NOT).
```
Concepts: Bitwise operations, image masking
Input: Image file(s)
Output: Result of bitwise operations
```

#### `Guassian_blur.py`
Applies Gaussian blur filter to smooth images and reduce noise.
```
Concepts: Kernel-based filtering, blurring
Input: Image file
Output: Blurred image
```

#### `median.py`
Applies median blur for effective noise removal.
```
Concepts: Non-linear filtering, noise reduction
Input: Image file with noise
Output: Denoised image
```

#### `canny_func.py`
Implements Canny edge detection algorithm.
```
Concepts: Edge detection, gradient computation
Input: Image file
Output: Detected edges
```

#### `sharpning.py`
Sharpens images using kernel-based operations.
```
Concepts: Kernel operations, image enhancement
Input: Image file
Output: Sharpened image
```

#### `threshod_fun.py`
Applies various thresholding techniques to images.
```
Concepts: Binary thresholding, adaptive thresholding
Input: Grayscale image or color image
Output: Thresholded binary image
```

### Contour Operations

#### `contour_fun.py`
Detects and draws contours in images.
```
Concepts: Contour detection, hierarchy, contour properties
Input: Image file
Output: Image with contours overlaid
```

### Face Detection

#### `app.py`
Basic face detection from webcam feed.
```
Concepts: Haar Cascade Classifiers, real-time detection
Input: Webcam video stream
Output: Video with detected faces highlighted
```

#### `Face_smile_eyes.py` ⭐⭐
Advanced real-time detection of faces, eyes, and smiles.
```
Concepts: Multiple cascade classifiers, ROI extraction, labeled detection
Input: Webcam video stream
Output: Video with labeled detections (Face, Eyes, Smile in different colors)
Features: Color-coded rectangles, text labels, real-time processing
```

### Video Processing

#### `reading_video.py`
Reads and displays video from file or webcam.
```
Concepts: VideoCapture, frame processing, real-time streaming
Input: Video file or webcam (device ID: 0)
Output: Video playback with processing
```

#### `saving_video.py`
Captures video from webcam and saves to file.
```
Concepts: VideoCapture, VideoWriter, codec selection
Input: Webcam video stream
Output: Saved video file
```

---

## 🚀 Quick Start

### Example 1: Convert Image to Grayscale

```bash
python Introduction/grey_scale.py
```

### Example 2: Draw Shapes Interactively

```bash
python Image\ Drawing\ Function/Mini_project_2.py
# Enter image path when prompted
# Select shape type (line/circle/rectangle/text)
# Provide coordinates and parameters
# Choose to save or view the result
```

### Example 3: Image Filtering & Enhancement

```bash
python Image\ Filtering/canny_func.py          # Edge detection
python Image\ Filtering/Guassian_blur.py       # Blur filter
python Image\ Filtering/threshod_fun.py        # Thresholding
```

### Example 4: Resize and Rotate

```bash
python Image\ Resizing/resize.py
python Image\ Resizing/rotate.py
```

### Example 5: Detect Contours

```bash
python Contour_fun.py/contour_fun.py
```

### Example 6: Real-time Face Detection (Webcam)

```bash
python Face\ detection/Face_smile_eyes.py
# Press 'q' to exit
```

### Example 7: Video Processing

```bash
python Video\ Processing\ workflow/reading_video.py   # Play video
python Video\ Processing\ workflow/saving_video.py    # Record video
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
✅ **Image Filtering**: Applying blur, sharpening, and edge detection  
✅ **Thresholding**: Converting images to binary format with various techniques  
✅ **Contour Detection**: Finding and analyzing object contours  
✅ **Object Detection**: Using Haar Cascade Classifiers for face/eye/smile detection  
✅ **Real-time Processing**: Processing video streams from webcam  
✅ **Video I/O**: Reading, playing, and saving video files  
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
| `cv2.GaussianBlur()` | Apply Gaussian blur filter |
| `cv2.medianBlur()` | Apply median blur filter |
| `cv2.Canny()` | Perform Canny edge detection |
| `cv2.threshold()` | Apply binary thresholding |
| `cv2.adaptiveThreshold()` | Apply adaptive thresholding |
| `cv2.bitwise_and()` | Bitwise AND operation |
| `cv2.bitwise_or()` | Bitwise OR operation |
| `cv2.bitwise_xor()` | Bitwise XOR operation |
| `cv2.bitwise_not()` | Bitwise NOT operation |
| `cv2.findContours()` | Find contours in image |
| `cv2.drawContours()` | Draw contours on image |
| `cv2.CascadeClassifier()` | Load Haar cascade classifier |
| `cv2.CascadeClassifier.detectMultiScale()` | Detect objects using cascade |
| `cv2.VideoCapture()` | Capture video from file or camera |
| `cv2.VideoWriter()` | Write video to file |

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
