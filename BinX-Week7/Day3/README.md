# 🧠 Week 7 · Day 3 — Sequence Modeling

> 🔄 **From remembering patterns to understanding sequences.**

Day 3 focused on **Recurrent Neural Networks**, moving from the limitations of plain RNNs to more powerful sequence models such as **LSTMs**.
The practical work was applied to **ECG heartbeat sequences** from the MIT-BIH dataset. 🫀📈

---

## 🎯 Day 3 Goals

During this day, the main goals were to:

* 🔄 Understand how RNNs process sequential data
* 🧠 Understand the hidden state as the RNN's memory
* ⚠️ Explore the Vanishing Gradient Problem
* 🚀 Understand why LSTMs were introduced
* 🫀 Apply LSTM to ECG sequence classification
* 📊 Compare sequential models using validation and test accuracy
* 🔍 Prepare the notebook for Mentor Review

---

## 🔄 3.2 Recurrent Neural Networks

RNNs are designed to work with **sequential data**, where the order of information matters.

Instead of processing all inputs independently, an RNN processes the sequence step by step while carrying information from previous time steps through a **hidden state**.

The hidden state acts as a form of memory:

**Input → Hidden State → Updated Hidden State → Next Step**

This allows the model to use information from earlier parts of a sequence when making predictions.

### ⚠️ The Limitation

Plain RNNs can struggle with long sequences because information has to pass through many recurrent steps during training.

This can lead to the **Vanishing Gradient Problem**, where gradients become very small and the model gradually loses information from earlier time steps.

---

## 🧠 3.3 The Vanishing Gradient Problem

When a sequence is long, the gradient must travel backward through many time steps.

Because the gradient can repeatedly become smaller, information from earlier steps may have very little influence on the model's updates.

As a result:

> **Plain RNNs may forget information from far back in the sequence.**

This limitation motivated the development of more advanced recurrent architectures such as **LSTM** and **GRU**.

---

## 🚀 3.4 LSTMs and GRUs

### 🧠 LSTM

LSTM stands for **Long Short-Term Memory**.

It was designed to solve the problem of retaining important information over longer sequences.

An LSTM uses gates to control the flow of information:

* 🗑️ **Forget Gate** → decides what information should be removed
* 📥 **Input Gate** → decides what new information should be stored
* 📤 **Output Gate** → decides what information should be passed forward

This controlled memory allows LSTMs to preserve useful information across longer sequences.

### ⚡ GRU

GRU stands for **Gated Recurrent Unit**.

It provides a simpler recurrent architecture with fewer gates than an LSTM.

GRUs generally:

* ⚡ Use fewer parameters
* 🚀 Can train faster
* 🧩 Have a simpler architecture
* 🎯 Can achieve performance similar to LSTMs on many tasks

---

## 🫀 Connection to the Project

The practical application used **ECG heartbeat sequences** from the MIT-BIH dataset.

ECG signals are naturally sequential: each measurement is connected to measurements that come before and after it.

Therefore, the **order of the measurements carries useful information**.

An LSTM can process these measurements in sequence and learn temporal patterns that help distinguish between heartbeat classes.

### 🔗 Model Flow

**ECG Sequence → LSTM → Dense → Heartbeat Class**

---

## 🧪 Hands-On Experiment

The hands-on lab focused on training and evaluating an LSTM model on the sequential ECG dataset.

### 📊 LSTM Results

| Metric                   |     Result |
| ------------------------ | ---------: |
| Best Validation Accuracy | **92.98%** |
| Test Accuracy            | **92.96%** |
| Epochs                   |     **10** |

The model reached its best validation accuracy at **92.98%**, while the final test accuracy was **92.96%**.

This shows that the LSTM was able to learn useful patterns from the ECG sequences and generalize well to unseen test data.

---

## 🔍 RNN vs LSTM

A plain RNN was also tested as a sequential baseline.

The comparison highlighted the difference between a basic recurrent architecture and a gated recurrent architecture.

| Model        | Best Validation Accuracy | Test Accuracy |
| ------------ | -----------------------: | ------------: |
| 🔄 Plain RNN |               **13.87%** |    **82.76%** |
| 🧠 LSTM      |               **92.98%** |    **92.96%** |

The LSTM achieved substantially better validation performance than the plain RNN in this experiment.

This supports the idea that **gated memory mechanisms can help recurrent models handle sequential information more effectively**.

---

## 💡 Key Learning

The most important takeaway from Day 3 was that **not all sequential models handle memory in the same way**.

A plain RNN carries information through a hidden state, but its ability to preserve information over long sequences can be limited.

LSTMs improve this by introducing gates that control:

**what to forget → what to keep → what to output**

For ECG sequences, this order-aware processing allowed the LSTM to learn meaningful temporal patterns and achieve strong classification performance. 🫀📈

---

## 🔍 Mentor Code & Notebook Review

The final work was prepared for Mentor Review through GitHub.

### 📌 Review Workflow

1. 💻 Complete the Day 3 notebooks
2. 🌿 Push the work to the feature branch
3. 🔀 Open a Pull Request
4. 👨‍🏫 Assign the mentor for review
5. 📝 Address mentor feedback
6. 📚 Document feedback and implemented changes in Markdown

---

## 📁 Day 3 Files

* `rnn_lstm.ipynb` → RNN and LSTM experiments
* `hands_on_lab.ipynb` → Hands-On Lab and model comparison
* `README.md` → Day 3 documentation
* ECG dataset files → MIT-BIH / PTBDB data used for the experiments

---

## 🏁 Day 3 Summary

**RNN → Hidden State → Vanishing Gradients → LSTM → ECG Sequence Classification**

Day 3 connected the theoretical concepts of recurrent neural networks with a real sequential classification task.

The main lesson:

> 🧠 **When the order of information matters, the model needs a way to remember that order.**

And LSTM provides a much stronger mechanism for doing exactly that. 🚀🫀
