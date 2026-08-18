# 📉 PCA Dimensionality Reduction — Fashion-MNIST

## 📌 Overview

This project explores **Principal Component Analysis (PCA)** for dimensionality reduction using the **Fashion-MNIST** dataset.

The goal is to reduce the number of features while preserving as much information as possible, and to visualize the high-dimensional dataset in 2D.

---

## 🎯 Objectives

* Understand the **curse of dimensionality**.
* Apply feature scaling using `StandardScaler`.
* Apply **PCA** to a high-dimensional dataset.
* Analyze the **explained variance ratio**.
* Determine how many components are needed to retain approximately **95% variance**.
* Reduce the dataset to **2 components** for visualization.
* Understand the trade-off between dimensionality reduction and information loss.

---

## 👕 Dataset — Fashion-MNIST

Fashion-MNIST is a dataset of **70,000 grayscale fashion images**.

Each image has a resolution of:

**28 × 28 pixels = 784 features**

The dataset contains **10 classes**:

| Label | Class         |
| ----: | ------------- |
|     0 | T-shirt / Top |
|     1 | Trouser       |
|     2 | Pullover      |
|     3 | Dress         |
|     4 | Coat          |
|     5 | Sandal        |
|     6 | Shirt         |
|     7 | Sneaker       |
|     8 | Bag           |
|     9 | Ankle Boot    |

Each pixel contains a value representing the intensity of that pixel.

---

## 🧠 Why PCA?

Working with 784 features can make the dataset high-dimensional and harder to visualize.

PCA creates new features called **Principal Components** that capture the directions of greatest variance in the data.

Instead of working with all original features, we can keep a smaller number of components while preserving most of the dataset's information.

---

## 🔄 Workflow

The notebook follows these main steps:

1. Load the Fashion-MNIST dataset.
2. Separate features and labels.
3. Scale the features using `StandardScaler`.
4. Apply PCA.
5. Calculate the explained variance ratio.
6. Plot cumulative explained variance.
7. Find the number of components required for approximately 95% variance.
8. Reduce the dataset to 2 components.
9. Visualize the data using a 2D scatter plot.
10. Analyze the results and trade-offs.

---

## 📊 Results

The original dataset contains:

**784 features**

PCA showed that:

**256 components** are required to retain approximately:

**95.02% of the total variance**

This means the dimensionality can be reduced from **784 → 256 features** while preserving most of the information.

For visualization, the data was further reduced to **2 principal components** and displayed using a 2D scatter plot.

---

## ⚖️ Trade-offs

### What PCA Preserved

Using 256 components retained approximately **95.02% of the variance**, meaning that most of the important variation in the original dataset was preserved.

### What PCA Cost

The new principal components are combinations of the original pixel features, so they are less directly interpretable than the original pixels.

Reducing the data to only 2 components also causes a larger loss of information, but it makes visualization possible.

---

## 🛠️ Tools Used

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Scikit-learn

  * `StandardScaler`
  * `PCA`
* Matplotlib

---

## 📁 Project Structure

```text
Day3/
│
├── pca_fashion_mnist.ipynb
└── README.md
```

---

## 📚 Key Takeaway

PCA is useful for reducing high-dimensional data while retaining important information.

In this project, PCA reduced the Fashion-MNIST dataset from **784 original features to 256 components**, preserving approximately **95.02% of the variance**.

Reducing the data to **2 components** also allowed the high-dimensional Fashion-MNIST dataset to be visualized in a 2D space.
