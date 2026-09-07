# 🌿 Week 8 · Day 2 — Text Representation

<p align="center">

<img src="https://img.shields.io/badge/Week%208-Day%202-355C4A?style=for-the-badge">
<img src="https://img.shields.io/badge/NLP-TF--IDF%20%26%20Embeddings-B88746?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Completed-6B7F72?style=for-the-badge">

</p>

<p align="center">

<strong>📚 Phase 3 · Sprint 3 · BinX Tech AI & ML Internship</strong>

</p>

---

## 🧭 Overview

Day 2 focuses on one of the most important steps in **Natural Language Processing (NLP)**:

> 💡 **How do we convert human language into numerical representations that machine learning models can understand?**

We explored two major approaches:

🟩 **TF-IDF** → represents the importance of words based on their frequency.

🟫 **Word Embeddings** → represent words as dense vectors that capture semantic relationships.

We also introduced **Contextual Embeddings** and connected them to the transformer concepts covered in **Week 7**.

---

## 🎯 Learning Objectives

By the end of this day, we learned how to:

* 🔢 Convert cleaned text into numerical vectors using **TF-IDF**
* 🧠 Understand how **word embeddings** capture semantic relationships
* 🔍 Work with **pre-trained GloVe embeddings**
* 📐 Explore **semantic geometry**
* 🔗 Find nearest words using vector similarity
* ⚖️ Compare **TF-IDF vs. Word Embeddings**
* 💬 Understand contextual meaning using **BERT**
* 🧩 Choose an appropriate representation based on the task

---

## 📖 Topics Covered

### 2.1 🔢 From Text to Numbers

We started by understanding why cleaned text cannot be directly processed by most machine learning models.

The text must first be transformed into numerical representations.

Two main families were introduced:

```text
📝 Cleaned Text
      │
      ├───────────────┐
      ↓               ↓
  📊 TF-IDF       🧠 Embeddings
      │               │
 Word Importance   Word Meaning
```

---

### 2.2 📊 Bag-of-Words & TF-IDF

We explored the **Bag-of-Words** approach and how TF-IDF improves simple word counts.

#### 🔍 TF-IDF

**TF — Term Frequency**

How frequently a word appears in a document.

**IDF — Inverse Document Frequency**

How rare the word is across the collection of documents.

Together:

```text
TF-IDF = Term Frequency × Inverse Document Frequency
```

✨ TF-IDF gives higher importance to words that are:

* 📄 Frequent in the current document
* 🔎 Rare across other documents

We implemented TF-IDF using:

```python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(cleaned_texts)
```

### 💡 Key Idea

TF-IDF is:

⚡ Fast
🎯 Simple
📊 Interpretable
💪 Strong as a baseline for text classification

However, it does not understand the actual meaning or order of words.

---

## 2.3 🧠 Word Embeddings

Word embeddings represent words as **dense numerical vectors**.

Instead of treating every word as completely independent, embeddings organize words in a vector space where semantically related words tend to be closer together.

### 📐 Semantic Geometry

A famous example is:

```text
king − man + woman ≈ queen
```

This demonstrates that the vector space can encode meaningful relationships between words.

---

### 🔬 Word2Vec & GloVe

We explored two classic embedding approaches:

| Method      | Main Idea                                             |
| ----------- | ----------------------------------------------------- |
| 🧠 Word2Vec | Learns word representations from surrounding words    |
| 🌐 GloVe    | Learns representations from global word co-occurrence |

For the hands-on lab, we loaded a pre-trained GloVe model using **Gensim**.

```python
from gensim.downloader import load

word_vectors = load("glove-wiki-gigaword-50")
```

---

## 🔎 Nearest Neighbors

We used the embedding space to find words that are most similar to a target word.

Example:

```text
👑 king
   ↓
   ├── prince
   ├── queen
   ├── emperor
   └── son
```

For another example:

```text
💻 computer
   ↓
   ├── computers
   ├── software
   ├── technology
   ├── electronic
   └── internet
```

Similarity was measured using **cosine similarity**.

---

## ⚖️ TF-IDF vs. Word Embeddings

| Feature                | 📊 TF-IDF       | 🧠 Word Embeddings |
| ---------------------- | --------------- | ------------------ |
| Representation         | Word importance | Word meaning       |
| Vector type            | Sparse          | Dense              |
| Captures meaning       | ❌ No            | ✅ Yes              |
| Semantic relationships | ❌ Limited       | ✅ Yes              |
| Fast to train          | ⚡ Yes           | ⚡ Depends          |
| Strong baseline        | ✅ Yes           | ➖ Depends          |
| Deep learning input    | ➖ Sometimes     | ✅ Yes              |

