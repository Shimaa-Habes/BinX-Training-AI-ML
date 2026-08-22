# 🧠 Day 4 — Hyperparameter Tuning & End-to-End Pipelines

> 🎯 **Today's Focus:** Building a complete, tuned, and leakage-safe Machine Learning pipeline.

---

## 🌟 Overview

Today, I focused on **Hyperparameter Tuning** and building an **End-to-End Machine Learning Pipeline** using Scikit-learn.

The workflow combined:

`Feature Engineering → Preprocessing → Model Training → Cross-Validation → Hyperparameter Tuning → Evaluation`

The main model used was **Random Forest Classifier**.

---

## 🎯 Learning Objectives

* 🔧 Understand hyperparameters and their role in model performance
* 🏗️ Build an end-to-end Scikit-learn `Pipeline`
* 🔀 Use `ColumnTransformer` for numerical and categorical features
* 🩹 Handle missing values using `SimpleImputer`
* 📏 Scale numerical features using `StandardScaler`
* 🔤 Encode categorical features using `OneHotEncoder`
* 🎛️ Define a hyperparameter search space
* 🔍 Apply `GridSearchCV`
* 🔄 Use 5-Fold Cross-Validation
* 📊 Optimize the model using F1 Score
* 🧪 Evaluate the tuned Pipeline on the held-out test set
* ⚖️ Compare the tuned model with a baseline model
* 🔐 Prevent data leakage using Pipeline-based preprocessing

---

## 🧩 Step 1 — Build the End-to-End Pipeline

A complete Pipeline was created to combine preprocessing and model training.

### 🔢 Numerical Features

```text
Missing Values
      ↓
Median Imputation
      ↓
StandardScaler
```

### 🔤 Categorical Features

```text
Missing Values
      ↓
Most Frequent Imputation
      ↓
One-Hot Encoding
```

Both preprocessing branches were combined using `ColumnTransformer`.

---

## 🧩 Step 2 — Add Engineered Features

The engineered features created during Day 4 were included in the training data.

This allowed the model to use the additional information created during the feature engineering stage while keeping preprocessing and model training inside the same Pipeline.

---

## 🌲 Step 3 — Define the Model & Hyperparameter Grid

The selected model was:

`RandomForestClassifier(random_state=42)`

The following hyperparameters were tuned:

| ⚙️ Hyperparameter   | 🔍 Search Values   |
| ------------------- | ------------------ |
| `n_estimators`      | `100`, `200`       |
| `max_depth`         | `None`, `10`, `20` |
| `min_samples_split` | `2`, `5`           |

GridSearchCV tested every possible combination.

With 5-Fold Cross-Validation:

`2 × 3 × 2 × 5 = 60 fits`

---

## 🔎 Step 4 — Run GridSearchCV

`GridSearchCV` was used to systematically evaluate the defined hyperparameter combinations.

* 🔍 Search Method: `GridSearchCV`
* 🔄 Cross-Validation: `5-Fold`
* 📊 Scoring Metric: `F1 Score`
* 🌲 Model: `Random Forest`

The best configuration was selected based on the highest mean F1 Score across the five validation folds.

---

## 🏆 Step 5 — Best Hyperparameters & CV Score

The best hyperparameters were extracted using:

`grid_search.best_params_`

The selected model included:

* 🌲 Random Forest
* `max_depth = 20`
* `random_state = 42`

The best Cross-Validation F1 Score was:

**🏆 Best CV F1 Score = 1.00**

---

## 📊 Step 6 — Evaluate the Tuned Pipeline

The best Pipeline was evaluated on the held-out test set.

The evaluation included:

* 🎯 F1 Score
* 🎯 Precision
* 🎯 Recall
* 🎯 Accuracy
* 📋 Classification Report

### 🧪 Test Performance

**Test F1 Score = 1.00**

The tuned Pipeline achieved a perfect F1 Score on the held-out test set.

---

## ⚖️ Step 7 — Baseline vs Tuned Model

The tuned Pipeline was compared with the baseline Random Forest model.

