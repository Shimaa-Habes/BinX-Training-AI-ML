# 🖼️ Day 3 — Computer Vision Preprocessing with OpenCV

## 📌 Overview

Day 3 focuses on preparing images for deep learning models using OpenCV
and TensorFlow/Keras.

The notebook covers image standardization, OpenCV fundamentals,
image augmentation, and preprocessing for transfer learning.

---

## 🎯 Learning Objectives

- Understand why image preprocessing is important.
- Read and resize images using OpenCV.
- Convert images from BGR to RGB.
- Normalize pixel values from 0–255 to 0–1.
- Understand the BGR vs RGB issue.
- Build an image augmentation pipeline.
- Apply rotation, zoom, flipping, brightness changes, and rescaling.
- Visualize augmented images.
- Understand preprocessing requirements for pre-trained models.
- Use `preprocess_input` with transfer learning.

---

## 🔧 Technologies

- Python
- OpenCV
- TensorFlow
- Keras
- NumPy
- Matplotlib

---

## 📂 Notebook Structure

### 3.1 Why Images Need Preprocessing
Explains why image inputs should be standardized before model training.

### 3.2 OpenCV Fundamentals
Covers:
- Image reading
- Resizing
- BGR → RGB conversion
- Pixel normalization
- Edge detection

### 3.3 Building an Augmentation Pipeline
Uses `ImageDataGenerator` to apply:
- Rotation
- Zoom
- Horizontal flipping
- Brightness changes
- Rescaling

### 3.4 Connecting to Transfer Learning
Explains how preprocessing must match the expectations of the selected
pre-trained architecture.

### Hands-On Lab
Builds a complete preprocessing function and augmentation workflow.

---

## 🧪 Main Preprocessing Pipeline

```text
Raw Image
    ↓
Read with OpenCV
    ↓
Resize
    ↓
BGR → RGB
    ↓
Normalize
    ↓
Model-Ready Image
```

## 🔗 Transfer Learning

When using a pre-trained model, the input preprocessing should match
the preprocessing expected by that model.
For example, MobileNetV2 provides:

```python
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
```

## 🚀 Git Workflow

```bash
git add .
git commit -m "Complete Day 3: Computer Vision Preprocessing"
git push
```

Then open a Pull Request for mentor review.

## ✅ Status

Day 3 completed — Computer Vision Preprocessing with OpenCV