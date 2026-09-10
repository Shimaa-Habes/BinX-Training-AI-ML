# 🧠 Day 5 — Full Evaluation, Explainability & Sprint Review

> 🚀 **Sprint 3 — Final Evaluation & Explainability**
>
> Day 5 focused on turning the trained model into a **well-evaluated, explainable, and documented ML component**.
>
> The model was evaluated using task-appropriate metrics, tested with imbalance-handling techniques, and explained using **SHAP** at both global and individual prediction levels.

---

## 🎯 Learning Objectives

By the end of Day 5, I worked on:

- 📊 Full model evaluation using appropriate classification metrics
- 📈 Comparing the final model with the Week 6 baseline
- ⚖️ Checking and handling class imbalance
- 🧪 Testing SMOTE on the training data
- 🎚️ Tuning the prediction threshold
- 🔍 Analyzing the precision-recall trade-off
- 🧠 Understanding model behavior using SHAP
- 🌍 Generating global feature importance
- 🔎 Explaining individual predictions
- 🐛 Connecting explainability with error analysis
- 🔄 Completing the Sprint 3 review and retrospective
- 🚀 Defining the next action for Sprint 4

---

# 📊 1. Full Model Evaluation

The project uses a **binary classification task** based on the Breast Cancer Wisconsin dataset.

Instead of relying on accuracy alone, I evaluated the model using:

| Metric       | Purpose                                                     |
| ------------ | ----------------------------------------------------------- |
| 🎯 Precision | How many predicted positive cases were actually positive    |
| 🔎 Recall    | How many actual positive cases were correctly detected      |
| ⚖️ F1-score  | Balance between Precision and Recall                        |
| 📈 ROC-AUC   | Overall ability of the model to distinguish between classes |

### 🏆 Final Model Performance

| Metric       | Final Model |
| ------------ | ----------: |
| 🎯 Precision |  **0.9861** |
| 🔎 Recall    |  **0.9861** |
| ⚖️ F1-score  |  **0.9861** |
| 📈 ROC-AUC   |   Evaluated |

✨ The final model achieved strong performance across the main classification metrics.

---

# 📈 2. Week 6 Baseline vs Final Model

One of the main goals of Day 5 was to make the model improvement measurable.

### 🔄 Performance Comparison

| Metric       | Week 6 Baseline | Final Model |
| ------------ | --------------: | ----------: |
| 🎯 Precision |          0.7100 |  **0.9861** |
| 🔎 Recall    |          0.7100 |  **0.9861** |
| ⚖️ F1-score  |          0.7020 |  **0.9861** |

### 💡 What does this show?

The final model performed significantly better than the Week 6 baseline.

This comparison gives a clearer picture of the model's improvement than reporting a single accuracy value.

> ⚠️ ROC-AUC was not reported in the Week 6 baseline, so no baseline ROC-AUC value was added.

---

# ⚖️ 3. Class Imbalance Analysis

Before applying any imbalance technique, I checked the distribution of the target classes.

### 📊 Class Distribution

| Class      | Samples | Percentage |
| ---------- | ------: | ---------: |
| 🟣 Class 0 |     212 |     37.26% |
| 🟣 Class 1 |     357 |     62.74% |

### 📐 Imbalance Ratio

**1.68 : 1**

This means that the dataset has a **moderate class imbalance**, but it is not severely imbalanced.

---

# 🧪 4. SMOTE Experiment

I tested **SMOTE (Synthetic Minority Over-sampling Technique)** to balance the training data.

🔐 Important:

> SMOTE was applied **only to the training data**.
> The test set was kept unchanged for fair evaluation.

### 📊 Before vs After SMOTE

| Metric       | Original Model | SMOTE Model |
| ------------ | -------------: | ----------: |
| 🎯 Precision |         0.9861 |      0.9857 |
| 🔎 Recall    |         0.9861 |      0.9583 |
| ⚖️ F1-score  |         0.9861 |      0.9718 |

### 🧠 Conclusion

SMOTE did **not** improve the model's test performance.

In fact:

- Precision decreased slightly
- Recall decreased
- F1-score decreased

Therefore, I kept the **original model** instead of using SMOTE.

