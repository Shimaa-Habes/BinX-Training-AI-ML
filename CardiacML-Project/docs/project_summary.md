# 🫀 Cardiac Patient Monitoring System — Project Summary

> **Detailed Technical Documentation**

---

## 1. 🎯 Project Objective

The goal of this project is to analyze cardiac patient data and develop supervised machine learning models capable of classifying patients according to different heart disease severity levels.

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

**Heart Disease UCI Dataset**

### Dataset Size

The dataset contains:

- **920 records**
- Multiple demographic and clinical features
- One target variable: `num`

### Data Sources

The records originate from:

- Cleveland
- Hungary
- Switzerland
- VA Long Beach

---

## 3. 🧬 Data Dictionary

| Feature | Description | Type |
|---|---|---|
| `id` | Patient record identifier | Numerical |
| `age` | Patient age | Numerical |
| `sex` | Patient sex | Categorical |
| `dataset` | Source dataset | Categorical |
| `cp` | Chest pain type | Categorical |
| `trestbps` | Resting blood pressure | Numerical |
| `chol` | Serum cholesterol | Numerical |
| `fbs` | Fasting blood sugar indicator | Boolean |
| `restecg` | Resting ECG result | Categorical |
| `thalch` | Maximum achieved heart rate | Numerical |
| `exang` | Exercise-induced angina | Boolean |
| `oldpeak` | ST depression induced by exercise | Numerical |
| `slope` | Slope of peak exercise ST segment | Categorical |
| `ca` | Number of major vessels | Numerical |
| `thal` | Thalassemia result | Categorical |
| `num` | Heart disease severity class | Target |

---

## 4. 🎯 Target Variable

The target variable is:

```text
num
```

The dataset contains five target classes:

```text
0, 1, 2, 3, 4
```

The observed target distribution was:

| Class | Count |
|---:|---:|
| 0 | 411 |
| 1 | 265 |
| 2 | 109 |
| 3 | 107 |
| 4 | 28 |

The distribution shows that the classes are not perfectly balanced, with class `4` having considerably fewer observations than class `0`.

---

## 5. 🧹 Data Preparation

A working copy of the original dataset was created before applying data preparation operations.

### Missing Values

The original dataset contained missing values in several features, including:

- `trestbps`
- `chol`
- `fbs`
- `restecg`
- `thalch`
- `exang`
- `oldpeak`
- `slope`
- `ca`
- `thal`

### Missing-Value Strategy

Numerical features were imputed using the **median**.

Categorical and boolean features were imputed using the **most frequent value (mode)**.

After imputation:

```text
Remaining missing values: 0
```

---

## 6. 🔍 Duplicate Check

Duplicate rows were checked before modeling.

Result:

```text
Number of duplicate rows: 0
Remaining duplicate rows: 0
```

No duplicate records were found.

---

## 7. ✅ Data Validation

Several validation checks were performed to identify potentially invalid or unusual values.

The validation included:

- `age <= 0`
- `trestbps <= 0`
- `chol <= 0`
- `thalch <= 0`
- `oldpeak < 0`
- `ca` outside `0–3`
- `num` outside `0–4`
- Unexpected values in categorical features

The validation step helped identify values that required review before modeling.

---

## 8. 🔢 Feature Encoding

Boolean features:

```text
fbs
exang
```

were converted to numerical values.

Categorical features were transformed using **one-hot encoding**:

```text
sex
dataset
cp
restecg
slope
thal
```

`drop_first=True` was used to avoid unnecessary redundant dummy variables.

---

## 9. 📈 Descriptive Statistics

Descriptive statistics were calculated for the numerical features.

Important observations included:

- Mean age: approximately **53.51 years**
- Mean resting blood pressure: approximately **132.14**
- Mean cholesterol: approximately **244.03**
- Mean maximum heart rate: approximately **137.69**
- Mean oldpeak: approximately **0.87**

These statistics were used to understand the scale and distribution of the numerical features before modeling.

---

## 10. 📊 Exploratory Data Analysis

EDA was performed to better understand the structure of the dataset.

The analysis included:

### 🎯 Target Distribution

The distribution of the five target classes was examined to identify class imbalance.

