# 🚀 Day 1 — Sprint 1 Planning & Neural Network Architecture

> 🧠 **Week 6 | Deep Learning Foundations**
> ⏱️ **Duration:** 8 Hours
> 🎯 **Focus:** Sprint Planning • Baseline Model • Neural Network Architecture

---

## 🎯 Learning Objectives

By the end of this day, I will be able to:

* ✅ Complete Sprint 1 planning and establish a baseline model.
* 🧮 Explain how a neuron works using weighted inputs, bias, and an activation function.
* 🏗️ Understand input, hidden, and output layers in a neural network.
* 🔍 Explain what makes a neural network “deep.”
* ⚙️ Understand weights and biases as learnable parameters.

---

## 📚 1. Key Topics

| Topic                   | Description                                                   |
| ----------------------- | ------------------------------------------------------------- |
| 📋 Sprint Planning      | Define the sprint goal, backlog, and initial tasks.           |
| 📊 Baseline Model       | Establish a performance benchmark for future models.          |
| 🧠 Deep Learning        | Understand its strengths with complex, high-dimensional data. |
| 🔢 The Neuron           | Learn weighted sums, bias, and activation functions.          |
| 🏗️ Network Layers      | Explore input, hidden, and output layers.                     |
| ⚙️ Learnable Parameters | Understand how weights and biases change during training.     |

---

## 📋 2. Sprint 1 Planning & Baseline First

Sprint 1 begins with defining a clear goal and organizing the work into manageable backlog tasks.

### 📝 Main Tasks

* 📂 Finalize the project dataset.
* 🔎 Perform Exploratory Data Analysis (EDA).
* 🤖 Train a simple baseline model.
* 📈 Record the baseline evaluation metric.
* 🌿 Commit the notebook to a feature branch and open a draft Pull Request.

### 💡 Why Is a Baseline Important?

A baseline is a simple model used as a reference point for evaluating future models.

Every new model, including the neural network, should be compared against this benchmark to determine whether it actually improves performance.

> 📌 **Key Takeaway:** Without a baseline, it is difficult to measure whether a more complex model provides a real improvement.

---

## 🧠 3. Why Deep Learning?

Classical Machine Learning performs well on many structured datasets, especially tabular data. Deep Learning is particularly powerful for learning complex patterns from high-dimensional data.

### 🔍 Common Applications

* 🖼️ **Computer Vision:** Images and visual recognition.
* 📝 **Natural Language Processing (NLP):** Text understanding and language generation.
* 🔊 **Audio Processing:** Speech recognition and sound analysis.

### ⚖️ Classical ML vs. Deep Learning

| Classical ML                                  | Deep Learning                                            |
| --------------------------------------------- | -------------------------------------------------------- |
| Often effective for structured, tabular data. | Especially effective for complex, high-dimensional data. |
| May rely on manually engineered features.     | Can learn useful representations directly from data.     |
| Often requires fewer computational resources. | May require more data and computational power.           |

---

## 🔢 4. Understanding a Neuron

A neuron is the fundamental building block of a neural network.

It performs a weighted sum of its inputs, adds a bias, and applies an activation function.

### 🧮 The Mathematical Formula

$$
z = \sum_{i=1}^{n} x_i w_i + b
$$

$$
\text{output} = f(z)
$$

Where:

* 🔹 \(x_i\): Input feature.
* 🔹 \(w_i\): Weight assigned to the input.
* 🔹 \(b\): Bias.
* 🔹 \(z\): Weighted sum plus bias.
* 🔹 \(f\): Activation function.

### 💻 Python Example

```python
import numpy as np

# Define inputs, weights, and bias
inputs = np.array([2.0, 3.0])
weights = np.array([0.5, 0.8])
bias = 0.2

# Calculate the weighted sum
z = np.dot(inputs, weights) + bias

# Apply a ReLU activation function
output = max(0, z)

print("Weighted sum:", z)
print("Neuron output:", output)
```

**Expected output:**

```text
Weighted sum: 3.6
Neuron output: 3.6
```

💡 **Connection to Week 2:** The neuron uses the same dot product concept, combined with a bias and an activation function.

---

## 🏗️ 5. Neural Network Layers & Architecture

Neurons are organized into layers, allowing information to flow from the input toward the final prediction.

### 🔄 The Three Main Layer Types

**1. 📥 Input Layer**

* Receives the input features.
* Represents the data provided to the network.

**2. ⚙️ Hidden Layer(s)**

* Learn intermediate representations.
* Transform the input into increasingly useful features.
* More or wider layers can increase model capacity.

**3. 📤 Output Layer**

* Produces the final prediction.
* Its structure depends on the task, such as binary classification, multiclass classification, or regression.

### 🧩 What Does “Deep” Mean?

Deep Learning refers to neural networks with multiple hidden layers. Stacking layers allows a network to learn increasingly complex representations.

---

## ⚙️ 6. Weights & Biases: What Does the Network Learn?

Weights and biases are the trainable parameters of a neural network.

* 🎚️ **Weights:** Control the influence of input features.
* ➕ **Biases:** Allow the neuron to adjust its activation independently of the weighted inputs.
* 🔁 **Training:** Updates these parameters to reduce prediction errors.

A newly initialized network typically starts with randomly initialized parameters. During training, an optimization algorithm adjusts them based on the loss and its gradients.

📌 The next learning days will explore how predictions are evaluated and how these parameters are updated through training.

---

## 🧪 7. Hands-On Lab — Sprint 1 Kickoff & Baseline

### ✅ Practical Checklist

* [ ] 📋 Confirm the Sprint 1 goal and prioritize backlog tasks.
* [ ] 📂 Finalize the project dataset.
* [ ] 🔎 Complete a brief EDA in the project notebook.
* [ ] 🤖 Train a simple baseline model, such as Logistic Regression or Linear Regression, depending on the task.
* [ ] 📊 Evaluate the model using an appropriate metric.
* [ ] 📝 Document the baseline score in Markdown.
* [ ] 🌿 Commit the baseline notebook to a feature branch.
* [ ] 🔀 Open a draft Pull Request for review.

### 📈 Baseline Record

| Item              | Result                               |
| ----------------- | ------------------------------------ |
| Dataset           | To be documented                     |
| Baseline Model    | To be selected                       |
| Evaluation Metric | To be selected                       |
| Baseline Score    | To be recorded                       |
| Improvement Goal  | Beat the baseline using later models |

> 🎯 **Success Criteria:** Establish a reproducible baseline and document its evaluation metric before developing the neural network.

---

## 🛠️ 8. Tools & Technologies

* 🐍 **Python**
* 📊 **Pandas** — Data manipulation and analysis.
* 🤖 **Scikit-learn** — Baseline model training and evaluation.
* 📓 **Jupyter Notebook / Google Colab** — Interactive experimentation.
* 🌿 **Git & GitHub** — Version control and collaboration.

---

## 💡 9. Key Takeaways

* ✅ Sprint planning turns project goals into actionable tasks.
* 📊 A baseline provides a reference for measuring improvement.
* 🧠 A neuron combines a dot product, bias, and activation function.
* 🏗️ Neural networks organize neurons into input, hidden, and output layers.
* ⚙️ Training adjusts weights and biases to improve predictions.
* 🚀 Deep Learning builds on familiar mathematical operations rather than introducing an entirely new concept.

---

### 🎉 Day 1 Complete!

**Next Step:** Move toward understanding the neural network training process, including loss functions, optimization, and how model parameters are updated.

*📌 Note: Record actual project results and baseline metrics after completing the hands-on lab.*
