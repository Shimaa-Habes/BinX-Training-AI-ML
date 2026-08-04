# 📘 Week 3 - Day 3: Logistic Regression & Classification Metrics

Today I moved from predicting numbers to predicting categories. After
mastering Linear Regression yesterday, I learned that Logistic Regression
uses the same underlying math but adds a twist — the sigmoid function — to
turn a raw score into a probability, and then into a class decision.

## 📚 Logistic Regression

Logistic Regression is used when the target is a category, not a number
(for example: diabetic vs. not diabetic). Despite the name, it's a
classification model.

The workflow is:

- ⚖️ Compute the weighted sum of features (same as Linear Regression)
- 🌀 Pass it through the sigmoid function to get a probability (0 to 1)
- 🎯 Compare the probability to a threshold (usually 0.5) to decide the class

## ⚠️ Why Accuracy Isn't Enough

One of the most important lessons today was realizing that accuracy alone
can be misleading. On imbalanced data, a model can score very high accuracy
while completely failing at its actual job — for example, always predicting
"no diabetes" would still be right most of the time simply because most
patients don't have diabetes.

This is why classification needs richer evaluation tools.

## 🧮 The Confusion Matrix

The confusion matrix breaks predictions into four outcomes:

- ✅ True Positive (TP) — correctly predicted positive
- ✅ True Negative (TN) — correctly predicted negative
- 🚨 False Negative (FN) — missed a real positive case
- ⚠️ False Positive (FP) — false alarm

This matrix is the foundation for every other classification metric.

## 🎯 Precision, Recall & F1

- 📌 Precision: Of everything predicted positive, how much was actually right?
- 📌 Recall: Of all actual positives, how many did the model catch?
- 📌 F1-score: A balanced score combining precision and recall

I learned that choosing between precision and recall is a real decision
based on the problem, not just a formula. For example, in disease
screening, recall matters more (missing a real case is dangerous), while
in a spam filter, precision matters more (blocking a real email is worse
than letting spam through).

## 📉 AUC-ROC

The ROC curve shows the trade-off between catching positives and raising
false alarms across every possible threshold. The AUC (Area Under the
Curve) summarizes this into a single score between 0.5 (random guessing)
and 1.0 (perfect separation), making it a great way to judge a classifier
independent of any single threshold.

## 🧪 Hands-On Lab

Applied Logistic Regression on the Diabetes dataset:

- 📥 Loaded and prepared the dataset (encoded categorical columns)
- 🤖 Trained a Logistic Regression model
- 🔮 Generated predictions and class probabilities
- 🧮 Built the confusion matrix
- 📊 Computed precision, recall, and F1-score with classification_report
- ⚖️ Decided whether precision or recall matters more for this problem
- 📉 Computed the AUC-ROC score
- 💭 Interpreted all the results together

## 📈 Results

The model reached 96% accuracy, but the real story was in the details.
For the diabetic class specifically:

- 📌 Precision: 0.86
- 📌 Recall: 0.62
- 📌 F1-score: 0.72
- 📉 AUC-ROC: 0.9617

The confusion matrix showed 653 false negatives — real diabetic patients
the model missed — compared to only 166 false positives. This confirmed
that recall matters more here: missing a real diagnosis is riskier than a
harmless follow-up test for a false alarm.

Despite the moderate recall at the default threshold, the very high
AUC-ROC (0.9617) showed the model is excellent at ranking diabetic
patients as higher-risk than non-diabetic ones across all thresholds —
meaning the model's underlying signal is strong, and adjusting the
decision threshold could improve recall further.

## 🩺 Dataset

Diabetes Prediction Dataset containing patient information such as age,
BMI, hypertension, heart disease, smoking history, HbA1c level, blood
glucose level, and diabetes outcome.

## 🛠️ Tools

Python, NumPy, Pandas, Scikit-learn, Matplotlib, Jupyter Notebook