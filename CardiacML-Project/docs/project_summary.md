# 🫀 Cardiac Patient Monitoring System — Project Summary

> **Detailed Technical Documentation**

---

## 1. 🎯 Project Objective

The goal of this project is to analyze cardiovascular patient data and develop supervised machine learning models capable of classifying patients according to the presence or absence of cardiovascular disease.

The project demonstrates a complete machine learning workflow, including:

- Data loading
- Data cleaning
- Missing-value handling
- Duplicate detection
- Data validation
- Categorical encoding
- Exploratory Data Analysis
- Target analysis
- Baseline classification
- Model comparison
- Cross-validation
- Feature engineering
- Machine learning pipeline development
- Model evaluation

---

## 2. 📊 Dataset

### Dataset Name

**Cardiovascular Disease Dataset**

### Dataset Size

The dataset contains:

- **70,000 records**
- **13 columns** (12 input features + 1 target)
- One target variable: `cardio`

---

## 3. 🧬 Data Dictionary

| Feature | Description | Type |
|---|---|---|
| `id` | Patient record identifier | Numerical |
| `age` | Patient age in days | Numerical |
| `gender` | Patient gender | Categorical |
| `height` | Patient height in centimeters | Numerical |
| `weight` | Patient weight in kilograms | Numerical |
| `ap_hi` | Systolic blood pressure | Numerical |
| `ap_lo` | Diastolic blood pressure | Numerical |
| `cholesterol` | Cholesterol level category | Categorical |
| `gluc` | Glucose level category | Categorical |
| `smoke` | Smoking status | Boolean |
| `alco` | Alcohol consumption status | Boolean |
| `active` | Physical activity status | Boolean |
| `cardio` | Presence of cardiovascular disease | Target |

---

## 4. 🎯 Target Variable

The target variable is:

```text
cardio
```

The dataset contains two target classes (binary classification):

```text
0, 1
```

The observed target distribution was:

| Class | Count | Percentage |
|---:|---:|---:|
| 0 (No cardiovascular disease) | 35,021 | 50.03% |
| 1 (Cardiovascular disease) | 34,979 | 49.97% |

The distribution shows that the target classes are highly balanced, with an almost equal number of observations in each class.

---

## 5. 🧹 Data Preparation

A working copy of the original dataset was created before applying data preparation operations.

### Missing Values

The dataset contains no missing values, so no imputation was required for any feature.

### Missing-Value Strategy

Not applicable — since the dataset has no missing values, no median or mode imputation was needed.

After the missing-value check:

```text
Remaining missing values: 0
```

---

## 6. 🔍 Duplicate Check

Duplicate rows were checked before modeling to ensure data quality.

---

## 7. ✅ Data Validation

Several validation checks were performed to identify potentially invalid or unusual values.

The validation included:

- `age` range checks
- `height` range checks
- `weight` range checks
- `ap_hi` and `ap_lo` (blood pressure) range and consistency checks
- Unexpected values in categorical features (`gender`, `cholesterol`, `gluc`)
- Unexpected values in binary features (`smoke`, `alco`, `active`)
- `cardio` restricted to valid target values (`0` or `1`)

The validation step helped identify values that required review before modeling.

---

## 8. 🔢 Feature Encoding

Binary features:

```text
smoke
alco
active
```

were already represented as binary values and required no additional transformation.

Categorical features were transformed using **OneHotEncoder(handle_unknown="ignore")**:

```text
gender
cholesterol
gluc
```

Numerical features were scaled using **StandardScaler**:

```text
age
height
weight
ap_hi
ap_lo
```

Categorical and numerical preprocessing steps were combined using a **ColumnTransformer**.

---

## 9. 📈 Descriptive Statistics

Descriptive statistics were calculated for the numerical features:

```text
age
height
weight
ap_hi
ap_lo
```

These statistics were used to understand the scale and distribution of the numerical features before modeling. Detailed values are available directly in the analysis notebook.

