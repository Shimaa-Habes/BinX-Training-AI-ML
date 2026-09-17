# 🚀 ScaleFlow

> **End-to-End Machine Learning Project — AI-Powered Project Intelligence**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Machine%20Learning-Project-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Deployment-Streamlit-red?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/API-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white">
</p>

---

## 🌟 Project Overview

**ScaleFlow** is an AI-powered project management and project intelligence platform designed to help teams plan, organize, monitor, and analyze their projects in one place.

The platform uses Machine Learning to analyze project and task data and support intelligent project decisions through:

- 📅 Task Delay Prediction
- ⚠️ Project Risk Analysis
- 🚧 Bottleneck Detection
- 📊 Project Performance and Health Analysis

The ML component follows an end-to-end workflow:

```text
📊 Project & Task Data
        ↓
🔍 Data Analysis
        ↓
🧹 Data Cleaning & Preprocessing
        ↓
⚙️ Feature Engineering
        ↓
🤖 ML Model Training
        ↓
📈 Model Evaluation
        ↓
💾 Model Serialization
        ↓
⚡ API Integration
        ↓
🎨 ScaleFlow Application
```

The goal is to build a reproducible and deployable Machine Learning component that can later be integrated with the ScaleFlow backend and mobile application.

---

## 🎯 Problem Statement

### What problem are we solving?

Large software projects generate large amounts of task, dependency, team, and progress data. Without proper analysis, project managers may have difficulty identifying delayed tasks, high-risk projects, workload problems, and potential bottlenecks early.

**ScaleFlow** uses Machine Learning to analyze project and task data and provide predictions and insights that support project monitoring and decision-making.

### 💡 Why does it matter?

- 📌 Early identification of potential task delays.
- ⚠️ Detection of projects or tasks with increased risk.
- 🚧 Identification of potential bottlenecks.
- 📊 Data-driven project monitoring.
- 🤖 Automated intelligence based on historical project data.
- 🚀 ML predictions can later be integrated into the ScaleFlow application.

---

## 📦 Dataset

The current ML data preparation uses public **Apache JIRA issue data** as the initial source for developing the Machine Learning pipeline.

The dataset preparation combines:

- Issues
- Issue Links
- Changelog
- Comments reserved for future NLP / Generative AI use

| Property            | Details                                       |
| ------------------- | --------------------------------------------- |
| 📚 Dataset          | Apache JIRA Issues                            |
| 🧩 Data Sources     | Issues, Issue Links, Changelog                |
| 🎯 Primary Target   | `resolution_time_days`                        |
| 🎯 Secondary Target | `long_resolution_risk`                        |
| 🏷️ ML Tasks         | Regression, Classification, Anomaly Detection |
| 🌐 Source           | Public Apache JIRA dataset                    |

### 🔎 Main Features

The current baseline dataset includes features such as:

- `project_key` — Identifies the project.
- `priority` — Task priority.
- `issue_type` — Type of issue/task.
- `is_subtask` — Indicates whether the issue is a subtask.
- `created_year` — Year when the task was created.
- `created_month` — Month when the task was created.
- `created_dayofweek` — Day of the week when the task was created.

Additional project and task features are planned as ScaleFlow generates its own historical data.

---

## 🧠 Machine Learning Methodology

The project follows a structured Machine Learning pipeline.

### 1️⃣ Exploratory Data Analysis

The dataset is analyzed to understand:

- Missing values
- Data distributions
- Data quality
- Task lifecycle
- Project distribution
- Target distribution
- Relationships between available features

### 2️⃣ Data Preprocessing

The preprocessing pipeline includes:

- 🧹 Data cleaning
- 🔄 Timestamp parsing
- 🗑️ Duplicate removal
- 🔎 Column validation
- ⚠️ Data leakage prevention
- 🎯 Target preparation
- ✂️ Chronological train / validation / test splitting
- 🔤 Categorical feature preparation

The current dataset uses a chronological:

```text
70% Train
15% Validation
15% Test
```

split to better reflect time-dependent project data.

### 3️⃣ Target Preparation

The current dataset uses two prepared targets:

#### `resolution_time_days`

