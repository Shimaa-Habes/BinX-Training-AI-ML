# Day 4 — Pandas: Tabular Data

> **Phase 1 · Week 1 · Day 4** — BinX Tech AI & ML Internship Program

---

## 🎯 Overview

Today I learned how to work with tabular data using Pandas — loading,
inspecting, filtering, cleaning, and aggregating real-world data
(global CO2 emissions dataset).

---

## 📚 What I Learned

### 📦 4.1 Series and DataFrames

Understood the difference between a `Series` (single labeled column)
and a `DataFrame` (full table).

### 📥 4.2 Loading and Inspecting Data

Loaded a CO2 emissions dataset with `read_csv()` and inspected it using
`.head()`, `.shape`, `.info()`, and `.describe()`.

### 🔍 4.3 Selecting and Filtering

Selected single/multiple columns and filtered rows using boolean
conditions and `.loc`.

### 🧹 4.4 Cleaning Data

Checked for missing values and duplicates using `.isnull().sum()` and
`.duplicated()` — dataset was already clean.

### 📊 4.5 Grouping and Aggregation

Used `groupby()` and `.agg()` to compute average CO2 emissions per country.

---

## 🧪 Hands-On Lab

| #   | Task                                                      | Status |
| --- | --------------------------------------------------------- | ------ |
| 1   | 📂 Loaded CO2 dataset, reported shape/columns/dtypes      | ✔️     |
| 2   | 🔎 Checked missing values (none found) with justification | ✔️     |
| 3   | 🎯 Filtered data above mean value and analyzed subset     | ✔️     |
| 4   | 📈 Grouped by country to find top CO2 emitters            | ✔️     |

---

## 🧰 Tools Used

`Python 3.14` · `Pandas` · `Jupyter Notebook` · `VS Code`

---
