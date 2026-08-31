# 🧠 Week 7 · Day 2 — Building CNNs & Transfer Learning

> 🚀 **From building a CNN from scratch to leveraging a pre-trained deep learning model.**

---

## 🌟 Overview

Day 2 focused on **Convolutional Neural Networks (CNNs)** and **Transfer Learning** for image classification.

We started by understanding the main CNN building blocks, including:

* 🧩 Convolution
* ⚡ Activation Functions
* 🏊 Pooling
* 🔗 Fully Connected Layers
* 🎯 Classification

Then, we moved from theory to practice by building and comparing three different approaches:

> 🥇 **CNN from Scratch**
> 🔄 **CNN + Data Augmentation**
> 🚀 **Transfer Learning with MobileNetV2**

---

## 🎯 Learning Objectives

By the end of this day, we learned how to:

* 🧠 Understand the architecture of CNNs.
* 🔍 Understand how convolution extracts visual features.
* 🏊 Understand the purpose of pooling.
* 🛠️ Build a complete CNN using Keras.
* 🔄 Apply Data Augmentation to training images.
* 🔗 Understand Transfer Learning.
* 📦 Use a pre-trained **MobileNetV2** model.
* ❄️ Freeze pre-trained layers.
* 🔧 Understand the concept of Fine-Tuning.
* 📊 Compare different CNN approaches.
* 📈 Evaluate models using accuracy, validation accuracy, training time, and trainable parameters.

---

## 🏊 Pooling

**Pooling** reduces the spatial dimensions of feature maps while keeping important information.

It helps the network to:

* ⚡ Reduce computational cost.
* 📉 Reduce the number of parameters.
* 🎯 Preserve important visual features.
* 🛡️ Become less sensitive to small changes in image position.

For the implemented CNN, **MaxPooling2D** was used after the convolution layers.

---

## 🏗️ Full CNN Architecture

A complete CNN was built **from scratch** to establish a baseline model.

### 🔄 Architecture Flow

```text
🖼️ Input Image
      ↓
🔍 Conv2D
      ↓
🏊 MaxPooling2D
      ↓
🔍 Conv2D
      ↓
🏊 MaxPooling2D
      ↓
📐 Flatten
      ↓
🧠 Dense
      ↓
🎯 Output Layer
```

The **Convolutional Layers** extract visual features from the images.

The **Pooling Layers** reduce the spatial dimensions of the extracted feature maps.

The **Flatten Layer** converts the feature maps into a one-dimensional vector.

Finally, the **Dense Layers** use these extracted features to perform classification.

---

## 🔄 Data Augmentation

Data Augmentation creates different variations of existing training images.

Instead of always showing the CNN exactly the same image, random transformations are applied during training.

### 🎨 Transformations Used

* ↔️ **Horizontal Flip**
* 🔄 **Random Rotation**
* 🔍 **Random Zoom**

### 💡 Why use augmentation?

Data Augmentation can:

* 📚 Provide more varied training examples.
* 🛡️ Reduce overfitting.
* 🌍 Improve generalization.
* 🧠 Help the model learn more robust visual patterns.

### 📊 Experimental Result

In our experiment, augmentation **did not improve the measured performance**.

Both models achieved:

> 🎯 **50.00% Test Accuracy**
> 📈 **50.00% Validation Accuracy**

The augmented model also required more training time.

---

## 🚀 Transfer Learning

Transfer Learning allows us to reuse knowledge learned by a model trained on a large dataset.

For this experiment, we used:

### 📱 MobileNetV2

The model was loaded using:

```python
weights="imagenet"
```

and:

```python
include_top=False
```

This means that we used the pre-trained **feature extraction part** of MobileNetV2 and replaced its original classification head with our own classifier.

### 🧩 Architecture

```text
🖼️ Input Image
      ↓
🚀 Pre-trained MobileNetV2
      ↓
📊 GlobalAveragePooling2D
      ↓
🧠 Dense Layer
      ↓
🎯 Output Layer
```

MobileNetV2 already contains useful visual features learned from **ImageNet**, allowing our model to start with a strong representation instead of learning everything from zero.

---

## ❄️ Freezing & Fine-Tuning

### ❄️ Freezing

The MobileNetV2 base model was initially frozen:

```python
base.trainable = False
```

This keeps the pre-trained weights unchanged while training only the new classification layers.

### 🔧 Fine-Tuning

Fine-Tuning means making some of the pre-trained layers trainable later so that the model can adapt its learned features to the new dataset.

