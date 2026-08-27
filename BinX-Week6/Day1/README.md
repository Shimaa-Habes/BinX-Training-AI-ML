# 🧪 Sprint 1: Cardiovascular Disease Baseline

## 📌 Overview
This project builds a baseline machine learning model to predict cardiovascular
disease (`cardio`) from patient health indicators, as part of Sprint 1 of the
BinX AI/ML training program.

## 🎯 Sprint 1 Goal
Build a working baseline model and establish the minimum benchmark score that
every future model iteration must outperform.

## 📊 Dataset
- **Source:** Cardiovascular Disease Dataset
- **Size:** 70,000 records, 13 columns
- **Target:** `cardio` (0 = no disease, 1 = disease) — balanced ~50/50
- **Features:** age, gender, height, weight, blood pressure (ap_hi/ap_lo),
  cholesterol, glucose, smoking, alcohol intake, physical activity
- **Data quality:** No missing values, no duplicate rows
- **Note:** `age` is provided in days and converted to years (`age_years`) during EDA

## 🔍 Exploratory Data Analysis
- Verified data shape, missing values, and duplicates
- Checked target class balance
- Visualized age distribution, target balance, and blood pressure vs. target
- Reviewed feature correlations with the target variable

## 🤖 Baseline Model
- **Algorithm:** Logistic Regression
- **Preprocessing:** StandardScaler on numeric features
- **Train/test split:** 80/20, stratified on target

### Results
| Metric | Score |
|---|---|
| Accuracy | 71.3% |
| F1-score | 0.702 |

> ⚠️ **Baseline to beat:** Any future model must achieve an accuracy higher than
> **71.3%** and an F1-score higher than **0.702** to be considered an improvement.

## 📁 Project Structure
BinX-Week6/Day1/
├── hands_on_lab.ipynb # Main  notebook: EDA + baseline model
├── nn_architecture_sprint1.ipynb
├── heart_disease_uci.csv # Dataset
└── README.md


## 🔧 How to Run
1. Clone the repository and navigate to `BinX-Week6/Day1`
2. Install dependencies: `pip install pandas numpy matplotlib seaborn scikit-learn`
3. Open `hands_on_lab.ipynb` in Jupyter or VS Code
4. Run all cells in order

## 🚀 Development Workflow
- Work done on feature branch: `feature/sprint1-baseline`
- Draft Pull Request opened for review before merging to `main`

## 📈 Next Steps
- Try additional models (Decision Trees, Random Forest, etc.)
- Feature engineering (e.g., BMI from height/weight)
- Hyperparameter tuning
- Compare results against the Sprint 1 baseline