---

## 10. 📊 Exploratory Data Analysis

EDA was performed to better understand the structure of the dataset.

The analysis included:

### 🎯 Target Distribution

The distribution of the two target classes (`cardio`) was examined to confirm class balance.

### 📊 Numerical Feature Distributions

The distributions of `age`, `height`, `weight`, `ap_hi`, and `ap_lo` were examined.

### 🚨 Outlier Analysis

Numerical features were reviewed for outliers, particularly in blood pressure, height, and weight.

### 🔗 Correlation Matrix

A correlation matrix was used to explore linear relationships between numerical variables.

### 📊 Feature vs Target Relationships

Numerical features (`age`, `height`, `weight`, `ap_hi`, `ap_lo`) were compared across the `cardio` classes using visualizations such as boxplots.

These visualizations helped identify features that showed noticeable differences between patients with and without cardiovascular disease.

EDA findings were treated as exploratory observations and not as evidence of clinical causation.

---

## 11. 🤖 Supervised Baseline

The classification problem was defined as a **binary classification task**.

### Features

The encoded dataset was separated into:

```text
X → Input features
y → Target variable (cardio)
```

### Train/Test Split

The dataset was divided using:

```text
80% Training
20% Testing
```

With:

```text
Training samples: 56,000
Testing samples: 14,000
Random state: 42
Stratified: Yes
```

---

## 12. 🧠 Logistic Regression

Logistic Regression was selected as the baseline classifier.

### Why Logistic Regression?

Logistic Regression provides a simple and interpretable baseline for classification problems.

It allows us to establish an initial performance reference before testing a more flexible model.

### Baseline Result

The Logistic Regression model achieved:

```text
Test Accuracy: 70.73%
```

This result was used as the baseline for comparison with the second classifier.

---

## 13. 🌲 Random Forest

Random Forest was selected as the second classifier.

### Why Random Forest?

Random Forest can capture nonlinear relationships and interactions between features.

It also provides a useful comparison against the simpler Logistic Regression baseline.

The Random Forest model was trained using the **same train/test split** to ensure a fair comparison.

---

## 14. 🔄 Cross-Validation

Cross-validation was applied to evaluate model stability across multiple training and validation splits.

The average cross-validation accuracy was compared with the test accuracy for both models.

This provides additional information beyond a single train/test split.

---

## 15. 🧩 Confusion Matrix

Confusion matrices were generated for both classification models.

A confusion matrix shows:

- Correct predictions for each class
- Incorrect predictions between classes
- Which target class is easier or harder for the model to identify

### False Positive

A **false positive** occurs when the model predicts `cardio = 1` but the patient does not actually have cardiovascular disease.

### False Negative

A **false negative** occurs when the model predicts `cardio = 0` but the patient actually has cardiovascular disease.

---

## 16. 📐 Model Evaluation Metrics

The models were evaluated using several metrics.

### 🎯 Accuracy

Measures the overall proportion of correct predictions.

### 🎯 Precision

Measures how many predictions for a class were actually correct.

### 🔍 Recall

Measures how many actual samples belonging to a class were correctly identified.

### ⚖️ F1-Score

Combines precision and recall into a single metric.

### 📈 ROC-AUC

ROC-AUC is calculated using the predicted probability of the positive class (`cardio = 1`), reflecting the binary nature of the classification task.

### 🧩 Confusion Matrix

Provides a detailed view of correct and incorrect predictions across both target classes.

---

## 17. ⚖️ Model Comparison

The models were compared using:

| Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| Test Accuracy | 70.73% | Evaluated in notebook |
| Cross-Validation | Evaluated in notebook | Evaluated in notebook |
| Weighted Precision | Evaluated in notebook | Evaluated in notebook |
| Weighted Recall | Evaluated in notebook | Evaluated in notebook |
| Weighted F1-Score | Evaluated in notebook | Evaluated in notebook |
| ROC-AUC | Evaluated in notebook | Evaluated in notebook |

