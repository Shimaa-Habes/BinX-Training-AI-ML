# 🛍️ Week 5 — Day 1: Unsupervised Learning & K-Means

> **BinX Tech • AI & Machine Learning Internship Program**  
> **Week 5 — Unsupervised Learning**  
> **Day 1 — K-Means Clustering & Choosing k**

---

## 🎯 Overview

Today we started **Unsupervised Learning**, where the data does not have a predefined target label.

Instead of predicting an existing target, the goal is to discover hidden patterns and natural groups within the data.

For this hands-on project, we used the **Mall Customers Dataset** and applied **K-Means Clustering** to identify customer segments based on their characteristics and spending behavior.

---

## 🛍️ Dataset

The dataset used in this project is the **Mall Customers Dataset** from Kaggle.

It contains information about **200 customers** and includes the following features:

| Feature | Description |
|---|---|
| 🆔 `CustomerID` | Unique customer identifier |
| 👤 `Genre` | Customer gender |
| 🎂 `Age` | Customer age |
| 💰 `Annual Income (k$)` | Annual income in thousands of dollars |
| 🛍️ `Spending Score (1-100)` | Customer spending score |

### 🌐 Dataset Source

Kaggle — Mall Customers Dataset

The dataset is publicly available and is used for educational machine learning purposes.

---

## 🧠 Why This Dataset?

The Mall Customers dataset is a good example for unsupervised learning because it does not contain a predefined clustering target.

This allows us to explore whether customers naturally form different groups based on:

- 🎂 Age
- 💰 Annual Income
- 🛍️ Spending Score

The goal is to discover these groups using the characteristics already present in the dataset.

---

## 📚 Learning Objectives

By completing this notebook, we practiced:

- 🧠 Understanding supervised vs. unsupervised learning
- 🔵 Understanding how K-Means clustering works
- 📏 Scaling features before distance-based clustering
- 📉 Choosing `k` using the Elbow Method
- 📐 Evaluating clusters using the Silhouette Score
- 🎨 Visualizing customer clusters
- 🧠 Interpreting the characteristics of discovered clusters

---

## 🔬 Workflow

The notebook follows this workflow:

```text
📥 Load Dataset
      ↓
🔎 Inspect Dataset
      ↓
🎯 Select Clustering Features
      ↓
📏 Scale Features
      ↓
🔵 Apply K-Means
      ↓
📉 Elbow Method
      ↓
📐 Silhouette Score
      ↓
🎯 Select Best k
      ↓
🔵 Train Final K-Means
      ↓
🎨 Visualize Clusters
      ↓
🧠 Interpret Customer Groups
🎯 Features Used for Clustering

The following numerical features were selected:

Age
Annual Income (k$)
Spending Score (1-100)

CustomerID was excluded because it is only an identifier and does not provide meaningful information about customer similarity.

📏 Feature Scaling

Before applying K-Means, the numerical features were standardized using:

StandardScaler()

Scaling is important because K-Means is a distance-based algorithm.

Without scaling, a feature with a larger numerical range could have a greater influence on the clustering process.

🔵 K-Means Clustering

K-Means divides the dataset into a predefined number of clusters.

The algorithm repeatedly:

Selects initial centroids.
Assigns each data point to its nearest centroid.
Calculates new centroid positions.
Repeats the process until the clusters stabilize.

The implementation used:

KMeans(
    n_clusters=k,
    random_state=42,
    n_init=10
)
📉 Elbow Method

The Elbow Method was used to explore different values of k.

For each value of k from 1 to 10, the model calculates inertia, which represents the total distance between data points and their assigned cluster centers.

As the number of clusters increases, inertia decreases.

The goal is to identify an elbow point, where adding more clusters provides only a small improvement.

📐 Silhouette Score

The Silhouette Score was used as an additional quantitative evaluation method.

The score ranges approximately from:

-1 → Poorly separated clusters
 0 → Overlapping clusters
+1 → Well-separated clusters

Higher values generally indicate better-defined clusters.

We calculated the Silhouette Score for multiple candidate values of k and selected the value with the strongest score.

🎨 Cluster Visualization

The final clusters were visualized using:

💰 Annual Income
🛍️ Spending Score

The visualization helps us understand how customers are distributed across the discovered groups.

Cluster centroids were also displayed to show the center of each group.

🧠 Cluster Interpretation

After training the final K-Means model, each customer was assigned a cluster label.

The average values of:

🎂 Age
💰 Annual Income
🛍️ Spending Score

were calculated for every cluster.

This allows us to interpret the characteristics of the discovered customer segments.

The clusters are not predefined labels. They are groups discovered automatically by the clustering algorithm based on similarities in the selected features.

🧪 Hands-On Lab

The required hands-on tasks were completed:

✅ Loaded and inspected the dataset
✅ Selected numerical features
✅ Scaled the features using StandardScaler
✅ Ran K-Means for k = 1 to 10
✅ Used the Elbow Method
✅ Calculated Silhouette Scores
✅ Selected a suitable number of clusters
✅ Trained the final K-Means model
✅ Visualized the resulting clusters
✅ Interpreted the discovered customer groups
🛠️ Technologies Used
🐍 Python
🐼 Pandas
🔢 NumPy
📊 Matplotlib
🤖 Scikit-learn
📓 Jupyter Notebook
📁 Project Structure
Day1/
│
├── kmeans_clustering.ipynb
├── Mall_Customers.csv
└── README.md
🚀 How to Run
1️⃣ Activate the Virtual Environment

On Windows:

.venv\Scripts\activate
2️⃣ Install Required Libraries
pip install numpy pandas matplotlib scikit-learn jupyter
3️⃣ Start Jupyter Notebook
jupyter notebook
4️⃣ Open the Notebook

Open:

kmeans_clustering.ipynb
5️⃣ Run the Notebook

Run the cells from top to bottom.

The notebook should execute the complete workflow without requiring manual hidden steps.

📌 Key Takeaway

Today's main idea was that unsupervised learning does not require predefined labels.

Instead, algorithms such as K-Means can discover natural patterns in data.

In this project, K-Means was used to discover groups of customers with similar characteristics based on age, annual income, and spending score.

⚠️ Note

This project is created for educational purposes as part of the BinX Tech AI & Machine Learning Internship Program.

The discovered customer segments are algorithmic groupings and should not automatically be interpreted as definitive real-world customer categories.

✅ Day 1 Status

Completed 🎉

🧠 Unsupervised Learning concepts
🔵 K-Means Clustering
📉 Elbow Method
📐 Silhouette Score
📏 Feature Scaling
🎨 Cluster Visualization
🧠 Cluster Interpretation
🧪 Hands-On Lab
📋 Documentation