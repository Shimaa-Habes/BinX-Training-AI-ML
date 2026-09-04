# 🧠 CardioML — Week 7 · Day 5

### 🚀 Sprint 2 Close-Out · From Experiments to a Better Core Model

<p align="center">
  <img src="https://img.shields.io/badge/BinX%20Tech-AI%20%2F%20ML%20Internship-0F766E?style=for-the-badge&logo=googlecolab&logoColor=white" alt="BinX Tech">
  <img src="https://img.shields.io/badge/Week%207-Day%205-164E43?style=for-the-badge" alt="Week 7 Day 5">
  <img src="https://img.shields.io/badge/Sprint%202-COMPLETED-138A78?style=for-the-badge" alt="Sprint 2">
</p>

<p align="center">

> **✨ Experiments → Evidence → Evaluation → Review**

</p>

---

## 🌿 The Mission

Sprint 2 was not about making the model **more complicated**.

It was about making the model **more intentional**.

The goal was to take the CardioML core model, improve its architecture, systematically experiment with important hyperparameters, evaluate the results correctly, and finish the sprint with a model that provides measurable improvement over the Week 6 baseline.

---

## 🫀 CardioML at a Glance

| 🔎 Item                 | 📌 Details                                 |
| ----------------------- | ------------------------------------------ |
| **Dataset**             | Cardiovascular Disease Dataset             |
| **Records**             | 70,000                                     |
| **Data Type**           | Structured / Tabular                       |
| **Task**                | Binary Classification                      |
| **Target**              | `cardio`                                   |
| **Core Model**          | Dense Neural Network                       |
| **Evaluation Metric**   | Test Accuracy                              |
| **Validation Strategy** | Stratified Train / Validation / Test Split |

---

# 🧭 Sprint 2 Roadmap

```text
┌──────────────────────┐
│  01 · Architecture   │
│  Match model to data │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│  02 · Experiments    │
│  Tune the core model │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│  03 · Evaluation     │
│  Compare performance │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│  04 · Review         │
│  Document & reflect  │
└──────────┬───────────┘
           ↓
       🏁 SPRINT 2
        COMPLETE
```

---

# 🏗️ 01 · Architecture Decision

### Why a Dense Neural Network?

CardioML contains **structured patient-level features** rather than images, audio, or sequential text.

Therefore:

```text
📊 Tabular Data
      ↓
🧠 Dense Neural Network
      ↓
⚡ Feature Interactions
      ↓
🎯 Binary Classification
      ↓
🔵 Sigmoid Output
```

### ❌ Why not CNN?

CNNs are primarily designed to capture spatial patterns such as those found in images.

### ❌ Why not LSTM / GRU?

LSTM and GRU architectures are designed for sequential or temporal dependencies.

### ✅ Final Decision

> **The architecture was selected based on the structure of the data — not on model complexity.**

---

# 🧬 02 · The Improved Core Model

The Sprint 2 model uses a deeper and more regularized Dense architecture:

```text
Input
  │
  ▼
Dense(128) + ReLU
  │
Batch Normalization
  │
Dropout(0.20)
  │
  ▼
Dense(64) + ReLU
  │
Batch Normalization
  │
Dropout(0.20)
  │
  ▼
Dense(32) + ReLU
  │
Batch Normalization
  │
Dropout(0.10)
  │
  ▼
Dense(1) + Sigmoid
  │
  ▼
🎯 Cardio Prediction
```

### 🛡️ Why these layers?

| Component            | Purpose                           |
| -------------------- | --------------------------------- |
| `Dense`              | Learns feature relationships      |
| `ReLU`               | Introduces non-linearity          |
| `BatchNormalization` | Stabilizes and improves training  |
| `Dropout`            | Helps reduce overfitting          |
| `Sigmoid`            | Produces binary-class probability |

---

# 🧪 03 · Controlled Experiments

Instead of changing everything at once, Sprint 2 used controlled experiments where the main architecture remained consistent while selected hyperparameters were changed.

| Experiment        | Learning Rate | Batch Size | Dropout  | Best Val. Accuracy |
| ----------------- | ------------: | ---------: | -------- | -----------------: |
| 🧪 Experiment 1   |       `0.001` |       `64` | Standard |         **73.44%** |
| 🧪 Experiment 2   |      `0.0005` |       `64` | Standard |         **73.29%** |
| 🧪 Experiment 3 ⭐ |       `0.001` |       `32` | Standard |         **73.48%** |
| 🧪 Experiment 4   |       `0.001` |       `64` | Reduced  |         **73.43%** |

---

# 🏆 04 · Best Configuration

## ⭐ Experiment 3

The best configuration was selected using **validation performance**, keeping the test set unseen for final evaluation.