A numerical target representing the number of days between task creation and resolution.

**Task type: Regression**

#### `long_resolution_risk`

A binary target identifying tasks with unusually long resolution times.

**Task type: Classification**

The threshold for `long_resolution_risk` is calculated using the **75th percentile of the training data** to avoid using information from validation or test data.

---

## 🤖 ML Models

ScaleFlow's ML architecture covers multiple project intelligence problems.

| Problem              | Task Type         | Planned Model            |
| -------------------- | ----------------- | ------------------------ |
| Task Resolution Time | Regression        | Random Forest Regressor  |
| Long Resolution Risk | Classification    | Random Forest Classifier |
| Bottleneck Detection | Anomaly Detection | Isolation Forest         |
| Project Health       | Regression        | Random Forest Regressor  |

### MVP ML Scope

The initial MVP focuses on:

1. Task delay / resolution prediction
2. Risk analysis
3. Bottleneck detection

Project health prediction is planned as a later phase because it requires a reliable numerical project-health target based on real project data.

---

## 📈 Model Evaluation

Different evaluation metrics are used according to the ML problem.

### Regression

For `resolution_time_days`:

- 📉 MAE
- 📊 RMSE
- 📈 R²

### Classification

For `long_resolution_risk`:

- 🎯 Precision
- 🔄 Recall
- ⚖️ F1-score
- 📈 ROC-AUC
- 📊 Confusion Matrix

### Anomaly Detection

For bottleneck detection:

- 🚧 Anomaly scores
- 🚩 Anomaly flags
- 👩‍💼 Manual validation during the initial phase

> 📌 Final numerical model results will be added after the final training and evaluation runs are completed.

---

## 📊 Results

### 🏆 Final Model Performance

| Model                    | Metric    | Score                                  |
| ------------------------ | --------- | -------------------------------------- |
| Random Forest Regressor  | MAE       | **To be added after final evaluation** |
| Random Forest Regressor  | RMSE      | **To be added after final evaluation** |
| Random Forest Regressor  | R²        | **To be added after final evaluation** |
| Random Forest Classifier | Precision | **To be added after final evaluation** |
| Random Forest Classifier | Recall    | **To be added after final evaluation** |
| Random Forest Classifier | F1-score  | **To be added after final evaluation** |
| Random Forest Classifier | ROC-AUC   | **To be added after final evaluation** |

> 📌 No performance values are reported here until they are produced by the actual training and evaluation pipeline.

---

## 💾 Model & Preprocessing Artifacts

Trained models and preprocessing components are serialized so they can be reused during inference without retraining.

Expected artifacts include:

```text
📁 artifacts/
├── 🤖 models/
│   ├── delay_prediction.joblib
│   ├── risk_analysis.joblib
│   └── bottleneck_detection.joblib
│
├── 🔄 preprocessing/
│   └── preprocessor.joblib
│
└── 📋 reports/
    └── evaluation_report.json
```

> ℹ️ The exact artifact names should match the final repository implementation.

---

## ⚡ FastAPI Integration

The Machine Learning component is designed to expose predictions through an API layer.

Example inference flow:

```text
ScaleFlow Backend
       ↓
ML API
       ↓
Input Validation
       ↓
Preprocessing
       ↓
Trained ML Model
       ↓
Prediction / Risk Score
       ↓
ScaleFlow Backend
       ↓
Web / Mobile Application
```

The API can later expose endpoints for:

```text
POST /predict/delay
POST /predict/risk
POST /predict/bottleneck
```

> 📌 Endpoint names should be updated to match the actual implementation.

---

## 🎨 ScaleFlow Application Integration

ML predictions are intended to appear inside the ScaleFlow project management application.

Potential AI-powered information includes:

- 📅 Delay probability
- ⚠️ Risk level
- 🚧 Bottleneck indicators
- 📊 Project health
- 💡 AI-generated recommendations
- 📝 Automated project summaries

The ML predictions form the analytical foundation, while Generative AI can use project information and ML outputs to generate understandable reports and recommendations.

---

## 🧪 Experiment Tracking

Experiments are documented through notebooks and the Machine Learning project structure.