### 🧩 Main Difference

```text
📊 TF-IDF
"What words are important?"

        vs.

🧠 Embeddings
"How are these words related?"
```

---

## 2.4 🌐 Contextual Embeddings

Traditional embeddings such as Word2Vec assign **one fixed vector** to each word.

But a word can have different meanings depending on its context.

### 🏦 Example: "bank"

```text
"I sat near the bank of the river."
              ↓
        🌊 River meaning


"She deposited money in the bank."
              ↓
        💰 Financial meaning
```

A single fixed vector cannot fully represent both meanings.

### 🤖 BERT & Transformers

Contextual embeddings solve this problem by generating representations based on the surrounding words.

```text
Same word
   ↓
Different context
   ↓
Different representation
```

This connects directly to **Week 7**, where we explored transformer-based models and their ability to understand language through context.

---

# 🧪 Hands-On Lab

## Step 1 — 📊 TF-IDF Baseline

Applied TF-IDF to cleaned text and trained a simple classifier.

```text
📝 Cleaned Text
       ↓
✂️ Train / Test Split
       ↓
📊 TF-IDF
       ↓
🤖 Logistic Regression
       ↓
📈 Evaluation
       ↓
🎯 Baseline Metric
```

---

## Step 2 — 🧠 Pre-trained Embeddings

Loaded pre-trained GloVe embeddings and explored semantic relationships.

Tasks included:

* 📥 Loading GloVe
* 🔢 Inspecting word vectors
* 🔎 Finding nearest neighbors
* 📐 Exploring semantic geometry
* 📊 Comparing similarity scores

---

## Step 3 — 🔄 Model Comparison

The TF-IDF vs. LSTM/Transformer comparison was identified as **not applicable to CardioML**.

Why?

Because **CardioML is a structured tabular cardiovascular classification project**, not a text-based NLP project.

Therefore, there is no meaningful text representation pipeline to compare against the Week 7 LSTM/Transformer models.

---

## Step 4 — 🧩 Representation Decision

For **CardioML**:

> 🫀 The project uses structured numerical and categorical cardiovascular features rather than text, so TF-IDF and word embeddings are not appropriate as the primary feature representation.

For a text-based project:

```text
📊 TF-IDF
↓
Strong + Fast Baseline

🧠 Word Embeddings
↓
Semantic Representation

🤖 Contextual Embeddings
↓
Context-Aware Language Understanding
```

The appropriate representation depends on:

🎯 **The type of data**
🎯 **The task objective**
🎯 **The complexity of the language problem**

---

# 🛠️ Tools Used

<p align="center">

<img src="https://img.shields.io/badge/Python-3.13-355C4A?style=flat-square">
<img src="https://img.shields.io/badge/Scikit--learn-TF--IDF-B88746?style=flat-square">
<img src="https://img.shields.io/badge/Gensim-Embeddings-6B7F72?style=flat-square">
<img src="https://img.shields.io/badge/Jupyter-Notebook-203B2F?style=flat-square">

</p>

### Main Libraries

* 🐍 Python
* 📊 Scikit-learn
* 🔤 `TfidfVectorizer`
* 🧠 Gensim
* 🌐 Pre-trained GloVe embeddings
* 📓 Jupyter Notebook

---

# 📁 Project Structure

```text
Day2/
│
├── 📓 text_representation.ipynb
├── 🧪 hands_on_lab.ipynb
└── 📄 README.md
```

---

# 💡 Key Takeaways

### 📊 TF-IDF

> Represents **word importance** based on frequency across documents.

### 🧠 Word Embeddings

> Represent **word meaning and semantic relationships** using dense vectors.

### 🌐 Contextual Embeddings

> Represent a word differently depending on its **surrounding context**.

### 🎯 Representation Choice

> The best representation depends on the **data and the task**.

---

## 🏆 Day 2 Status

<p align="center">

### ✅ COMPLETED

**Text Representation: TF-IDF & Embeddings**

📊 TF-IDF
🧠 Word Embeddings
🌐 Contextual Embeddings
🔎 Semantic Similarity
🧪 Hands-On Lab

</p>

---

<p align="center">

<strong>🌿 Week 8 · Day 2 · BinX Tech AI & ML Internship</strong>

<br>

<em>From words → vectors → meaning.</em>

</p>

