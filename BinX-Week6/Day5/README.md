# 🧠 Week 6 — Deep Learning & Neural Networks

> **AI & Machine Learning Track — BinX Tech**

---

## 🎯 Week Overview

This week focused on the fundamentals of **Deep Learning** and the practical implementation of Neural Networks using **TensorFlow / Keras**.

The work progressed from understanding neural network concepts and activation functions to training, tuning, evaluating, and reviewing a Neural Network for the **Cardiovascular Patient Monitoring System**.

---

## 📚 Topics Covered

* 🧠 Neural Networks fundamentals
* 🔄 Forward Propagation
* 🔥 Activation Functions
* 📉 Loss Functions
* ⚙️ Training Mechanics
* 📐 Learning Rate
* 🧩 Network Width & Depth
* 🛡️ Dropout
* 📦 Batch Size
* ⏹️ EarlyStopping
* 📊 Model Evaluation
* 🔍 Hyperparameter Tuning
* 🔀 Git Workflow & Pull Requests
* 🔄 Sprint Review & Retrospective

---


# 🚀 Sprint 1 — Neural Network Baseline & Tuning

## 🎯 Sprint Goal

Build a baseline Neural Network for the cardiovascular dataset, understand the training process, systematically tune the model, and evaluate the final model against the baseline.

---

## 🫀 Dataset

The project uses the cardiovascular dataset with:

* **70,000 samples**
* **12 input features**
* **Binary target:** `cardio`

The dataset was prepared using:

* One-hot encoding for categorical features
* Feature scaling with `StandardScaler`
* Stratified train/validation/test splitting

### Dataset Split

| Set        |         Shape |
| ---------- | ------------: |
| Training   | `(44800, 12)` |
| Validation | `(11200, 12)` |
| Test       | `(14000, 12)` |

---

# 🧠 Neural Network Architecture

The final tuned network uses:

* **Input Layer:** 12 features
* **Hidden Layer 1:** 32 neurons — ReLU
* **Hidden Layer 2:** 32 neurons — ReLU
* **Dropout:** 0.0
* **Output Layer:** 1 neuron — Sigmoid
* **Optimizer:** Adam
* **Learning Rate:** 0.001
* **Loss:** Binary Crossentropy
* **Batch Size:** 32
* **EarlyStopping:** patience = 5

---

# 🎛️ Hyperparameter Tuning

The network was tuned systematically by changing one hyperparameter at a time.

### Learning Rate

| Experiment           | Learning Rate | Best Validation Accuracy |
| -------------------- | ------------: | -----------------------: |
| Baseline             |         0.001 |                   72.74% |
| Lower Learning Rate  |        0.0005 |                   72.21% |
| Higher Learning Rate |         0.005 |                   72.71% |

### Width / Depth

| Experiment     | Hidden Units | Layers | Best Validation Accuracy |
| -------------- | -----------: | -----: | -----------------------: |
| Baseline       |           32 |      1 |                   72.44% |
| Wider Network  |           64 |      1 |                   72.65% |
| Deeper Network |           32 |      2 |               **72.89%** |

### Dropout

| Experiment  | Dropout | Best Validation Accuracy |
| ----------- | ------: | -----------------------: |
| No Dropout  |     0.0 |               **73.25%** |
| Dropout 0.2 |     0.2 |                   73.19% |
| Dropout 0.4 |     0.4 |                   72.96% |

### Batch Size

| Experiment     | Batch Size | Best Validation Accuracy |
| -------------- | ---------: | -----------------------: |
| Small Batch    |         32 |               **73.00%** |
| Baseline Batch |         64 |                   72.65% |
| Large Batch    |        128 |                   72.81% |

---

# ⏹️ EarlyStopping

EarlyStopping was applied to prevent unnecessary training and restore the best-performing model weights.

```python
EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True
)
```

### Training Results

* **Epochs Trained:** 16
* **Best Epoch:** 11
* **Best Validation Accuracy:** 73.04%
* **Best Validation Loss:** 0.5478

---

# 📊 Final Evaluation

The final Neural Network was compared with the baseline model using Accuracy, Precision, Recall, and F1 Score.

| Model                    |   Accuracy |  Precision |     Recall |   F1 Score |
| ------------------------ | ---------: | ---------: | ---------: | ---------: |
| **Baseline**             |     72.23% |     71.87% | **73.00%** |     72.43% |
| **Tuned Neural Network** | **73.05%** | **73.84%** |     71.36% | **72.57%** |

### 📈 Result

The tuned Neural Network achieved improvements in:

* Accuracy
* Precision
* F1 Score

The baseline model achieved slightly higher Recall.

---

# 🔄 Sprint 1 Retrospective

## ✅ What Went Well

* Successfully built and trained the Neural Network.
* Completed systematic hyperparameter tuning.
* Tested learning rate, network width/depth, dropout, and batch size.
* Applied EarlyStopping successfully.
* Compared the tuned model against the baseline.

## 🛠️ What Could Be Improved

* Additional error analysis is needed.
* More targeted model experiments could improve performance.
* Training experiments can be time-consuming in the current environment.

## 🎯 Sprint 2 Focus

Sprint 2 will focus on:

* Detailed error analysis
* Further model improvements
* Additional targeted experiments
* Final project documentation and visualization

---

# 🔀 Git & PR Workflow

Sprint 1 work was organized using a feature branch and Pull Request workflow.

```text
Feature Branch
      ↓
Development & Experiments
      ↓
Commit
      ↓
Push
      ↓
Pull Request
      ↓
Mentor Review
      ↓
Merge → main
```

---

# ✅ Week 6 Deliverables

* [x] Sprint 1 plan and baseline model
* [x] Activations and forward-pass notebook
* [x] Training mechanics and learning-rate experiments
* [x] Trained Keras Neural Network
* [x] Hyperparameter tuning experiments
* [x] EarlyStopping
* [x] Final model evaluation
* [x] Baseline vs. tuned model comparison
* [x] Sprint 1 retrospective
* [ ] Final PR review and merge

---

## 🏁 Conclusion

Week 6 covered the complete first Deep Learning workflow, from building a Neural Network and understanding its training process to systematic tuning, EarlyStopping, final evaluation, and Sprint review.

The final tuned Neural Network achieved **73.05% test accuracy**, providing a stronger baseline for the next Sprint.
