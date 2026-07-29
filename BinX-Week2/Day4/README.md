# 📊 Day 4 — EDA Part 1: Distributions & Outliers

## 🎯 Learning Objectives

- Understand why Exploratory Data Analysis (EDA) is an essential step before Machine Learning modeling.
- Perform univariate analysis using Seaborn visualizations.
- Analyze distributions using histograms, box plots, count plots, and KDE plots.
- Detect potential outliers using the IQR method.
- Document insights and patterns discovered from the dataset.

---

# 📚 Topics Covered

## 🔍 4.1 What EDA Is and Why It Comes First

Exploratory Data Analysis (EDA) is the process of understanding a dataset before building Machine Learning models.

In this section, I learned:
- Why EDA is important.
- How to inspect data patterns and problems.
- Why understanding data comes before modeling.

---

## 📊 4.2 Seaborn: Statistical Visualization

Seaborn is a Python visualization library built on top of Matplotlib.

It helps create informative statistical plots with less code.

Used tools:

- Seaborn
- Matplotlib
- Pandas

Example:

```python
sns.histplot(data=df, x="value")
plt.show()
```

---

# 📈 4.3 Univariate Analysis

Univariate analysis focuses on analyzing one variable at a time.

I practiced different visualization techniques:

## 📊 Histogram

Used to understand the distribution of numeric variables.

```python
sns.histplot()
```

Reveals:
- Distribution shape
- Frequency
- Skewness

---

## 📦 Box Plot

Used to understand:

- Median
- Quartiles
- Potential outliers

```python
sns.boxplot()
```

---

## 📊 Count Plot

Used for categorical variables to show frequency.

```python
sns.countplot()
```

Helps identify:
- Most common categories
- Category imbalance

---

## 📉 KDE Plot

Shows a smooth estimation of the distribution.

```python
sns.kdeplot()
```

Helps understand:
- Distribution shape
- Data concentration

---

# 🎯 4.4 Outlier Detection with IQR Method

In this section, I learned how to detect potential outliers using the Interquartile Range (IQR).

Formula:

```
IQR = Q3 - Q1
```

Outlier boundaries:

```
Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR
```

Important note:

> An outlier is a question, not a verdict.

Outliers should be investigated before deciding whether to keep, modify, or remove them.

---

# 🧪 Hands-On Lab: Univariate EDA on a Real Dataset

Steps completed:

✅ Load and inspect a real dataset.

✅ Analyze numeric variables using histograms.

✅ Visualize distributions using box plots.

✅ Detect potential outliers using the IQR method.

✅ Analyze categorical variables using count plots.

✅ Document findings and observations using Markdown cells.

---

# 🛠️ Tools Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

# 🤖 AI Assistance Note

I used ChatGPT as a learning assistant to explore a new notebook design style and improve the Markdown formatting.

I experimented with different colors, layouts, and documentation styles to make the notebook more organized, readable, and easier to review.

This helped me improve not only my technical skills but also my documentation and presentation skills.

---

# 🚀 Git & GitHub

Completed:

- [x] Saved the notebook
- [x] Updated README.md
- [x] Added changes using Git
- [x] Created a commit
- [x] Pushed the work to GitHub