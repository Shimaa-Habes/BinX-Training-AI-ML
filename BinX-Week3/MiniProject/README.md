# 🤖 BinX Tech AI & Machine Learning Internship Program

# Week 3 — Supervised Learning

## Regression & Classification with Scikit-learn

---

## 📌 Week Overview

Week 3 is the first week of Phase 2: Core Machine Learning Training.

During this week, we built our first real machine learning models using the Scikit-learn library.

The main focus was supervised learning, where models learn from labeled data to predict future outcomes.

The week covered:

- Regression models for predicting continuous values.
- Classification models for predicting categories.
- Model evaluation and comparison.
- Building a complete machine learning pipeline.

---

# 🎯 Learning Objectives

By the end of Week 3, we learned how to:

- Understand supervised learning concepts.
- Differentiate between regression and classification.
- Split datasets into features (X) and target (y).
- Apply train/test splitting correctly.
- Train and evaluate machine learning models.
- Interpret regression coefficients.
- Use classification metrics.
- Compare multiple machine learning algorithms.
- Build an end-to-end supervised learning project.

---

# 🧠 Supervised Learning

Supervised learning trains models using labeled examples.

Each training sample contains:

- Input features (X)
- Correct output label (y)

The model learns the relationship between X and y, then uses this knowledge to predict new unseen data.

---

# 🔀 Regression vs Classification

## Regression

Regression predicts continuous numerical values.

Examples:

- House prices
- Temperature
- Income prediction

Common metrics:

- MAE
- RMSE
- R²

---

## Classification

Classification predicts categories or classes.

Examples:

- Spam / Not Spam
- Disease prediction
- Customer churn

Common metrics:

- Accuracy
- Precision
- Recall
- F1-score
- AUC-ROC

---

# 🗓️ Week 3 Schedule

| Day   | Topic                                           |
| ----- | ----------------------------------------------- |
| Day 1 | Supervised Learning Concepts & Scikit-learn API |
| Day 2 | Linear Regression                               |
| Day 3 | Logistic Regression & Classification Metrics    |
| Day 4 | Decision Trees, Random Forests, SVM & k-NN      |
| Day 5 | Supervised Learning Mini-Project                |

---

# 📘 Day 1 — Supervised Learning Concepts

## Topics Covered

- What supervised learning is.
- Regression vs classification.
- Features and target separation.
- Scikit-learn workflow.
- Train/test split.

---

## Scikit-learn API

All models follow the same workflow:

```python
model = Model()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

model.score(X_test, y_test)
```

---

## Train/Test Split

The dataset is divided into:

### Training Data

Used for learning patterns.

### Testing Data

Used for evaluating performance on unseen data.

This prevents misleading results and provides a realistic evaluation.

---

# 📘 Day 2 — Linear Regression

## Topics Covered

- Linear regression concept.
- Training regression models.
- Making predictions.
- Understanding coefficients.
- Regression evaluation metrics.

---

## Linear Regression

Linear Regression predicts continuous values by finding the best relationship between features and target.

Example:

Predicting house prices based on features.

---

## Regression Metrics

### MAE

Average prediction error.

### RMSE

Penalizes large errors more strongly.

### R² Score

Measures how well the model explains data variation.

---

# 📘 Day 3 — Logistic Regression & Classification

## Topics Covered

- Logistic Regression.
- Class probabilities.
- Confusion matrix.
- Classification metrics.

---

## Logistic Regression

Although it contains "Regression" in its name, Logistic Regression is a classification algorithm.

It predicts class probabilities and assigns categories based on a threshold.

---

## Classification Metrics

### Accuracy

Percentage of correct predictions.

### Precision

How many predicted positives are actually positive.

### Recall

How many actual positives were detected.

### F1-score

Balance between precision and recall.

---

## Confusion Matrix

Shows:

- True Positive
- True Negative
- False Positive
- False Negative

It helps understand model mistakes.

---

# 📘 Day 4 — Trees, Forests, SVM & k-NN

## Topics Covered

- Decision Trees.
- Random Forests.
- Support Vector Machines.
- k-Nearest Neighbors.
- Model comparison.

---

# 🌳 Decision Tree

A decision tree learns rules by splitting data based on features.

Advantages:

- Easy to understand.
- Interpretable decisions.

Disadvantage:

- Can overfit.

---

# 🌲 Random Forest

Random Forest combines multiple decision trees.

Advantages:

- Better generalization.
- Reduces overfitting.
- Provides feature importance.

---

# 📈 Support Vector Machine (SVM)

SVM finds the best decision boundary between classes.

Advantages:

- Powerful for high-dimensional data.

---

# 👥 k-Nearest Neighbors (k-NN)

k-NN predicts classes based on the closest training examples.

Advantages:

- Simple and intuitive.

Disadvantage:

- Slower with large datasets.

---

# 📊 Model Comparison

Different models were trained using the same dataset split.

Models compared:

- Decision Tree
- Random Forest
- SVM
- k-NN

The best model was selected based on evaluation metrics.

---

# 📘 Day 5 — Supervised Learning Mini-Project

## Project Goal

Build a complete machine learning pipeline:

```
EDA
↓
Preprocessing
↓
Train/Test Split
↓
Model Training
↓
Evaluation
↓
Model Selection
```

---

## Project Steps

### 1. Dataset Understanding

- Load dataset.
- Explore features.
- Perform EDA.

### 2. Data Preprocessing

Including:

- Handling missing values.
- Encoding categorical features.
- Feature scaling.

### 3. Model Training

Train multiple suitable models.

### 4. Evaluation

Compare models using proper metrics.

### 5. Final Selection

Choose the best model and document the results.

---

# 🛠️ Technical Stack

## Machine Learning

- Scikit-learn

Models:

- LinearRegression
- LogisticRegression
- DecisionTreeClassifier
- RandomForestClassifier
- SVC
- KNeighborsClassifier

---

## Data Processing

- Pandas
- NumPy

---

## Visualization

- Matplotlib
- Seaborn

---

## Environment

- Python 3.10+
- Jupyter Notebook
- Git & GitHub

---

# 📂 Week 3 Deliverables

Completed:

✅ Supervised learning workflow notebook  
✅ Linear regression notebook  
✅ Logistic regression notebook  
✅ Classification metrics analysis  
✅ Model comparison notebook  
✅ End-to-end ML mini-project  
✅ GitHub documentation

---

# ⭐ Best Practices Learned

During Week 3, we focused on:

- Always separating training and testing data.
- Never evaluating on training data.
- Comparing models fairly.
- Choosing metrics based on the problem.
- Avoiding data leakage.
- Writing clear notebook explanations.

---

# ✅ Conclusion

Week 3 introduced the first real machine learning models.

Through regression, classification, model comparison, and the final mini-project, we built a strong foundation in supervised learning using Scikit-learn.

The skills learned in this week prepare the foundation for future machine learning projects and advanced pipelines.