💡 This experiment showed that an imbalance technique should be evaluated based on its actual results rather than applied automatically.

---

# 🎚️ 5. Threshold Tuning

I also tested different prediction thresholds to understand the **Precision-Recall trade-off**.

The default threshold was compared with several alternatives.

For this task, **Recall is especially important** because missing a positive case means creating a **False Negative**.

### ⭐ Selected Threshold

**Threshold = 0.2**

| Metric       |     Result |
| ------------ | ---------: |
| 🎚️ Threshold |    **0.2** |
| 🎯 Precision | **0.9730** |
| 🔎 Recall    | **1.0000** |
| ⚖️ F1-score  | **0.9863** |

### 💡 Why 0.2?

The threshold of **0.2** achieved:

> 🔎 **100% Recall**

while still maintaining:

> 🎯 **97.3% Precision**

This makes it a useful operating point when reducing **False Negatives** is especially important.

---

# 🧠 6. SHAP Explainability

To understand **why the model makes its predictions**, I used:

### 🔍 SHAP — SHapley Additive exPlanations

SHAP provides two important levels of explanation:

🌍 **Global Explanation**

Shows which features are generally important across the dataset.

🔎 **Local Explanation**

Shows how individual features influenced one specific prediction.

---

# 🌍 7. Global Feature Importance

The SHAP analysis identified the following features as the strongest contributors:

|    # | Feature                 |         Mean | SHAP |     |
| ---: | ----------------------- | -----------: | ---- | --- |
| 🥇 1 | mean compactness        | **1.253661** |
| 🥈 2 | compactness error       | **0.755928** |
| 🥉 3 | fractal dimension error | **0.238135** |
|    4 | worst smoothness        |     0.158510 |
|    5 | worst compactness       |     0.093999 |
|    6 | mean smoothness         |     0.044040 |
|    7 | worst symmetry          |     0.044025 |
|    8 | smoothness error        |     0.041666 |
|    9 | concavity error         |     0.038206 |
|   10 | texture error           |     0.009503 |

### 💡 Main Finding

The strongest global feature was:

> ⭐ **mean compactness**

This means it had the largest average SHAP contribution among the evaluated features.

---

# 🔎 8. Individual Prediction Explanation

A SHAP **waterfall plot** was generated to understand one specific prediction.

The explanation showed that different features pushed the prediction in different directions.

### ⬆️ Features Pushing the Prediction Higher

Some of the strongest positive contributions were:

- 🟢 mean compactness
- 🟢 compactness error
- 🟢 fractal dimension error
- 🟢 worst smoothness
- 🟢 worst compactness
- 🟢 mean smoothness
- 🟢 worst symmetry

### ⬇️ Features Pushing the Prediction Lower

Some of the strongest negative contributions were:

- 🔵 worst texture
- 🔵 radius error
- 🔵 worst area
- 🔵 worst radius
- 🔵 worst perimeter
- 🔵 area error
- 🔵 perimeter error
- 🔵 mean concave points
- 🔵 mean texture

### 🧩 Simple Explanation

The model does not depend on one feature only.

Instead, it combines multiple measurements and their contributions before producing the final prediction.

This makes SHAP useful for communicating model behavior to **non-technical stakeholders**.

---

# 🐛 9. Error Analysis

The final model produced:

> ❌ **2 misclassified test samples**

The purpose of error analysis is to understand why these predictions were incorrect.

The errors can be investigated from several perspectives:

- 🧹 Data quality
- 📊 Feature limitations
- 🧠 Model limitations
- 🎚️ Decision threshold
- 🔀 Ambiguous samples

### 🔗 SHAP + Error Analysis

SHAP can be used together with the misclassified samples.

The confusion matrix tells us:

> **"Where did the model make mistakes?"**

SHAP helps answer:

> **"Why did the model make this prediction?"**

This makes explainability an important part of the error-analysis process.

---

# 🎤 10. Sprint Review

The Sprint 3 review covered the complete evaluation and explainability workflow.

### ✅ Completed Work

- 📊 Full model evaluation
- 📈 Week 6 baseline comparison
- ⚖️ Class imbalance analysis
- 🧪 SMOTE experiment
- 🎚️ Threshold tuning
- 🔎 Precision-Recall analysis
- 🌍 Global SHAP explanation
- 🔍 Individual SHAP explanation
- 🐛 Error analysis
- 📝 Results documentation

