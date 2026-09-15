# 🩺 Day 3 — Interactive Streamlit Dashboard

<p align="center">
  <strong>Turning a Machine Learning Model into an Interactive Web Dashboard</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-1.63.0-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/scikit--learn-1.9.0-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">
  <img src="https://img.shields.io/badge/Joblib-1.5.3-green?style=for-the-badge">
</p>

---

## 🌟 Overview

Day 3 focuses on building an **interactive Streamlit dashboard** around the Breast Cancer classification model trained during Day 1.

Instead of interacting with the model only through Python code or an API, the Streamlit application provides a simple user interface where users can:

> ✏️ Enter feature values → ⚙️ Process the data → 🤖 Generate a prediction → 📊 Understand the result

The dashboard uses the saved model and scaler from **Day 1** and presents the prediction in a clear, user-friendly interface.

---

## 🎯 Learning Objectives

By the end of this day, we completed the following:

- 🖥️ Built a Streamlit application.
- 📦 Loaded the trained `model.joblib`.
- ⚙️ Loaded the saved `scaler.joblib`.
- 🔢 Added input widgets for all **30 features**.
- 🔄 Applied the same preprocessing used during training.
- 🤖 Generated predictions using the trained model.
- 📊 Displayed prediction probabilities.
- 🧪 Tested the application locally.
- 🔍 Reviewed the interface from a first-time user's perspective.
- 🚀 Prepared the dashboard for mentor code review.

---

## 🗂️ Project Structure

```text
BinX-Week9/
│
├── 📁 Day1/
│   ├── 🤖 model.joblib
│   └── ⚙️ scaler.joblib
│
├── 📁 Day2/
│   └── 🚀 main.py
│
└── 📁 Day3/
    ├── 🖥️ streamlit_app.py
    └── 📓 Day3.ipynb
```

---

# 🖥️ Dashboard Features

## 🔢 30 Numeric Input Features

The dashboard collects all 30 features from the Breast Cancer Wisconsin dataset using Streamlit input widgets.

### 📌 Mean Features

| Feature                | Input           |
| ---------------------- | --------------- |
| Mean Radius            | 🔢 Number Input |
| Mean Texture           | 🔢 Number Input |
| Mean Perimeter         | 🔢 Number Input |
| Mean Area              | 🔢 Number Input |
| Mean Smoothness        | 🔢 Number Input |
| Mean Compactness       | 🔢 Number Input |
| Mean Concavity         | 🔢 Number Input |
| Mean Concave Points    | 🔢 Number Input |
| Mean Symmetry          | 🔢 Number Input |
| Mean Fractal Dimension | 🔢 Number Input |

### 📌 Error Features

| Feature                 | Input           |
| ----------------------- | --------------- |
| Radius Error            | 🔢 Number Input |
| Texture Error           | 🔢 Number Input |
| Perimeter Error         | 🔢 Number Input |
| Area Error              | 🔢 Number Input |
| Smoothness Error        | 🔢 Number Input |
| Compactness Error       | 🔢 Number Input |
| Concavity Error         | 🔢 Number Input |
| Concave Points Error    | 🔢 Number Input |
| Symmetry Error          | 🔢 Number Input |
| Fractal Dimension Error | 🔢 Number Input |

### 📌 Worst Features

| Feature                 | Input           |
| ----------------------- | --------------- |
| Worst Radius            | 🔢 Number Input |
| Worst Texture           | 🔢 Number Input |
| Worst Perimeter         | 🔢 Number Input |
| Worst Area              | 🔢 Number Input |
| Worst Smoothness        | 🔢 Number Input |
| Worst Compactness       | 🔢 Number Input |
| Worst Concavity         | 🔢 Number Input |
| Worst Concave Points    | 🔢 Number Input |
| Worst Symmetry          | 🔢 Number Input |
| Worst Fractal Dimension | 🔢 Number Input |

---

# ⚙️ Prediction Pipeline

The dashboard follows the same preprocessing pipeline used during model training.

```text
       👤 User
          │
          ▼
   🔢 Enter 30 Features
          │
          ▼
   📋 Keep Feature Order
          │
          ▼
   ⚙️ scaler.transform()
          │
          ▼
      🤖 Model
          │
          ▼
    model.predict()
          │
          ▼
   🎯 Final Prediction
          │
          ▼
     📊 Probabilities
```

---

# 🤖 Model Integration

The trained model and scaler are loaded using `joblib`.

```python
model = joblib.load("BinX-Week9/Day1/model.joblib")
scaler = joblib.load("BinX-Week9/Day1/scaler.joblib")
```

This allows the Streamlit application to reuse the exact model and preprocessing objects created during Day 1.

---