### 🔗 Correlation Matrix

A correlation matrix was used to explore linear relationships between numerical variables.

### 📊 Feature vs Target Relationships

Selected numerical features were compared across the target classes using visualizations such as boxplots.

These visualizations helped identify features that showed noticeable differences between heart disease severity classes.

EDA findings were treated as exploratory observations and not as evidence of clinical causation.

---

## 11. 🤖 Supervised Baseline

The classification problem was defined as a **multi-class classification task**.

### Features

The encoded dataset was separated into:

```text
X → Input features
y → Target variable (num)
```

### Train/Test Split

The dataset was divided using:

```text
80% Training
20% Testing
```

With:

```text
Training samples: 736
Testing samples: 184
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
Test Accuracy: 59.78%
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
- Which target classes are easier or harder for the model to distinguish

### False Positive

A **false positive** occurs when the model predicts a class incorrectly when the actual class is different.

In simple terms:

> The model says a patient belongs to a particular class, but the actual class is different.

### False Negative

A **false negative** occurs when the model fails to correctly identify a class that is actually present.

In simple terms:

> The model predicts another class even though the patient actually belongs to the target class being considered.

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

ROC-AUC measures the model's ability to distinguish between classes when applicable.

### 🧩 Confusion Matrix

Provides a detailed view of correct and incorrect predictions across all target classes.

---

## 17. ⚖️ Model Comparison

The models were compared using:

| Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| Test Accuracy | 59.78% | Evaluated in notebook |
| Cross-Validation | Evaluated in notebook | Evaluated in notebook |
| Weighted Precision | Evaluated in notebook | Evaluated in notebook |
| Weighted Recall | Evaluated in notebook | Evaluated in notebook |
| Weighted F1-Score | Evaluated in notebook | Evaluated in notebook |
| ROC-AUC | Evaluated in notebook | Evaluated in notebook |

The final model comparison is available directly in the analysis notebook.

The model selection should consider multiple metrics rather than accuracy alone.

---

## 18. 🔧 Feature Engineering

Additional feature engineering was performed to create useful representations of the existing patient information.

The engineered features were incorporated into the modeling workflow to determine whether additional transformations could improve model performance.

---

## 19. 🔗 Machine Learning Pipeline

A Scikit-learn Pipeline was developed to combine the required preprocessing and modeling steps into a single workflow.

The pipeline allows the model to:

```text
Raw Features
     ↓
Preprocessing
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
│   └── heart.csv
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

- The dataset contains five target classes with noticeable class imbalance.
- Several features contained missing values and required preprocessing.
- Categorical and boolean features required transformation before modeling.
- Logistic Regression provided a baseline accuracy of **59.78%**.
- Random Forest was used as a more flexible comparison model.
- Multiple evaluation metrics were considered to avoid relying on accuracy alone.
- The final pipeline provides a reproducible end-to-end modeling workflow.

---

## 24. ⚠️ Limitations

### 📊 Dataset

The dataset contains 920 records and may not represent all real-world cardiac populations.

### 🧹 Missing Data

Imputation was required for several features. The chosen imputation strategies may not perfectly represent the original missing values.

### ⚖️ Class Imbalance

The target classes are not evenly distributed, particularly class `4`, which contains substantially fewer samples.

### 🤖 Model Selection

Only a limited number of classification algorithms were evaluated.

### 🌍 Generalization

The models were trained and evaluated using a single dataset and may not generalize to different patient populations or clinical environments.

### 🏥 Clinical Use

The models are educational machine learning models and have not undergone clinical validation.

---

## 25. 🏁 Final Conclusion

This project demonstrates an end-to-end supervised machine learning workflow for cardiac patient data.

Starting from raw patient records, the project performs data cleaning, validation, exploratory analysis, feature encoding, classification, model evaluation, feature engineering, and pipeline development.

Logistic Regression established a baseline performance of **59.78% test accuracy**, while Random Forest provided a second model for comparison.

Overall, the project demonstrates how machine learning techniques can be combined with structured data analysis to explore classification problems in healthcare-related datasets.

> 🫀 **The project is intended for educational purposes only and should not be used for clinical diagnosis or medical decision-making.**