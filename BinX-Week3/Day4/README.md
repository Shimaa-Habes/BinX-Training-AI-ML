# 🤖 AI & ML Course with BinX

# 📘 Week 3 — Day 4
## 🌳 Trees, Forests, SVMs & k-NN

---

## 🎯 Overview

In this day, we explored four powerful machine learning classification algorithms:

- 🌳 Decision Trees
- 🌲 Random Forests
- 📐 Support Vector Machines (SVM)
- 👥 k-Nearest Neighbors (k-NN)

The goal was to understand how each algorithm makes predictions, compare their performance, and select the best model using evaluation metrics.

---

# 📂 Dataset

## Healthcare Diabetes Prediction Dataset

The dataset contains medical and demographic information used to predict whether a person has diabetes.

### Features:

- Gender
- Age
- Hypertension
- Heart Disease
- Smoking History
- BMI
- HbA1c Level
- Blood Glucose Level

### Target:

- Diabetes

---

# 🌳 4.1 Decision Tree

## Concept

Decision Tree is a rule-based classification algorithm that makes decisions by splitting data using a sequence of questions.

## Advantages

✅ Easy to interpret  
✅ Human-readable rules  
✅ Handles nonlinear relationships  

## Disadvantages

⚠️ Can overfit when the tree becomes too deep

---

# 🌲 4.2 Random Forest

## Concept

Random Forest is an ensemble learning method that combines multiple Decision Trees.

Each tree learns from random samples of the data, and the final prediction is based on majority voting.

## Advantages

✅ Reduces overfitting  
✅ Strong performance  
✅ Provides feature importance analysis  

## Feature Importance

Random Forest was used to identify which features contributed most to diabetes prediction.

---

# 📐 4.3 Support Vector Machine (SVM)

## Concept

SVM finds the optimal decision boundary that separates different classes while maximizing the margin.

The RBF kernel was used to handle nonlinear relationships.

## Advantages

✅ Powerful classifier  
✅ Works well with high-dimensional data  

## Disadvantages

⚠️ Requires feature scaling  
⚠️ Slower with large datasets  

---

# 👥 4.4 k-Nearest Neighbors (k-NN)

## Concept

k-NN predicts new samples by looking at the closest training examples and assigning the majority class.

## Advantages

✅ Simple and intuitive  
✅ No complex training process  

## Disadvantages

⚠️ Slow for large datasets  
⚠️ Sensitive to feature scaling  

---

# ⚖️ Model Comparison

All models were trained and evaluated using:

- Same dataset
- Same train/test split
- Same evaluation metrics

## Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1-score

---

# 🧪 Hands-On Lab

## Steps Completed:

✅ Loaded and prepared diabetes dataset  
✅ Split data into training and testing sets  
✅ Trained four classification models  
✅ Generated predictions  
✅ Evaluated models using classification metrics  
✅ Compared model performance  
✅ Analyzed Random Forest feature importance  
✅ Selected the best-performing model  

---

# 🏆 Final Model Selection

The best model was selected based on the highest F1-score.

F1-score was chosen because it provides a balance between:

- Correct diabetes detection (Recall)
- Avoiding incorrect predictions (Precision)

---

# 🛠️ Tools Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

---

# 📁 Project Structure
Day4/
│
├── day4.ipynb
│
├── diabetes.csv
│
└── README.md
