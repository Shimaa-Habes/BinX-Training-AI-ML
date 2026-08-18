# Day 2 — DBSCAN & Hierarchical Clustering

## Overview

This notebook explores clustering methods beyond K-Means, focusing on **DBSCAN** and **Hierarchical Clustering**.

The goal is to understand the limitations of K-Means and learn how alternative clustering methods can handle irregular cluster shapes, noise, outliers, and nested structures.

---

## Learning Objectives

* Explain the limitations of K-Means and when another clustering method is preferred.
* Apply DBSCAN and interpret its clusters and noise points.
* Understand the `eps` and `min_samples` parameters.
* Build and interpret a hierarchical clustering dendrogram.
* Compare K-Means, DBSCAN, and Hierarchical Clustering.
* Select the most suitable clustering method based on the dataset structure.

---

## Key Topics

### 1. Limitations of K-Means

K-Means requires the number of clusters `k` to be specified in advance.

It also works best when clusters are approximately round and similarly sized. Another limitation is that every data point must belong to a cluster, meaning that outliers can be incorrectly assigned to groups.

---

### 2. DBSCAN

**DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** groups points based on their density.

Unlike K-Means:

* It does not require the number of clusters in advance.
* It can identify irregularly shaped clusters.
* It explicitly detects noise and outliers.
* Noise points are assigned the label `-1`.

#### Main Parameters

| Parameter     | Description                                                     |
| ------------- | --------------------------------------------------------------- |
| `eps`         | Maximum distance for points to be considered neighbors          |
| `min_samples` | Minimum number of nearby points required to form a dense region |

---

### 3. Hierarchical Clustering

Hierarchical clustering creates a tree-like structure of clusters.

It starts with each point as an individual cluster and repeatedly merges the closest clusters until all points belong to one cluster.

The resulting structure is visualized using a **dendrogram**.

A horizontal cut through the dendrogram can be used to determine the desired number of clusters.

---

## Choosing the Right Method

| Method           | Best Used When                                     | Main Limitation                                    |
| ---------------- | -------------------------------------------------- | -------------------------------------------------- |
| **K-Means**      | Clusters are round and similarly sized             | Requires `k` and forces every point into a cluster |
| **DBSCAN**       | Data contains noise or irregularly shaped clusters | Sensitive to `eps` and varying densities           |
| **Hierarchical** | Nested structure or dendrogram analysis is useful  | Can be slow for very large datasets                |

---

## Hands-On Lab

The practical section compares three clustering approaches on the same dataset.

### Step 1 — DBSCAN

Run DBSCAN and determine:

* Number of clusters discovered.
* Number of noise/outlier points.
* Distribution of points across clusters.

### Step 2 — Hierarchical Clustering

Build a hierarchical clustering model and visualize its structure using a dendrogram.

Choose an appropriate cut height and determine the resulting number of clusters.

### Step 3 — Method Comparison

Compare the results of:

* K-Means
* DBSCAN
* Hierarchical Clustering

The comparison focuses on cluster structure, number of clusters, and treatment of outliers.

### Step 4 — Final Analysis

Use Markdown to explain which clustering method best fits the dataset and justify the choice based on its shape, density, and presence of noise.

---

## Tools Used

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Scikit-learn
* SciPy
* Matplotlib

---

## Expected Outcomes

By the end of this notebook, we should be able to:

* Identify situations where K-Means is not appropriate.
* Detect noise and irregular clusters using DBSCAN.
* Interpret `eps` and `min_samples`.
* Read a hierarchical clustering dendrogram.
* Compare different clustering algorithms on the same dataset.
* Select the most appropriate clustering method based on the structure of the data.

---

## Conclusion

DBSCAN and Hierarchical Clustering provide useful alternatives to K-Means.

DBSCAN is particularly useful when the dataset contains **noise or irregularly shaped clusters**, while Hierarchical Clustering is valuable when we want to understand the **nested relationships between data points**.

Comparing multiple clustering methods helps determine which algorithm represents the underlying structure of a dataset most effectively.

