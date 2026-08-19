# 🧪 Day 4 — t-SNE & Anomaly Detection

## 📌 Overview

This project explores dimensionality reduction and anomaly detection using a Credit Card Fraud Detection dataset.

The main goal is to visualize hidden patterns in high-dimensional transaction data using **t-SNE**, compare it with **PCA**, and detect unusual transactions using **Isolation Forest**.

---

## 🎯 Learning Objectives

- Apply t-SNE to high-dimensional data.
- Understand the difference between PCA and t-SNE.
- Visualize transaction patterns in 2D.
- Understand anomaly detection and why it is often unsupervised.
- Apply Isolation Forest to detect unusual observations.
- Inspect and interpret detected anomalies.

---

## 📊 Dataset

The project uses the **Credit Card Fraud Detection** dataset.

The dataset contains credit card transactions labeled as either legitimate or fraudulent.

### Dataset Features

| Feature | Description |
|---|---|
| `Time` | Seconds elapsed between transactions |
| `V1–V28` | Anonymized numerical features |
| `Amount` | Transaction amount |
| `Class` | Target variable: `0 = Genuine`, `1 = Fraud` |

The original dataset contains **284,807 transactions** and **30 features** including the target variable.

Because t-SNE can be computationally expensive on large datasets, a sample of **10,000 transactions** was used for the visualization and lab exercises.

---

## 🌀 t-SNE

**t-SNE (t-distributed Stochastic Neighbor Embedding)** is a dimensionality reduction technique mainly designed for visualization.

It focuses on preserving **local neighborhoods**, making it useful for discovering visually similar groups in high-dimensional data.

In this project, t-SNE was configured with:

- `n_components = 2`
- `perplexity = 30`
- `random_state = 42`

---

## ⚖️ PCA vs. t-SNE

PCA and t-SNE both reduce dimensionality, but they focus on different types of structure.

| PCA | t-SNE |
|---|---|
| Preserves global variance | Preserves local neighborhoods |
| Fast and efficient | More computationally expensive |
| Components have interpretable directions | Axes have no direct meaning |
| Useful for compression and modeling | Mainly used for visualization |

---

## 🚨 Anomaly Detection

Anomaly detection identifies observations that differ significantly from the normal patterns in a dataset.

It is often unsupervised because unusual observations are usually rare and may not have predefined labels.

Examples include:

- 💳 Fraudulent transactions
- 🏥 Unusual patient records
- 🖥️ System failures
- 🏭 Defective products

---

## 🌲 Isolation Forest

Isolation Forest is an anomaly detection algorithm based on the idea that unusual observations are easier to isolate than normal observations.

The model was configured with:

```python
IsolationForest(
    contamination=0.05,
    random_state=42
)

The `contamination` parameter represents the estimated proportion of observations expected to be anomalies.

For the 10,000 sampled transactions:

- **9,500** observations were classified as normal.
- **500** observations were classified as anomalies.
- **5%** of the sample was flagged as anomalous.

Isolation Forest predictions use:

- `1` → Normal observation
- `-1` → Anomaly

---

## 🔎 Anomaly Inspection

Two flagged observations were inspected.

### Observation 1

The first observation was labeled:

`Class = 1 → Fraud`

It contained several relatively extreme values across the anonymized features, making it different from the majority of transactions.

### Observation 2

The second observation was labeled:

`Class = 0 → Genuine`

Although it was legitimate, its combination of feature values was unusual enough for Isolation Forest to flag it as an anomaly.

This demonstrates that **anomaly detection does not directly mean fraud detection**. An unusual transaction can still be genuine.

---

## 🧪 Hands-On Lab

The practical lab followed four main steps:

### Step 1 — t-SNE

Reduced the high-dimensional transaction data to two dimensions and created a 2D visualization.

### Step 2 — PCA vs. t-SNE

Applied PCA to the same sample and compared its visualization with the t-SNE representation.

### Step 3 — Isolation Forest

Applied Isolation Forest and detected:

**500 anomalies**

### Step 4 — Inspect Anomalies

Inspected two flagged observations and analyzed why their feature patterns may have caused them to be identified as unusual.

---

## 🛠️ Tools Used

- Python
- Pandas
- Scikit-learn
  - `TSNE`
  - `PCA`
  - `IsolationForest`
- Matplotlib
- Jupyter Notebook
- VS Code

---

## 📁 Project Structure

```text
Week4/
└── Day4/
    ├── tsne_anomaly_detection.ipynb
    ├── hands_on_lab.ipynb
    └── README.md

    ## 💡 Key Takeaways

- t-SNE is mainly used to visualize local structure in high-dimensional data.
- PCA focuses on global variance, while t-SNE focuses on local neighborhoods.
- Isolation Forest can identify unusual observations without using class labels.
- Anomalies are not necessarily fraudulent transactions.
- Combining visualization and anomaly detection provides a better understanding of complex datasets.

---

## ⚠️ Note

This project is part of an educational AI & Machine Learning training program and is intended for learning and experimentation.