### 🏆 Sprint Result

The final model achieved strong classification performance and the SHAP analysis provided additional insight into **which features influenced the predictions and in which direction**.

---

# 🔄 11. Sprint 3 Retrospective

## 🌟 What Went Well

- 📊 Used multiple evaluation metrics instead of relying on one number.
- 📈 Compared the final model directly with the Week 6 baseline.
- 🧪 Tested SMOTE and evaluated its actual effect.
- 🎚️ Used threshold tuning to prioritize Recall.
- 🧠 Added SHAP explainability.
- 🌍 Generated global feature importance.
- 🔎 Explained individual predictions.
- 📝 Documented the main results.

---

## 🛠️ What Could Be Improved

- 🔍 Expand error analysis by investigating more individual samples.
- 📊 Use a separate validation set for threshold selection in a production workflow.
- 🧪 Test the final model on additional unseen data before deployment.
- 📦 Improve the final integration and user-facing prediction workflow.

---

## 💭 Main Lesson

> **A model is not complete just because it has a high score.**

A reliable ML component should include:

**Evaluation → Error Analysis → Explainability → Documentation → Review**

---

# 🚀 12. Sprint 4 Action

The main action for Sprint 4 is:

## 🚀 Deployment & Final Polish

The next sprint will focus on turning the completed model into a **usable and deployable component**.

### Planned Actions

- 🔌 Prepare the model for deployment
- 🔄 Keep training-time and prediction-time preprocessing consistent
- 🖥️ Improve the prediction interface
- 🧪 Perform final testing
- 📝 Finalize documentation
- 🔗 Integrate the model into the final application
- 🚀 Prepare the project for deployment

---

# 🧰 13. Tools Used

| Tool                | Purpose                     |
| ------------------- | --------------------------- |
| 🐍 Python           | Main programming language   |
| 📊 Pandas           | Data manipulation           |
| 🔢 NumPy            | Numerical operations        |
| 🤖 Scikit-learn     | ML model and evaluation     |
| ⚖️ imbalanced-learn | SMOTE                       |
| 🧠 SHAP             | Model explainability        |
| 📈 Matplotlib       | Visualization               |
| 📓 Jupyter Notebook | Development and experiments |
| 🌿 Git              | Version control             |
| 🐙 GitHub           | Repository and PR workflow  |

---

# ✅ 14. Sprint 3 Completion Checklist

### 📊 Evaluation

- [x] Full evaluation completed
- [x] Precision reported
- [x] Recall reported
- [x] F1-score reported
- [x] ROC-AUC evaluated
- [x] Week 6 baseline comparison completed

### ⚖️ Imbalance

- [x] Class distribution checked
- [x] Imbalance ratio calculated
- [x] SMOTE tested on training data
- [x] Precision-Recall trade-off analyzed
- [x] Threshold tuning completed
- [x] Best operating threshold selected

### 🧠 Explainability

- [x] SHAP installed and configured
- [x] Global SHAP analysis completed
- [x] Global feature importance identified
- [x] Individual prediction explained
- [x] SHAP results interpreted

### 🐛 Error Analysis

- [x] Misclassified samples identified
- [x] Error-analysis process documented
- [x] SHAP connected with error analysis

### 🔄 Sprint Completion

- [x] Sprint Review completed
- [x] Sprint 3 Retrospective documented
- [x] Sprint 4 action defined
- [ ] Git commit
- [ ] Git push
- [ ] Pull Request created/updated
- [ ] Mentor review
- [ ] Requested changes fixed
- [ ] Pull Request merged

---

# 🎯 Final Takeaway

Day 5 completed the **evaluation and explainability stage of Sprint 3**.

The final model was:

**📊 Evaluated → ⚖️ Tested for imbalance → 🎚️ Threshold-tuned → 🧠 Explained with SHAP → 🐛 Reviewed for errors → 📝 Documented**

The next step is:

> 🚀 **Sprint 4 — Deployment & Final Polish**

Turning the completed ML model into a **usable, tested, and deployable component**.
