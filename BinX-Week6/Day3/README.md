# 🧠 Week 6 — Day 3

## Backpropagation, Gradient Descent & Optimizers

> **AI & Machine Learning Track — Deep Learning | Sprint 1**

---

## 🎯 Learning Objectives

By the end of this day, I was able to:

- Describe the four-step neural network training loop.
- Explain gradient descent and the role of the learning rate.
- Understand backpropagation conceptually using the chain rule.
- Explain epochs, batches, and optimizers.
- Compare SGD and Adam.
- Train a neural network using TensorFlow/Keras.
- Analyze training and validation curves.
- Apply dropout to improve model generalization.

---

## 📚 Topics Covered

### 3.1 The Training Loop in One Picture

Training a neural network follows a repeated four-step loop:

**Forward → Loss → Backpropagation → Update**

1. **Forward** — The input passes through the network to produce a prediction.
2. **Loss** — The prediction is compared with the true target to measure the error.
3. **Backpropagation** — Gradients are calculated to determine how each weight contributed to the loss.
4. **Update** — The weights are adjusted using the gradients to reduce the loss.

This loop is repeated many times over batches and iterations so the model gradually learns better parameters.

---

### 3.2 Gradient Descent

Gradient descent is the optimization process used to reduce the loss.

The gradient points toward the direction of the **steepest increase in loss**. Gradient descent moves in the **opposite direction** to reach a lower-loss region.

**Foggy hillside intuition:**

- The gradient indicates the steepest uphill direction.
- We move in the opposite direction.
- Small repeated steps gradually take us toward a low-loss region.

---

### 3.3 The Learning Rate

The learning rate controls the size of each update made during gradient descent.

| Learning Rate | Effect |
|---|---|
| Too High | Can overshoot the minimum and make training unstable |
| Too Low | Training becomes very slow |
| Just Right | Produces steady and efficient learning |

The learning rate is one of the most important hyperparameters in deep learning.

A practical starting point when using Adam is around:

```text
0.001
```

---

### 3.4 Backpropagation

Backpropagation calculates the gradients needed to update the network weights.

It works backward from the loss and determines how much each weight contributed to the final error. The chain rule is used to connect the effect of each weight through the different layers of the network.

A useful intuition:

> Backpropagation assigns blame to the weights that contributed to the error.

The calculations do not need to be implemented manually because deep learning frameworks handle them automatically:

- **PyTorch:** `autograd`
- **TensorFlow:** `GradientTape`

---

### 3.5 Optimizers, Epochs, and Batches

| Term | Meaning |
|---|---|
| **Optimizer** | Uses the gradients to update the network weights |
| **Epoch** | One complete pass through the entire training dataset |
| **Batch** | A subset of training samples processed before a weight update |

**SGD vs. Adam**

- **SGD** — Basic gradient descent approach.
- **Adam** — Adapts the update size for individual weights and is a strong practical default.

**Practical rule:** Use Adam as a reliable starting optimizer and begin with a learning rate around `0.001`. Adjust the learning rate only if the loss curve behaves poorly.

---

## 🧪 Hands-On Lab — Training a Neural Network

For the practical lab, I trained a neural network for the **Cardio classification** task using the `heart_disease_uci.csv` dataset.

### 📊 Dataset

- **Samples:** 70,000
- **Features:** 12
- **Target:** `cardio`
- **Task:** Binary Classification
- **Classes:** 0 and 1

The dataset was loaded using the semicolon separator:

```python
df = pd.read_csv("heart_disease_uci.csv", sep=";")
```

The features were separated from the target, split into training and test sets using stratification, and standardized before training.

---

### 🧩 Step 1 — Build the Neural Network

A Keras `Sequential` network was created with:

- Input layer
- Dense layer with 64 neurons and ReLU activation
- Dense layer with 32 neurons and ReLU activation
- Output layer with 1 neuron and Sigmoid activation

The sigmoid output is appropriate because the task is binary classification.

---

### ⚙️ Step 2 — Compile and Train

The model was compiled using:

```python
Adam(learning_rate=0.001)
```

with loss function:

```python
binary_crossentropy
```

**Training configuration:**

- Epochs: 30
- Batch size: 32
- Validation split: 20%

**Observation:** The model learned quickly during the early epochs and then reached a relatively stable validation performance.

---

### 📈 Step 3 — Training and Validation Curves

Training and validation loss and accuracy were plotted using the Keras `History` object.

**Observations:**

- Training accuracy increased from approximately **68.94%** to **73.93%**.
- Validation accuracy reached a best value of approximately **74.14%** around Epoch 8.
- Validation performance remained mostly around **73–74%** afterward.
- Validation loss showed some fluctuations after the earlier epochs.

Overall, the model showed reasonable learning without severe overfitting.

---

### 🛡️ Step 4 — Dropout Experiment

Dropout layers were added to the network to test whether regularization could improve generalization.

**Improved architecture:**

```text
Dense(64, ReLU)
Dropout(0.30)
Dense(32, ReLU)
Dropout(0.20)
Dense(1, Sigmoid)
```

The new training curves were compared with the baseline model using:

- Validation loss
- Validation accuracy
- Generalization behavior

---

### 🧪 Step 5 — Final Evaluation

The final neural network was evaluated on the unseen test set and compared with the Day 1 baseline.

**Results:**

| Model | Accuracy |
|---|---|
| Day 1 Baseline | 59.78% |
| Neural Network | 73.19% |
| **Improvement** | **+13.41 percentage points** |

The neural network achieved **73.19%** test accuracy, which is **13.41 percentage points** higher than the Day 1 baseline.

---

## 💡 Key Takeaways

- Neural network training follows a repeated **Forward → Loss → Backpropagation → Update** loop.
- Gradient descent moves in the direction that reduces the loss.
- The learning rate controls the size of each weight update.
- Backpropagation uses the chain rule to calculate gradients efficiently.
- Adam is a useful default optimizer for many neural network tasks.
- Validation curves help diagnose model behavior and generalization.
- Dropout can be used as a regularization technique to reduce overfitting.
- The neural network significantly improved the Day 1 baseline on the cardiac classification task.

---

## 🛠️ Tools Used

- Python
- NumPy
- Pandas
- Scikit-learn
- TensorFlow / Keras
- Matplotlib
- Jupyter Notebook
- VS Code
- Git & GitHub

---

## 📁 Files

```text
Day3/
├── README.md
├── hands_on_lab.ipynb
└── backprop_optimizers.ipynb
```