Fine-Tuning should be performed carefully using a **low learning rate** to avoid damaging useful pre-trained features.

---

# 🧪 Hands-On Experiments

Three different approaches were implemented and evaluated.

---

## 1️⃣ CNN from Scratch

The first experiment established a baseline by training a CNN from the beginning.

| 📊 Metric               |       Result |
| ----------------------- | -----------: |
| 🎯 Test Accuracy        |   **50.00%** |
| 📈 Validation Accuracy  |   **50.00%** |
| ⏱️ Training Time        | **300.92 s** |
| 🧠 Trainable Parameters |  **926,753** |

---

## 2️⃣ CNN + Data Augmentation

The second experiment introduced random image transformations during training.

| 📊 Metric               |       Result |
| ----------------------- | -----------: |
| 🎯 Test Accuracy        |   **50.00%** |
| 📈 Validation Accuracy  |   **50.00%** |
| ⏱️ Training Time        | **483.80 s** |
| 🧠 Trainable Parameters |  **926,753** |

📌 **Observation:** Data Augmentation did not improve the validation performance in this experiment.

---

## 3️⃣ 🚀 Transfer Learning

The final experiment used **MobileNetV2 with ImageNet weights** and a custom classification head.

| 📊 Metric               |       Result |
| ----------------------- | -----------: |
| 🎯 Test Accuracy        |   **88.70%** |
| 📈 Validation Accuracy  |   **90.05%** |
| ⏱️ Training Time        | **578.40 s** |
| 🧠 Trainable Parameters |   **41,025** |

🔥 Transfer Learning achieved a major improvement compared with both CNN models trained from scratch.

---

# 📊 Model Comparison

| 🧠 Model             | 🎯 Test Accuracy | 📈 Validation Accuracy | ⏱️ Training Time | 🔢 Trainable Parameters |
| -------------------- | ---------------: | ---------------------: | ---------------: | ----------------------: |
| CNN from Scratch     |           50.00% |                 50.00% |  **300.92 s** 🥇 |                 926,753 |
| CNN + Augmentation   |           50.00% |                 50.00% |         483.80 s |                 926,753 |
| 🚀 Transfer Learning |    **88.70%** 🥇 |          **90.05%** 🥇 |         578.40 s |           **41,025** 🥇 |

---

## 🏆 Best Performing Approach

### 🚀 Transfer Learning

Transfer Learning achieved the strongest overall performance.

It reached:

> 🎯 **88.70% Test Accuracy**
> 📈 **90.05% Validation Accuracy**

Compared with the CNN models trained from scratch, this represents a substantial improvement.

Although Transfer Learning required the **longest training time**, it used only **41,025 trainable parameters**, because the MobileNetV2 base was frozen.

### 💡 Why did it perform better?

Because MobileNetV2 starts with visual features learned from **ImageNet**.

Instead of asking the model to learn basic visual patterns from scratch, we reuse existing knowledge and train a smaller classification head for our target classes.

---

## 🛠️ Tools Used

| 🧰 Tool             | Purpose              |
| ------------------- | -------------------- |
| 🐍 Python           | Programming          |
| 🧠 TensorFlow       | Deep Learning        |
| 🔗 Keras            | Model Development    |
| 🔢 NumPy            | Numerical Operations |
| 📊 Pandas           | Data Handling        |
| 📈 Matplotlib       | Visualization        |
| 📓 Jupyter Notebook | Experimentation      |
| 🚀 MobileNetV2      | Transfer Learning    |
| 🖼️ ImageNet        | Pre-trained Weights  |

---

# 🎉 Final Outcome

This hands-on lab demonstrated the progression from a basic CNN to a more powerful **Transfer Learning** approach.

### 📌 Key Takeaways

> 🧠 **CNN from Scratch** → Established the baseline.
>
> 🔄 **Data Augmentation** → Added image variation but did not improve performance in this experiment.
>
> 🚀 **Transfer Learning** → Achieved the best performance with significantly fewer trainable parameters.

### 🏆 Final Result

**Transfer Learning with MobileNetV2 was the best-performing approach**, achieving:

## 🎯 88.70% Test Accuracy

## 📈 90.05% Validation Accuracy

> 💡 **Main Lesson:** Pre-trained CNN architectures can provide a significant advantage when working with limited image data because they already contain useful visual representations learned from large-scale datasets.

---


### 🧠 Learn → 🛠️ Build → 🧪 Experiment → 📊 Compare → 🚀 Improve

**Week 7 · Day 2 Complete ✅**

