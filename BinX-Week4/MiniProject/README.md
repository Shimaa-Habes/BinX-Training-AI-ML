# 🧠 BinX Tech • AI & Machine Learning Internship
## WEEK 4 — Evaluation, Tuning & Pipelines

> **Cross-Validation • Bias-Variance • Feature Engineering • GridSearchCV • Scikit-learn Pipelines**

---

## 📌 Week Overview

Week 4 focused on moving from simply building models to building **trustworthy, reliable, and reproducible machine learning workflows**.

Throughout the week, I worked on model evaluation, cross-validation, diagnosing overfitting and underfitting, feature engineering, hyperparameter tuning, and finally building an end-to-end Scikit-learn Pipeline that combines preprocessing and modeling without data leakage.

### 🎯 Main Goal

Build models that are not only accurate, but also:

- Reliable
- Generalizable
- Properly evaluated
- Tuned systematically
- Protected against data leakage
- Reproducible and ready for real-world workflows

---

## 🗂️ Week Structure

| Day | Topic | Dataset | Notebook |
|---|---|---|---|
| 🟦 Day 1 | Train / Validation / Test Splits | Titanic | `train_validation_test_splits.ipynb` |
| 🟩 Day 2 | Cross-Validation | Bank Marketing | `cross_validation.ipynb` |
| 🟨 Day 3 | Bias-Variance & Model Diagnosis | BRCA | `bias_variance_diagnosis.ipynb` |
| 🟧 Day 4 | Feature Engineering & Hyperparameter Tuning | Video Games | `feature_engineering_tuning.ipynb` |
| 🟥 Day 5 | Scikit-learn Pipelines & Tuned Mini-Project | Hotel Booking | `tuned_pipeline_mini_project.ipynb` |

---

# 🟦 Day 1 — Train / Validation / Test Splits

### 📂 Dataset
**Titanic Dataset**

### 📓 Notebook
`train_validation_test_splits.ipynb`

### 🎯 Focus

The first day focused on understanding why a single train/test split is not always enough for model development.

I learned how to divide data into:

- Training Set → used to learn model parameters
- Validation Set → used during development and tuning
- Test Set → used only for the final evaluation

### 🔑 Key Concepts

- Train / Validation / Test split
- Data leakage
- Model tuning
- Generalization
- Hold-out test set
- `train_test_split`

### 🧪 Hands-On Work

The lab included:

1. Creating a three-way split.
2. Training a model using the training data.
3. Using the validation set for model decisions.
4. Evaluating the final model on the held-out test set.
5. Understanding why repeatedly checking the test set can lead to misleading performance estimates.

### 💡 Main Takeaway

> The test set should remain untouched during development and should only be used once the modeling decisions are finalized.

---

# 🟩 Day 2 — Cross-Validation

### 📂 Dataset
**Bank Marketing Dataset**

### 📓 Notebook
`cross_validation.ipynb`

### 🎯 Focus

Day 2 introduced **cross-validation** as a more reliable alternative to relying on a single validation split.

### 🔑 Key Concepts

- K-Fold Cross-Validation
- 5-Fold Cross-Validation
- Stratified K-Fold
- `cross_val_score`
- Mean CV score
- Standard deviation
- Model stability

### 🧪 Hands-On Work

I evaluated a classification model using 5-fold cross-validation and analyzed:

- Score for each fold
- Mean cross-validation score
- Standard deviation
- Difference between a single split and cross-validation

For classification, I also worked with **stratified folds** to preserve class proportions across the folds.

### 💡 Main Takeaway

> Cross-validation provides a more stable estimate of model performance because the model is evaluated across multiple training and validation splits.

---

# 🟨 Day 3 — Bias-Variance & Diagnosing Model Fit

### 📂 Dataset
**BRCA Dataset**

### 📓 Notebook
`bias_variance_diagnosis.ipynb`

### 🎯 Focus

Day 3 focused on understanding why models fail and how to identify whether a model is **underfitting or overfitting**.

### 🔑 Key Concepts

- Bias
- Variance
- Underfitting
- Overfitting
- Train vs. validation performance
- Model complexity
- Regularization
- Ridge Regression
- Lasso Regression

### 📊 Model Diagnosis

| Training Score | Validation Score | Diagnosis |
|---|---|---|
| Low | Low | Underfitting |
| High | Much Lower | Overfitting |
| High | High / Close | Good Fit |

### 🧪 Hands-On Work

I worked with intentionally different model complexities to observe:

- Underfitting
- Overfitting
- Train-validation score gaps

I then applied techniques such as reducing model complexity and regularization to improve generalization.

### 💡 Main Takeaway

> A good model is not the one that memorizes the training data. The goal is to find the balance between bias and variance so the model can generalize to unseen data.

---

# 🟧 Day 4 — Feature Engineering & Hyperparameter Tuning

### 📂 Dataset
**Video Games Dataset**

### 📓 Notebook
`feature_engineering_tuning.ipynb`

### 🎯 Focus

Day 4 focused on improving model performance through **feature engineering** and systematic hyperparameter tuning.

### 🔑 Key Concepts

- Feature engineering
- Feature creation
- Feature transformation
- Binning
- Encoding
- Scaling
- Parameters vs. hyperparameters
- GridSearchCV
- RandomizedSearchCV

### 🧪 Feature Engineering

I created and transformed features to provide the model with more useful information.

Common techniques explored included:

- Creating new features
- Transforming existing features
- Binning continuous values
- Encoding categorical variables
- Scaling numerical features

### 🔍 Hyperparameter Tuning

Instead of manually selecting model settings, I used **GridSearchCV** to systematically test multiple hyperparameter combinations.

The search process used:

- Multiple parameter combinations
- 5-fold cross-validation
- F1 Score
- Best parameter selection

### 💡 Main Takeaway

> Better features can have a major impact on model performance, while systematic hyperparameter tuning helps identify a stronger configuration without relying on guesswork.

---

# 🟥 Day 5 — Scikit-learn Pipelines & Tuned End-to-End Pipeline

### 📂 Dataset
**Hotel Booking Dataset**

### 📓 Notebook
`pipelines_tuned_project.ipynb`

### 🎯 Focus

Day 5 brought together the concepts from the entire week into one **end-to-end machine learning workflow**.

The main goal was to create a professional pipeline that combines:

**Preprocessing → Feature Handling → Model → Hyperparameter Tuning → Evaluation**

### 🔑 Key Concepts

- `Pipeline`
- `ColumnTransformer`
- `SimpleImputer`
- `StandardScaler`
- `OneHotEncoder`
- Random Forest
- GridSearchCV
- 5-Fold Cross-Validation
- F1 Score
- Data Leakage Prevention
- Held-out Test Set

---

## 🏗️ Pipeline Structure

```text
Raw Dataset
     ↓
Train / Test Split
     ↓
ColumnTransformer
     ├── Numerical Features
     │      ↓
     │   Imputation
     │      ↓
     │   Scaling
     │
     └── Categorical Features
            ↓
         Imputation
            ↓
       One-Hot Encoding
            ↓
      Random Forest Model
            ↓
       GridSearchCV
            ↓
      Best Pipeline
            ↓
       Test Evaluation