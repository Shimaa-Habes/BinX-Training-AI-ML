# 🎗️ Week 4 — Day 3
## Bias-Variance & Diagnosing Model Fit

<div align="center">

### 🧠 Understanding When a Machine Learning Model Learns Too Little or Too Much

**Diagnosing Underfitting • Overfitting • Bias-Variance Trade-off • Regularization**

</div>

---

## 🎗️ About This Day

Day 3 focuses on one of the most important skills in Machine Learning: **understanding how well a model is learning from data**.

Instead of only looking at the final accuracy, we analyze the difference between **training and validation performance** to determine whether a model is:

- 📉 **Underfitting** — too simple to capture important patterns
- 📈 **Overfitting** — too complex and memorizing the training data
- ⚖️ **Well-fitted** — learning useful patterns while generalizing to unseen data

The practical work uses the **Breast Cancer Wisconsin (Diagnostic)** dataset to make these concepts easier to observe through real classification results.

---

## 🎗️ Dataset — Breast Cancer Wisconsin (Diagnostic)

The dataset contains measurements computed from digital images of breast mass biopsy samples.

Each sample contains **30 numerical features** describing characteristics of cell nuclei, including:

- Radius
- Texture
- Perimeter
- Area
- Smoothness
- Compactness
- Concavity
- Symmetry
- Fractal dimension

The target is a binary classification:

| Target | Meaning |
|:---:|---|
| `0` | Malignant |
| `1` | Benign |

### ⭐ Why This Dataset?

This dataset is particularly useful for this lesson because it is:

- 📊 **Small and manageable** — 569 samples and 30 features
- 🎯 **Binary classification** — makes model evaluation straightforward
- 🧹 **Clean and structured** — keeps the focus on model behavior rather than data cleaning
- 📐 **Feature-rich** — provides enough information for models to learn complex patterns
- ⚡ **Fast to train** — allows multiple experiments without long waiting times

---

## 📚 Learning Objectives

By the end of this day, I should be able to:

- Distinguish **underfitting** from **overfitting**
- Explain the **bias-variance trade-off**
- Diagnose model fit using the **train-validation gap**
- Understand how model complexity affects generalization
- Apply **regularization** to control model complexity
- Compare **Ridge (L2)** and **Lasso (L1)** regularization
- Use score evidence to justify a model-fit diagnosis

---

## ⚖️ Topics Covered

### 3.1 — The Two Ways a Model Fails

Understanding the symptoms, causes, and fixes of:

- Underfitting
- Overfitting

### 3.2 — The Bias-Variance Trade-off

Exploring how:

> **Higher model complexity → Lower Bias + Higher Variance**

and why the goal is to find a balance between the two.

### 3.3 — Diagnosing With the Train-Validation Gap

Using the difference between training and validation scores as a practical diagnostic tool.

### 3.4 — Regularization

Exploring two common regularization techniques:

- 🛡️ **Ridge — L2 Regularization**
- 🛡️ **Lasso — L1 Regularization**

The `alpha` parameter controls the strength of the regularization penalty.

---

## 🧪 Hands-On Lab

The practical experiment follows four steps:

### Step 1 — Deliberately Overfit

A highly complex Decision Tree is trained to demonstrate a large train-validation gap.

**Observed result:**

- Training Accuracy: **100%**
- Validation Accuracy: **91.23%**
- Gap: **8.77%**

This indicates that the model learned the training data too closely.

---

### Step 2 — Deliberately Underfit

A very simple Decision Tree is used to investigate the opposite behavior.

**Observed result:**

- Training Accuracy: **92.31%**
- Validation Accuracy: **92.11%**
- Gap: **0.20%**

The extremely small gap shows stable generalization, although the scores are still relatively high, so the experiment does not demonstrate strong underfitting.

---

### Step 3 — Reduce Model Complexity

The overfitted model is simplified to reduce its tendency to memorize the training data.

**Before:**

> Gap = **8.77%**

**After:**

> Gap = **7.24%**

The smaller gap indicates a modest improvement in generalization, although some overfitting remains.

---

### Step 4 — Document the Diagnosis

Each experiment is documented using:

- Training Accuracy
- Validation Accuracy
- Train-Validation Gap
- Diagnosis
- Applied Fix
- Final Interpretation

This makes the model-fit decision **evidence-based rather than based only on the final accuracy**.

---

## 🛠️ Tools & Libraries

```text
Python
Scikit-learn
Pandas
Matplotlib
Jupyter Notebook