```text
Learning Rate     → 0.001
Batch Size        → 32
Maximum Epochs    → 30
Early Stopping    → Enabled
Reduce LR         → Enabled
```

### 📈 Validation Results

| Metric                   |       Result |
| ------------------------ | -----------: |
| Best Validation Accuracy |   **73.48%** |
| Best Validation Loss     | **0.544566** |

---

# 📊 05 · Final Performance

### Week 6 → Sprint 2

| Stage              | Test Accuracy |
| ------------------ | ------------: |
| 🟦 Week 6 Baseline |    **73.02%** |
| ⚪ Sprint 1         |       **N/A** |
| 🟩 Sprint 2        |    **73.18%** |

### 📌 Improvement

```text
Week 6 Baseline
      73.02%
         │
         │  +0.16 percentage points
         ▼
Sprint 2
      73.18%
```

> 🎯 Sprint 2 achieved a **small but measurable improvement** over the Week 6 baseline.

The Sprint 2 model was selected using validation performance, while the test set was reserved for the final evaluation.

---

# 📉 06 · Training Behavior

Training and validation curves were reviewed to understand how the selected model learned across epochs.

### 🔍 What we monitored

* Training Accuracy
* Validation Accuracy
* Training Loss
* Validation Loss
* Possible signs of overfitting
* Possible signs of underfitting
* Effect of training duration

> 📈 The training curves provide additional evidence alongside the final numerical metrics.

---

# 🧠 07 · What Went Well

### ✅ Architecture

The model architecture was selected according to the tabular nature of CardioML.

### ✅ Controlled Experiments

Four configurations were trained and compared rather than changing multiple variables randomly.

### ✅ Model Selection

Validation performance was used to select the strongest configuration.

### ✅ Evaluation

The final selected model was evaluated on the unseen test set.

### ✅ Documentation

Architecture decisions, experiments, training behavior, metrics, and conclusions were documented throughout the sprint.

---

# 🔧 08 · What Can Be Improved?

Sprint 2 showed that the current model still has significant room for improvement.

### 🔬 Next areas to investigate

* Wider hyperparameter search
* Different network depths
* Alternative dropout rates
* Learning-rate optimization
* Batch-size optimization
* Additional feature engineering
* More systematic regularization experiments
* Better analysis of validation behavior

---

# 🚀 09 · Sprint 3 — Next Move

## 🎯 One Concrete Change

Sprint 3 will move from manual experimentation toward a **more systematic hyperparameter optimization strategy**.

```text
Learning Rate
      +
Batch Size
      +
Network Depth
      +
Dropout
      +
Training Duration
      ↓
Systematic Search
      ↓
Validation Performance
      ↓
🏆 Strongest Configuration
      ↓
Final Unseen Test Evaluation
```

### The objective:

> **Search smarter, not just harder.**

---

# 🧾 10 · Sprint 2 Deliverables

```text
✅ Architecture Decision
✅ Improved Dense Neural Network
✅ Experiment 1
✅ Experiment 2
✅ Experiment 3
✅ Experiment 4
✅ Best Model Selection
✅ Training Curves
✅ Metric Comparison
✅ Sprint Review
✅ Retrospective
```

---

# 🔐 11 · Reproducibility

The experiments use a fixed random state for the dataset split:

```python
random_state = 42
```

The data is divided using stratification to preserve the target distribution across the training, validation, and test sets.

---

# 📁 12 · Notebook Structure

```text
Week 7/
│
├── Day 5/
│   ├── hands_on_lab.ipynb
│   └── README.md
│
└── ...
```

The main hands-on implementation is contained in:

```text
📓 hands_on_lab.ipynb
```

---

# 🏁 Sprint 2 Status

<p align="center">

### 🟢 EXPERIMENTS COMPLETE

### 🟢 MODEL SELECTED

### 🟢 EVALUATION COMPLETE

### 🟢 REVIEW DOCUMENTED

### 🟡 PR / MENTOR APPROVAL

</p>

---

# 💭 Final Reflection

> **Sprint 2 was not about chasing a bigger number.**
>
> It was about learning how to improve a model through controlled experimentation, validation-based selection, proper evaluation, and evidence-driven decisions.

```text
                 ┌───────────────┐
                 │   CardioML    │
                 └───────┬───────┘
                         │
                  Understand Data
                         │
                         ▼
                Choose Architecture
                         │
                         ▼
                  Run Experiments
                         │
                         ▼
                  Validate Models
                         │
                         ▼
                   Select Best
                         │
                         ▼
                   Test Unseen Data
                         │
                         ▼
                   Review & Reflect
                         │
                         ▼
                      🚀 SPRINT 3
```

---

<p align="center">

**🧠 Learn → 🧪 Experiment → 📊 Measure → 🔍 Analyze → 🚀 Improve**

### Built during the BinX Tech AI / ML Internship

</p>
