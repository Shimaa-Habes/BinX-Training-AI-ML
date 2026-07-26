# Day 3 — NumPy: Numerical Computing

> **Phase 1 · Week 1 · Day 3** — BinX Tech AI & ML Internship Program

---

## 🎯 Overview

Today I built the numerical foundation behind the entire AI/ML stack —
learning how NumPy arrays work and why they're the backbone of Pandas,
Scikit-learn, TensorFlow, and PyTorch.

---

## 📚 What I Learned

### 🤔 3.1 Why NumPy

Understood why `ndarray` is faster and more compact than Python lists —
operations run in optimized C code instead of Python loops.

### 🧱 3.2 Creating Arrays

Created arrays with `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`,
`np.linspace()`, and `np.random.rand()`.

### 🔍 3.3 Array Attributes, Indexing & Slicing

Explored `.shape`, `.dtype`, `.ndim`, and 2D indexing/slicing with `array[row, column]`.

### ⚡ 3.4 Vectorized Operations

Used vectorized math (`a * 2`, `a + a`, `a.mean()`) and boolean masking (`a[a > 2]`)
instead of manual loops.

### 📡 3.5 Broadcasting

Learned how NumPy combines arrays of different shapes without copying data —
e.g. adding a 1D row to every row of a 2D matrix.

---

## 🧪 Hands-On Lab

| #   | Task                                                            | Status |
| --- | --------------------------------------------------------------- | ------ |
| 1   | 🔢 Created a 4×4 array (1-16), printed shape and dtype          | ✔️     |
| 2   | ✂️ Sliced the array to extract second column and last row       | ✔️     |
| 3   | 🎭 Used a boolean mask to select values greater than the mean   | ✔️     |
| 4   | 📡 Added a 1D row to every row of a 2D array using broadcasting | ✔️     |

---

## 🧰 Tools Used

`Python 3.14` · `NumPy` · `Jupyter Notebook` · `VS Code`

---