# 🔄 Data Preprocessing

Before making a prediction, the user's input is transformed using the saved scaler:

```python
scaled_input = scaler.transform(input_data)
```

This ensures that the new input follows the same scaling process used during model training.

---

# 🎯 Prediction

The scaled input is passed to the trained model:

```python
prediction = model.predict(scaled_input)
```

The model uses the following target encoding:

| Value | Classification |
| ----: | -------------- |
|   `0` | 🔴 Malignant   |
|   `1` | 🟢 Benign      |

The result is displayed prominently using Streamlit components.

```python
if prediction == 0:
    st.error("Prediction: Malignant")
else:
    st.success("Prediction: Benign")
```

---

# 📊 Prediction Probability

To provide additional context, the dashboard calculates the probability for both classes:

```python
probabilities = model.predict_proba(scaled_input)[0]
```

The results are displayed using:

- 📌 `st.metric()`
- 📊 `st.progress()`

This gives the user a quick visual understanding of how the model's probability is distributed between **Malignant** and **Benign**.

---

# 🧪 Testing

The application was tested locally through the Streamlit development server.

### Test Flow

```text
▶️ Start Application
       ↓
🌐 Open Browser
       ↓
🔢 Enter Feature Values
       ↓
🎯 Click Predict
       ↓
🤖 Generate Prediction
       ↓
📊 Display Probability
       ↓
✅ Verify Result
```

The application successfully:

- ✅ Started locally.
- ✅ Loaded the dashboard in the browser.
- ✅ Accepted the 30 feature inputs.
- ✅ Processed the inputs using the saved scaler.
- ✅ Generated a prediction.
- ✅ Displayed the prediction clearly.
- ✅ Displayed prediction probabilities.
- ✅ Responded to different input values.
- ✅ Provided a clear interface for a first-time user.

---

# 🛠️ Technologies & Tools

| Technology      | Purpose                      |
| --------------- | ---------------------------- |
| 🐍 Python       | Application development      |
| 🎈 Streamlit    | Interactive dashboard        |
| 🤖 Scikit-learn | Machine learning model       |
| 📦 Joblib       | Model and scaler loading     |
| 📊 Matplotlib   | Visualization support        |
| 🌿 Git          | Version control              |
| 🐙 GitHub       | Repository and collaboration |
| 🔀 Pull Request | Code review                  |

---

# ▶️ How to Run

Make sure the virtual environment is activated and run the following command from the repository root:

```powershell
& ".\.venv313\Scripts\python.exe" -m streamlit run BinX-Week9/Day3/streamlit_app.py
```

After starting the application, Streamlit provides a local URL such as:

```text
http://localhost:8501
```

Open the URL in your browser to access the dashboard.

---

# 📚 What We Practiced

### 🧠 Machine Learning

- Loading a trained model
- Loading preprocessing objects
- Transforming new input data
- Generating predictions
- Reading prediction probabilities

### 🎈 Streamlit

- `st.title()`
- `st.write()`
- `st.subheader()`
- `st.number_input()`
- `st.button()`
- `st.success()`
- `st.error()`
- `st.metric()`
- `st.progress()`
- `st.caption()`

### 🔧 Development Workflow

- Creating a Streamlit application
- Running an application locally
- Testing the complete user flow
- Preparing changes for GitHub
- Pull Request workflow
- Mentor Code Review preparation

---

# 🏁 Day 3 Status

| Task                         | Status |
| ---------------------------- | :----: |
| 🖥️ Streamlit App             |   ✅   |
| 📦 Load Model                |   ✅   |
| ⚙️ Load Scaler               |   ✅   |
| 🔢 30 Feature Inputs         |   ✅   |
| 🎯 Prediction                |   ✅   |
| 📊 Probability Visualization |   ✅   |
| 🧪 Local Testing             |   ✅   |
| 🎨 User-Friendly Interface   |   ✅   |
| 🔀 Pull Request Preparation  |   ✅   |
| 👨‍🏫 Mentor Review             |   🔄   |

---

## ⚠️ Important Note

> 🩺 **Educational Demo Only**
>
> This application is an educational machine learning demonstration and **is not a medical diagnostic tool**.

---

## ✨ Day 3 Outcome

By completing Day 3, the trained machine learning model was transformed into an **interactive Streamlit dashboard**.

The final workflow connects the complete process:

```text
📊 Dataset
   ↓
🧹 Preprocessing
   ↓
🤖 Trained Model
   ↓
💾 Saved Model + Scaler
   ↓
🎈 Streamlit Dashboard
   ↓
👤 User Input
   ↓
🎯 Prediction
   ↓
📊 Probability
```

> 🚀 **From a trained ML model to an interactive application.**
