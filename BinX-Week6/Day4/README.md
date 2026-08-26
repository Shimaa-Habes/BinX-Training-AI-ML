# 🧪 Week 6 — Day 4

## Hands-On Lab: Training a Neural Network

> **BinX Tech — AI & Machine Learning Internship Program**
> **Week 6: Deep Learning | Sprint 1**

---

## 📌 Overview

This hands-on lab applies the neural network concepts covered in **Week 6, Day 4** using **TensorFlow / Keras**.

The goal is to build, train, evaluate, and improve a neural network for the **CardioML binary classification task** using the cardiovascular disease dataset.

The lab follows a complete deep learning workflow:

**Build → Compile → Train → Diagnose → Improve → Evaluate**

---

## 🎯 Learning Objectives

By completing this lab, I was able to:

* Build a neural network using the Keras Sequential API.
* Select the correct output activation and loss function for binary classification.
* Compile a model using the Adam optimizer.
* Train a neural network with validation data.
* Read and interpret the Keras training history.
* Compare training and validation performance.
* Diagnose overfitting and underfitting.
* Apply Dropout and Batch Normalization.
* Evaluate the final model on unseen test data.
* Compare the neural network with the Day 1 baseline.

---

## 📊 Dataset

The lab uses the **Cardiovascular Disease Dataset**.

| Property           | Value                 |
| ------------------ | --------------------- |
| **Records**        | 70,000                |
| **Input Features** | 12                    |
| **Target**         | `cardio`              |
| **Task**           | Binary Classification |
| **Classes**        | `0` and `1`           |

The dataset is loaded using:

```python
df = pd.read_csv("../Day1/heart_disease_uci.csv", sep=";")
```

The target variable is:

```text
0 → No cardiovascular disease
1 → Cardiovascular disease
```

The features are split into training and test sets using a stratified split and standardized before being passed to the neural network.

---

# 🧩 Lab Steps

## Step 1 — Build a Keras Sequential Network

A simple Sequential neural network is created for the CardioML binary classification task.

The baseline architecture is:

```text
Input
  ↓
Dense(64, ReLU)
  ↓
Dense(32, ReLU)
  ↓
Dense(1, Sigmoid)
  ↓
Prediction
```

The hidden layers use **ReLU** to learn non-linear patterns.

The output layer uses **Sigmoid** because the target contains two classes and the model needs to produce a probability between 0 and 1.

---

## Step 2 — Compile and Train

The model is compiled using:

```python
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)
```

### Training Configuration

* **Optimizer:** Adam
* **Loss:** Binary Cross-Entropy
* **Metric:** Accuracy
* **Validation Split:** 20%
* **Epochs:** 50
* **Batch Size:** 32

The validation split allows the model's performance on unseen validation samples to be monitored during training.

---

## Step 3 — Training and Validation Analysis

The Keras `history` object records the model's performance after every epoch.

The following values are available:

```text
loss
accuracy
val_loss
val_accuracy
```

These values are plotted to compare training and validation behavior.

### Fit Diagnosis

The curves are used to determine whether the model is:

* **Underfitting:** Both training and validation performance remain poor.
* **Overfitting:** Training performance continues improving while validation performance gets worse.
* **Good Fit:** Training and validation performance improve together and remain reasonably close.

The curves provide a visual way to understand how well the network is learning and generalizing.

---

## Step 4 — Add Regularization

The baseline network is improved using:

### Batch Normalization

Batch Normalization helps stabilize the values flowing through the network during training and can make optimization smoother and more stable.

### Dropout

Dropout randomly disables a percentage of neurons during training.

In this lab, a dropout rate of:

```text
0.30
```

is used.

Dropout acts as a regularization technique and helps reduce overfitting by preventing the network from relying too heavily on specific neurons.

The improved model is retrained and its loss curves are compared with the baseline model.

---

## Step 5 — Final Evaluation

After training, the final model is evaluated on the unseen test set:

```python
model.evaluate(X_test, y_test)
```

The final test accuracy is then compared with the **Day 1 baseline accuracy of 71.3%**.

### Final Comparison

| Model                    |             Accuracy |
| ------------------------ | -------------------: |
| **Day 1 Baseline**       |            **71.3%** |
| **Day 4 Neural Network** |   **To be measured** |
| **Difference**           | **To be calculated** |

The neural network is considered an improvement only if its final test performance exceeds the Day 1 baseline.

---

# 💡 Key Takeaways

* Keras simplifies neural network development by handling the training mathematics automatically.
* The Sequential API is useful for stacking layers in a simple ordered architecture.
* Sigmoid is appropriate for the binary classification output.
* Binary Cross-Entropy is suitable for measuring error in binary classification.
* The training history is essential for understanding model behavior.
* Validation curves help identify overfitting and underfitting.
* Batch Normalization can stabilize and improve training.
* Dropout provides regularization and can improve generalization.
* Final evaluation must be performed on unseen test data.
* The Day 1 baseline provides a benchmark for measuring whether the neural network improves performance.

---

## 🛠️ Tools Used

* Python
* Pandas
* NumPy
* Scikit-learn
* TensorFlow
* Keras
* Matplotlib
* Jupyter Notebook
* VS Code
* Git & GitHub

---

## 📁 Files

```text
Day4/
├── README.md
├── keras_training.ipynb
└── hands_on_lab.ipynb
```

---

## ✅ Lab Checklist

* [x] Build a Keras Sequential network.
* [x] Use Sigmoid for the binary classification output.
* [x] Compile with Adam and Binary Cross-Entropy.
* [x] Train with a validation split for at least 30 epochs.
* [x] Plot training and validation loss.
* [x] Plot training and validation accuracy.
* [x] Diagnose the model fit.
* [x] Add Batch Normalization and Dropout.
* [x] Retrain and compare the models.
* [x] Evaluate on the test set.
* [x] Compare the final neural network accuracy with the 71.3% Day 1 baseline.

---

## 🚀 Final Outcome

This lab demonstrates the complete process of building and improving a neural network for the CardioML project, from defining the architecture to evaluating its performance on unseen cardiovascular disease data.