| 📌 Model       | 🎯 Test F1 Score |
| -------------- | ---------------: |
| Baseline Model |           `1.00` |
| Tuned Pipeline |           `1.00` |
| Improvement    |           `0.00` |

The baseline model had already achieved a perfect F1 Score, so hyperparameter tuning did not produce a measurable improvement.

---

## 🔐 Step 8 — Prevent Data Leakage

Preprocessing was performed **inside the Pipeline** instead of being applied to the entire dataset before Cross-Validation.

The final workflow was:

```text
X_train
   ↓
Preprocessor
   ├── Numerical Imputation
   ├── Numerical Scaling
   ├── Categorical Imputation
   └── Categorical Encoding
   ↓
Random Forest
   ↓
Prediction
```

### ✅ Leakage Check

`Preprocessing inside Pipeline → True`

This ensures that preprocessing steps are fitted only on the appropriate training data during Cross-Validation.

The held-out test set remained separate until the final evaluation.

---

## 🧪 Step 9 — Hands-On Lab

The Hands-On Lab brought together the complete workflow:

* 🏗️ Build a `Pipeline`
* 🔀 Add `ColumnTransformer`
* 🧩 Include engineered features
* 🌲 Define Random Forest
* 🎛️ Define the hyperparameter grid
* 🔍 Run `GridSearchCV`
* 🔄 Apply 5-Fold Cross-Validation
* 🏆 Find the best parameters
* 📊 Report the best CV score
* 🧪 Evaluate the tuned Pipeline
* ⚖️ Compare against the baseline
* 🔐 Confirm leakage-safe preprocessing
* 📝 Document the final results

---

## 🛠️ Libraries & Tools

### 🐍 Main Tools

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Scikit-learn

### 🤖 Main Scikit-learn Components

* `Pipeline`
* `ColumnTransformer`
* `SimpleImputer`
* `StandardScaler`
* `OneHotEncoder`
* `RandomForestClassifier`
* `GridSearchCV`
* `f1_score`
* `classification_report`

---

## 💡 Key Takeaways

* Hyperparameters control important aspects of model behavior.
* `GridSearchCV` provides a systematic way to search for better configurations.
* 5-Fold Cross-Validation helps evaluate model configurations more reliably.
* `Pipeline` keeps preprocessing and model training together.
* `ColumnTransformer` allows different preprocessing strategies for different feature types.
* Missing values can be handled directly inside the Pipeline.
* Preprocessing inside the Pipeline helps prevent data leakage.
* The final model should always be evaluated on a separate held-out test set.
* Hyperparameter tuning does not always improve the final score.
* A strong baseline can already achieve excellent performance.

---

## 🏁 Final Results

| 📊 Metric           | Result |
| ------------------- | -----: |
| 🏆 Best CV F1 Score | `1.00` |
| 🧪 Baseline Test F1 | `1.00` |
| 🚀 Tuned Test F1    | `1.00` |
| 📈 Improvement      | `0.00` |

### 📌 Final Interpretation

The tuned Pipeline achieved a **Test F1 Score of 1.00**, matching the baseline model.

Since the baseline already achieved a perfect score, hyperparameter tuning resulted in no measurable improvement.

However, the experiment successfully demonstrated a complete and structured Machine Learning workflow using preprocessing, feature engineering, Cross-Validation, hyperparameter tuning, model comparison, and final evaluation.

---

## ✨ Conclusion

Today's work moved the Machine Learning workflow toward a more structured and professional solution.

The final workflow combined:

**🧩 Feature Engineering → 🔀 Preprocessing → 🌲 Random Forest → 🎛️ Hyperparameter Tuning → 🔄 5-Fold Cross-Validation → 🧪 Test Evaluation → ⚖️ Model Comparison**

Even though the final score did not improve, the process provided practical experience in **Pipeline design, GridSearchCV, Cross-Validation, hyperparameter optimization, model evaluation, and data leakage prevention**.

> 💻 **Day 4 Complete — Tuned, Evaluated & Documented! 🚀**
