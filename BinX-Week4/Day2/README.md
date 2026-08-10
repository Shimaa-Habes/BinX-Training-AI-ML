# 🔄 AI & ML Course with BinX — Week 4 — Day 2

## Cross-Validation

### 📌 Overview

This notebook focuses on **Cross-Validation**, a model evaluation technique used to obtain a more reliable estimate of machine learning performance.

Instead of depending on a single train/test split, Cross-Validation evaluates the model across multiple folds and summarizes its performance using the **mean** and **standard deviation**.

---

## 🎯 Learning Objectives

By the end of this notebook, I learned how to:

* Explain how **k-Fold Cross-Validation** works.
* Use `cross_val_score` to evaluate a classification model.
* Interpret the **mean** and **standard deviation** of cross-validation scores.
* Understand why **Stratified k-Fold** is important for imbalanced classification.
* Compare Cross-Validation performance with a single train/test split.
* Evaluate model stability across different folds.

---

## 🏦 Dataset

### Bank Marketing Campaigns Dataset

The dataset contains information about marketing campaigns conducted by a Portuguese bank.

The classification goal is to predict whether a client subscribed to a **term deposit**.

### Target Variable

* `y` → Whether the client subscribed to a term deposit (`yes` / `no`).

### Dataset Characteristics

* **41,188 instances**
* **21 columns**
* Numerical and categorical features
* Binary classification problem
* Imbalanced target classes

The dataset is based on the **UCI Bank Marketing Dataset** and includes additional social and economic context features.

---

## 🌳 Model Used

For this notebook, I used the:

**Decision Tree Classifier**

```python
DecisionTreeClassifier(random_state=42)
```

The model was evaluated using the **F1-score**, which is particularly useful for classification problems where class imbalance exists.

---

## 🔄 5-Fold Cross-Validation

In 5-Fold Cross-Validation, the training data is divided into five folds.

The model is trained five times. During each round:

* Four folds are used for training.
* One fold is used for validation.
* A different fold is used for validation in each round.

This allows every observation to be used for validation exactly once.

---

## 📊 Cross-Validation Results

The initial 5-fold Cross-Validation produced the following F1-scores:

| Fold   | F1-score |
| ------ | -------- |
| Fold 1 | 0.3073   |
| Fold 2 | 0.3013   |
| Fold 3 | 0.3261   |
| Fold 4 | 0.3247   |
| Fold 5 | 0.3074   |

### Summary

* **Mean F1-score:** `0.3134`
* **Standard Deviation:** `0.0101`

The relatively low standard deviation indicates that the model's performance was fairly consistent across the folds.

---

## 🔍 Single Split vs. Cross-Validation

The original single train/test split produced:

**Single-Split F1-score:** `0.3311`

Compared with:

**5-Fold CV Mean F1-score:** `0.3134`

The difference was:

**`0.0177`**

The single-split score was slightly higher, showing that the particular test split was somewhat more favorable to the model than the average cross-validation fold.

Cross-Validation provides a broader and more reliable estimate because it evaluates the model across multiple data splits.

---

## ⚖️ Stratified k-Fold

Because this is a classification problem with imbalanced target classes, **StratifiedKFold** is important.

Stratification preserves approximately the same class distribution in every fold.

```python
StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
```

This helps ensure that the model is evaluated fairly across different validation folds.

### Stratified Results

| Fold   | F1-score |
| ------ | -------- |
| Fold 1 | 0.3127   |
| Fold 2 | 0.3122   |
| Fold 3 | 0.3098   |
| Fold 4 | 0.3286   |
| Fold 5 | 0.3390   |

### Summary

* **Mean F1-score:** `0.3205`
* **Standard Deviation:** `0.0114`

The results remained relatively consistent across the stratified folds.

---

## 🧪 Hands-On Lab

During the practical lab, I:

* ✅ Applied 5-Fold Cross-Validation.
* ✅ Calculated the F1-score for each fold.
* ✅ Calculated the mean and standard deviation.
* ✅ Compared Cross-Validation with a single train/test split.
* ✅ Created and used `StratifiedKFold`.
* ✅ Explained why stratification matters for imbalanced classification.
* ✅ Evaluated model stability across different folds.

---

## 🛠️ Tools & Libraries

* Python
* Pandas
* Scikit-learn
* Jupyter Notebook
* Git & GitHub

### Scikit-learn Components

* `DecisionTreeClassifier`
* `cross_val_score`
* `StratifiedKFold`
* `f1_score`

---

## 💡 Key Takeaways

> Cross-Validation gives a more reliable estimate of model performance than relying on a single data split.

> The **mean** represents the average performance across folds, while the **standard deviation** indicates how much that performance varies.

> For imbalanced classification problems, **StratifiedKFold** helps maintain similar class proportions across validation folds.

> A stable model is not necessarily a high-performing model. Both **performance** and **stability** should be considered when evaluating a classifier.

---

## 🚀 Conclusion

In this notebook, I explored how Cross-Validation can provide a more reliable view of machine learning model performance.

Using the Bank Marketing dataset and a Decision Tree Classifier, I evaluated the model with 5-Fold Cross-Validation, compared it with a single train/test split, and applied StratifiedKFold to preserve class distribution across folds.

**Cross-Validation Completed ✅**
