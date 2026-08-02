# 📘 Week 3 - Day 1: Supervised Learning & Scikit-learn

Started Phase 2 today, first real step into machine learning after spending 
the last two weeks on Python and EDA basics. Today was mostly about 
understanding the theory before jumping into actual models.

## 📚 Supervised Learning

The main idea is that the model learns from data that already has the 
correct answers attached (labeled data), kind of like studying with an 
answer key. Once it learns the pattern, it can predict answers for new data 
it hasn't seen.

There are two types depending on what you're trying to predict:
- 📈 Regression - predicts a number (price, temperature, etc.)
- 🏷️ Classification - predicts a category (disease or not, spam or not)

## 🎯 Features and Target

- 🔹 X = the columns used as input (features)
- 🔹 y = the column you're trying to predict (target)

## 🤖 Scikit-learn Workflow

Every model in Scikit-learn follows the same 4 steps, which makes it easy 
to switch between models later:

1. ⚙️ Instantiate - create the model
2. 🏋️ Fit - train it on the training data
3. 🔮 Predict - make predictions on new data
4. 📊 Score - check how well it did

## ✂️ Train/Test Split

The main rule: never test the model on the same data it trained on, 
otherwise it can just memorize the answers and look better than it 
actually is. Splitting the data (80% train / 20% test) gives a real idea 
of how the model performs on data it hasn't seen before.

Used `random_state=42` so the split is reproducible.

## 🧪 Hands-On Lab

Practiced all of this on the diabetes prediction dataset:
- 📥 Loaded the dataset
- ✂️ Split it into X (features) and y (target)
- 🔀 Did an 80/20 train/test split
- ✅ Checked the shapes to make sure everything matched
- 💭 Explained why the test set has to stay hidden during training

## 🩺 Dataset

Diabetes Prediction Dataset - patient info (age, BMI, hypertension, heart 
disease, smoking history, HbA1c, glucose level) with a diabetes label. 
Used it just to practice the workflow, no actual model training yet.

## 🛠️ Tools

Python, Pandas, Scikit-learn, Jupyter Notebook