# 🧠 Hands-On Lab: Activations & the Forward Pass

## 📌 Overview

This hands-on lab applies the neural network concepts covered in Day 2 using Python and NumPy.

The lab focuses on:

* Visualizing common activation functions.
* Selecting the correct output activation and loss function for the **CardioML** Phase 3 project.
* Computing a forward pass through a small 2-layer neural network.
* Documenting the activation, loss, and forward-pass results.

---

## 🎯 Learning Objectives

By completing this lab, we will:

1. Understand how ReLU, Sigmoid, and Tanh transform input values.
2. Understand why Sigmoid and Binary Cross-Entropy are appropriate for binary classification.
3. Follow the calculations of a forward pass through a neural network.
4. Interpret the final prediction produced by the output layer.

---

## 🧪 Lab Steps

### Step 1 — Plot Activation Functions

Plot **ReLU**, **Sigmoid**, and **Tanh** over a range of input values.

The goal is to visually compare how each activation function transforms its input.

**Activation functions:**

* **ReLU:** outputs `0` for negative values and keeps positive values unchanged.
* **Sigmoid:** maps values to the range `[0, 1]`.
* **Tanh:** maps values to the range `[-1, 1]`.

---

### Step 2 — Choose the Output Activation & Loss Function

The **CardioML** project is a binary classification task:

* `0` → No cardiovascular disease
* `1` → Cardiovascular disease

Therefore, the selected components are:

| Component         | Choice                | Reason                                                         |
| ----------------- | --------------------- | -------------------------------------------------------------- |
| Task              | Binary Classification | The target has two classes                                     |
| Hidden Activation | ReLU                  | Introduces non-linearity and is commonly used in hidden layers |
| Output Activation | Sigmoid               | Produces a probability between 0 and 1                         |
| Loss Function     | Binary Cross-Entropy  | Designed for binary classification                             |

**Sigmoid** is appropriate for the output layer because it converts the network's raw output into a probability between 0 and 1.

**Binary Cross-Entropy (BCE)** is appropriate because it measures the difference between the predicted probability and the actual binary label.

---

### Step 3 — Compute a Forward Pass

A tiny 2-layer neural network is used to demonstrate how an input moves through the network:

```text
Input Features
      ↓
Hidden Layer
      ↓
    ReLU
      ↓
Output Layer
      ↓
   Sigmoid
      ↓
 Prediction
```

The sample input is:

```text
x = [2.0, 1.0]
```

The forward pass is calculated using NumPy.

The intermediate results are:

```text
Hidden Layer Weighted Sum:
[2.5, -0.5]

After ReLU:
[2.5, 0.0]

Output Layer Weighted Sum:
3.0

Final Sigmoid Prediction:
≈ 0.953
```

The final prediction of approximately **0.953** represents a high probability for the positive class.

---

### Step 4 — Document the Choices & Results

The final documentation records the activation choices, loss function, and forward-pass results.

### Final Model Choices

```text
Task              → Binary Classification
Hidden Activation → ReLU
Output Activation → Sigmoid
Loss Function     → Binary Cross-Entropy
```

### Forward-Pass Summary

For the sample input `[2.0, 1.0]`:

```text
Input
  ↓
[2.0, 1.0]
  ↓
Weighted Sum
  ↓
[2.5, -0.5]
  ↓
ReLU
  ↓
[2.5, 0.0]
  ↓
Output Weighted Sum
  ↓
3.0
  ↓
Sigmoid
  ↓
0.953
```

The forward pass demonstrates how raw input features are transformed through neural network layers and activation functions to produce a final probability.

---

## 🛠️ Technologies Used

* Python
* NumPy
* Matplotlib
* Jupyter Notebook

---

## 📁 Notebook

The implementation is contained in:

```text
hands_on_lab.ipynb
```

---

## ✅ Lab Completion

* [x] Plot ReLU, Sigmoid, and Tanh
* [x] Choose the correct output activation
* [x] Choose the correct loss function
* [x] Justify the activation and loss choices
* [x] Compute a forward pass using NumPy
* [x] Document the forward-pass result
