# 🚀 Week 1 — Python & Data Science Foundations

**Phase 1 · Week 1 — BinX Tech AI & ML Internship Program**

---

## 📝 Overview

Week 1 was all about building a solid foundation before jumping into any real AI or ML work. I set up my environment, got comfortable with Python, and learned the four tools I'll be using throughout the entire program — NumPy, Pandas, and Matplotlib — all inside Jupyter Notebook, with everything saved and pushed to GitHub by the end of each day.

---

## 📅 What I Did Each Day

### 🛠️ Day 1 — Setting Up My Environment

The first thing I did was set up a clean Python environment using `venv` and `pip` so my project dependencies stay isolated and reproducible. I installed the core libraries, froze everything into `requirements.txt`, and built my first notebook mixing Markdown notes with actual running code. Then I pushed it all to GitHub — first commit done!

### 🐍 Day 2 — Python Basics for Data Science

I went through Python's building blocks: the 8 data types, `if/else` conditions, `for` loops, writing my own functions with docstrings, cleaning up loops into one-line list comprehensions, and building a simple class. These are the same patterns used by Scikit-learn and PyTorch under the hood, so it felt important to really understand them.

### 🔢 Day 3 — NumPy: Working with Arrays

I learned why NumPy is the backbone of the entire AI/ML world. I practiced creating arrays in different ways, explored how indexing and slicing works in 2D, replaced loops with vectorized operations, used boolean masking to filter data, and understood broadcasting — which honestly took a minute to click but makes total sense once you see it.

### 📊 Day 4 — Pandas: Real Data

This was the first time I worked with a real dataset. I loaded a CO2 emissions dataset, inspected it, filtered rows, handled missing values, and used `groupby()` to find average emissions per country. It felt much more like actual data work than anything before.

### 📈 Day 5 — Matplotlib & Putting It All Together

I learned the four main plot types — line, scatter, bar, and histogram — and how to combine them into one figure with subplots. Then I closed the week by building a mini-notebook that chains everything together: load the data with Pandas, process it with NumPy, and visualize it with Matplotlib. That's the pipeline I'll keep using for the rest of the program.

---

## 🧪 Week 1 Mini-Notebook — What I Built

I applied everything from the week to the CO2 emissions dataset:

**Step 1 — Load & Clean**
Loaded the dataset and checked for missing values before and after cleaning. It turned out the data was already clean — 13,953 rows, no nulls.

**Step 2 — NumPy Feature Engineering**
Calculated the mean and standard deviation of CO2 values, then added a `z_score` column to show how far each record sits from the average.

**Step 3 — Three Labeled Plots**

- 📊 Histogram — to see how CO2 values are distributed
- 🔵 Scatter plot — CO2 value vs. year
- 📶 Bar chart — top 10 countries/regions by average CO2

**Step 4 — What the Charts Actually Show**

- _Histogram:_ Most records have low CO2 values, but a few large countries/regions push the average way up — classic right skew.
- _Scatter:_ No clear trend across all countries combined, but the highest-emitting entities seem to be emitting more in recent years.
- _Bar:_ The "top 10" are actually aggregated regions like "World" and "High income" — not individual countries. That tells me I'd need to filter those out for any proper country-level comparison.

---

## ✅ What I Submitted

| #   | Deliverable                                             | Status |
| --- | ------------------------------------------------------- | ------ |
| 1   | Reproducible Python environment with `requirements.txt` | ✔️     |
| 2   | Python fundamentals notebook                            | ✔️     |
| 3   | NumPy notebook                                          | ✔️     |
| 4   | Pandas notebook                                         | ✔️     |
| 5   | Week 1 mini-notebook (NumPy + Pandas + Matplotlib)      | ✔️     |
| 6   | Everything committed to GitHub with clear messages      | ✔️     |

---

## 🧰 Tools I Used

`Python 3.14` · `venv` · `pip` · `NumPy` · `Pandas` · `Matplotlib` · `Jupyter Notebook` · `VS Code` · `Git & GitHub`

---

## 💡 Biggest Takeaway

> Every project this week followed the same shape: **load → process → visualize**. That pipeline, combined with clean code, documented notebooks, and a reproducible environment, is the foundation everything else in this program builds on.

---

## 📓 Appendix — Mini-Notebook Code

### Step 1: Load and clean the dataset with Pandas

```python
lab_df = pd.read_csv("data.csv")

print("Shape before cleaning:", lab_df.shape)
print("\nMissing values per column:\n", lab_df.isnull().sum())

lab_df = lab_df.dropna()

print("\nShape after cleaning:", lab_df.shape)
```

### Step 2: Use NumPy to compute a derived feature or summary statistic

```python
# compute overall mean and standard deviation of CO2 values using NumPy
mean_co2 = np.mean(lab_df["value"])
std_co2 = np.std(lab_df["value"])

print("Mean CO2 value:", mean_co2)
print("Standard deviation:", std_co2)

# derived feature: how many standard deviations each value is from the mean (z-score)
lab_df["z_score"] = (lab_df["value"] - mean_co2) / std_co2
lab_df[["country_name", "year", "value", "z_score"]].head()
```

### Step 3: Produce at least three labeled plots exploring the data

```python
plt.hist(lab_df["value"], bins=30, color="green")
plt.xlabel("CO2 Value")
plt.ylabel("Frequency")
plt.title("Distribution of CO2 Emission Values")
plt.show()
```

```python
plt.scatter(lab_df["year"], lab_df["value"], color="green", alpha=0.3)
plt.xlabel("Year")
plt.ylabel("CO2 Value")
plt.title("CO2 Value vs Year")
plt.show()
```

```python
top10 = lab_df.groupby("country_name")["value"].mean().sort_values(ascending=False).head(10)

plt.bar(top10.index, top10.values, color="green")
plt.xlabel("Country")
plt.ylabel("Average CO2 Value")
plt.title("Top 10 Countries by Average CO2 Value")
plt.xticks(rotation=45, ha="right")
plt.show()
```

### Step 4: Interpretation of each visualization

**Histogram — Distribution of CO2 Emission Values:**
The distribution is heavily right-skewed — most records have relatively low CO2 values, while a small number of records (large countries/regions) have extremely high values, pulling the mean well above the median.

**Scatter — CO2 Value vs Year:**
There is no strong linear trend visible across all countries combined, since values vary massively by country. However, the spread of high-value points appears to widen slightly in more recent years, suggesting increasing emissions among the highest-emitting entities over time.

**Bar — Top 10 Countries by Average CO2 Value:**
The top entities are dominated by large aggregated regions (e.g. "World", "High income", "IDA & IBRD total", "OECD members") rather than individual countries, reflecting that this dataset includes both country-level and regional/group-level records. This highlights the need to separate individual countries from aggregate groups for more precise country-level analysis.