Experiment records may include:

- 🤖 Model type
- ⚙️ Hyperparameters
- 📊 Evaluation metrics
- 🔄 Preprocessing configuration
- 📈 Training results
- 🧪 Model comparisons

MLflow can be added or used where available for structured experiment tracking.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone [REPOSITORY-URL]
cd ScaleFlow
```

### 2️⃣ Create a virtual environment

```bash
python -m venv .venv
```

### 3️⃣ Activate the environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the ML Pipeline

After placing the prepared dataset in the expected location:

```text
data/raw/scaleflow_tasks_dataset.csv
```

the ML pipeline can be executed through:

```bash
python main.py
```

Individual ML tasks can also be executed according to the implementation in the repository.

---

## 🔁 Reproducibility

The project is designed to support reproducible ML experiments through:

- 📌 Defined project structure
- 🎲 Controlled random seeds where applicable
- 🧹 Documented preprocessing
- ✂️ Reproducible data splitting
- 💾 Serialized model artifacts
- 📝 Documented experiments
- 📓 Reproducible notebooks
- 🔒 Leakage prevention

The preprocessing logic used during training is intended to be reused during inference.

---

## ⚠️ Limitations

The current ML system has several limitations:

- The initial dataset is based on public JIRA data rather than ScaleFlow's own historical project data.
- Planned due dates are not consistently available in the current JIRA dataset, so a fabricated `is_delayed` target is not used.
- Current baseline features are more limited than the complete feature set planned for production ScaleFlow.
- Risk labels are not directly available in the public dataset.
- Bottleneck detection initially requires manual validation because there is no reliable labeled bottleneck target.
- Project health prediction is deferred until a reliable real-world health target is available.

These limitations should be considered when interpreting model predictions.

---

## 🔮 Future Work

Possible improvements include:

- 🚀 Training on ScaleFlow's own historical project data.
- 🧠 Adding richer project and task features.
- 📅 Improving delay prediction using deadline and progress history.
- ⚠️ Developing more reliable project-risk labels.
- 🚧 Improving bottleneck detection with labeled historical outcomes.
- 📊 Implementing project health prediction.
- 🔍 Advanced feature engineering.
- 🤖 Hyperparameter optimization.
- ⚡ Backend and mobile integration.
- 📝 Generative AI project reports and recommendations.
- 📈 Continuous model monitoring and retraining.

---

## 🏁 Definition of Done

| Requirement                        | Status                         |
| ---------------------------------- | ------------------------------ |
| 📊 Dataset Obtained & Inspected    | ✅ Completed                   |
| 🧹 Data Cleaning & Preparation     | ✅ Completed                   |
| ⚙️ Feature Preparation             | ✅ Completed                   |
| 🎯 Target Preparation              | ✅ Completed                   |
| ✂️ Train / Validation / Test Split | ✅ Completed                   |
| 🤖 ML Pipeline Structure           | ✅ Prepared                    |
| 🧠 Model Training                  | ⚠️ Final results to be added   |
| 📈 Model Evaluation                | ⚠️ Final results to be added   |
| 💾 Model Serialization             | ⚠️ Final artifacts to be added |
| ⚡ API Integration                 | ⚠️ Pending implementation      |
| 🎨 Application Integration         | ⚠️ Pending implementation      |
| 🌍 Public Deployment               | ⚠️ Pending final deployment    |

---

## 📚 Technical Documentation

For more details, see:

- 📓 Machine Learning notebooks
- 📊 Data preparation documentation
- 🧠 ML model approach
- ⚙️ ML pipeline documentation
- 📈 Evaluation reports
- ⚡ API documentation
- 🎨 ScaleFlow application documentation

---

## 👩‍💻 Project

**ScaleFlow — Enterprise Project Intelligence Platform**

Developed as part of the **BinX Tech AI & Machine Learning Training Program — Team 04**.

> 🚀 From project data to intelligent project insights.

---

<p align="center">

### ✨ Plan • Analyze • Predict • Improve ✨

**Machine Learning | Python | Scikit-learn | FastAPI | ScaleFlow**

</p>