The final model comparison is available directly in the analysis notebook.

The model selection should consider multiple metrics rather than accuracy alone.

---

## 18. 🔧 Feature Engineering

Additional feature engineering was performed to create useful representations of the existing patient information, using only the features available in the current dataset (e.g., `age`, `height`, `weight`, `ap_hi`, `ap_lo`, `gender`, `cholesterol`, `gluc`, `smoke`, `alco`, `active`).

The engineered features were incorporated into the modeling workflow to determine whether additional transformations could improve model performance.

---

## 19. 🔗 Machine Learning Pipeline

A Scikit-learn Pipeline was developed to combine the required preprocessing (including the `ColumnTransformer` for categorical and numerical features) and modeling steps into a single workflow.

The pipeline allows the model to:

```text
Raw Features
     ↓
Preprocessing (ColumnTransformer)
     ↓
Feature Engineering
     ↓
Model
     ↓
Prediction
```

This approach reduces the need for manual preprocessing and helps maintain consistency between training and prediction.

---

## 20. 🧪 End-to-End Pipeline Validation

The pipeline was fitted using the training data and then used to generate predictions on the test data.

The complete workflow was tested to ensure that it can run from preprocessing through prediction without requiring manual intermediate steps.

This improves reproducibility and reduces the risk of applying inconsistent preprocessing to new data.

---

## 21. 💾 Saved Model

The trained pipeline can be saved using **Joblib**.

Expected location:

```text
results/saved_model.pkl
```

The saved model can later be loaded and reused for predictions without retraining the complete pipeline.

---

## 22. 📁 Project Structure

```text
CardiacML-Project/
│
├── input/
│   └── heart_disease_uci.csv
│
├── analysis/
│   └── heart_analysis.ipynb
│
├── results/
│   ├── charts/
│   │   ├── eda_charts.png
│   │   └── model_metrics.png
│   └── saved_model.pkl
│
├── docs/
│   └── project_summary.md
│
├── env.txt
└── README.md
```

---

## 23. 💡 Key Findings

The exploratory and modeling stages provided several observations:

- The dataset contains two target classes with a highly balanced distribution.
- The dataset contains no missing values, simplifying the preprocessing workflow.
- Categorical features required OneHotEncoder transformation, and numerical features required StandardScaler transformation before modeling.
- Logistic Regression provided a baseline accuracy of **70.73%**.
- Random Forest was used as a more flexible comparison model.
- Multiple evaluation metrics were considered to avoid relying on accuracy alone.
- The final pipeline provides a reproducible end-to-end modeling workflow.

---

## 24. ⚠️ Limitations

### 📊 Dataset

The dataset contains 70,000 records representing a specific population and may not generalize to all cardiovascular populations or clinical environments.

### ⚖️ Class Balance

The target classes are highly balanced, with an almost equal number of patients in each class.

### 🤖 Model Selection

Only a limited number of classification algorithms were evaluated.

### 🌍 Generalization

The models were trained and evaluated using a single dataset and may not generalize to different patient populations or clinical environments.

### 🏥 Clinical Use

The models are educational machine learning models and have not undergone clinical validation.

---

## 25. 🏁 Final Conclusion

This project demonstrates an end-to-end supervised machine learning workflow for cardiovascular patient data.

Starting from raw patient records, the project performs data cleaning, validation, exploratory analysis, feature encoding, classification, model evaluation, feature engineering, and pipeline development.

Logistic Regression established a baseline performance of **70.73% test accuracy** on the binary `cardio` classification task, while Random Forest provided a second model for comparison.

Overall, the project demonstrates how machine learning techniques can be combined with structured data analysis to explore classification problems in healthcare-related datasets.

> 🫀 **The project is intended for educational purposes only and should not be used for clinical diagnosis or medical decision-making.**