# Week 7 — Day 1: CNNs & Sprint 2 Planning

## 📌 Overview

Day 1 of Week 7 marks the beginning of **Sprint 2** in Phase 3 of the BinX Tech AI & Machine Learning Internship.

The focus of this day is to understand the fundamental ideas behind **Convolutional Neural Networks (CNNs)** and why convolution is more efficient than fully connected layers when working with image data.

The day also begins with Sprint 2 planning, including defining the sprint goal, backlog, and the improvement carried forward from the Sprint 1 retrospective.

---

## 🎯 Learning Objectives

By the end of Day 1, we should be able to:

* Understand the goal and structure of Sprint 2.
* Explain why Dense Networks are inefficient for image data.
* Understand convolution and how filters detect local patterns.
* Explain the role of kernels, feature maps, stride, and padding.
* Connect convolution to the dot-product operation.
* Understand parameter sharing and translation invariance.
* Explain the feature hierarchy learned by CNNs.
* Identify which architecture is appropriate for different data types.

---

## 🗓️ Sprint 2 Planning

### Sprint Goal

Advance the core model while applying appropriate deep-learning concepts and maintaining structured experimentation and evaluation.

### Sprint 2 Backlog

* Study CNNs, RNNs, LSTMs, and Transformers.
* Understand convolution, filters, and feature maps.
* Implement a convolution operation using NumPy.
* Analyze parameter sharing and translation invariance.
* Advance the core model.
* Compare experiments using consistent evaluation metrics.
* Document experiments and results for the Sprint Review.

### Sprint 1 Retrospective Improvement

The Sprint 2 workflow carries forward the improvement of using **structured experiments and consistent evaluation metrics** when evaluating model changes.

---

## 🖼️ CNN Fundamentals

### Why Dense Networks Fail on Images

A `200 × 200 × 3` color image contains:

**120,000 input values**

A Dense layer with 128 neurons requires:

**15,360,128 trainable parameters**

In comparison, a CNN layer using a `3 × 3` kernel, 3 input channels, and 32 filters requires only:

**896 trainable parameters**

This demonstrates the major efficiency advantage of convolution through **parameter sharing**.

---

## 🔍 Convolution

A convolution filter is a small matrix of learnable weights that moves across an image and performs a local dot product at each position.

### Key Concepts

* **Filter / Kernel:** A small matrix used to detect a specific pattern.
* **Feature Map:** The output produced by applying a filter to an image.
* **Stride:** The number of pixels the filter moves at each step.
* **Padding:** Extra pixels added around the image to control the output size.

The same filter is reused across different locations, allowing the CNN to detect the same pattern wherever it appears.

---

## 🧪 Hands-On Convolution

A simple grayscale image was generated using NumPy.

A hand-designed `3 × 3` edge-detection filter was then applied manually using convolution.

The resulting feature map demonstrates where the selected edge pattern appears in the image.

### Implementation

The convolution process includes:

1. Generate the sample image.
2. Define the `3 × 3` edge-detection filter.
3. Extract local image patches.
4. Calculate the dot product between each patch and the filter.
5. Store the results in a feature map.
6. Visualize the original image and the resulting feature map.

---

## ⚡ Why Convolution Wins

CNNs provide two important advantages:

### Parameter Sharing

The same filter is reused across the entire image instead of learning separate weights for every location.

### Translation Invariance

Because the filter scans across the image, the network can detect a pattern regardless of where it appears.

### Feature Hierarchy

CNNs progressively learn more complex features:

**Early Layers → Edges**

**Middle Layers → Shapes & Textures**

**Deep Layers → Objects**

---

## 🏗️ Architecture Selection

The appropriate architecture depends on the structure of the input data:

| Data Type               | Suitable Architecture |
| ----------------------- | --------------------- |
| Images                  | CNN                   |
| Sequential Data         | RNN / LSTM            |
| Text / Token Sequences  | Transformer           |
| Structured Tabular Data | Dense Network         |

For this day, CNNs are studied to understand their architecture and behavior, while the actual project architecture is selected according to the project's data type.

---

## 🛠️ Tools & Technologies

* Python
* NumPy
* Matplotlib
* Jupyter Notebook
* VS Code
* Git
* GitHub

---

## 📁 Day 1 Structure

```text
Day1/
│
├── cnn.ipynb
├── hands_on_lab.ipynb
└── README.md
```

---

## ✅ Day 1 Outcome

By the end of Day 1, the fundamental concepts of CNNs and convolution were covered, including:

* Sprint 2 planning
* Dense vs. CNN parameter efficiency
* Filters and kernels
* Feature maps
* Convolution using NumPy
* Edge detection
* Parameter sharing
* Translation invariance
* CNN feature hierarchy
* Architecture selection based on data type
