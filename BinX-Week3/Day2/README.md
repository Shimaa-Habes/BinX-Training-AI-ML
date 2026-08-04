# 📘 Week 3 - Day 2: Linear Regression

Today was my first time building an actual machine learning model. After
learning the Scikit-learn workflow yesterday, I trained a Linear Regression
model and learned how to evaluate whether it actually makes useful predictions.

## 📚 Linear Regression

Linear Regression is used when the target is a continuous numerical value.
The model learns the relationship between the input features and the target
by fitting the best possible line through the data.

The prediction is calculated using:

- 📈 Feature values
- ⚖️ Learned coefficients (weights)
- ➕ A bias (intercept)

## 🎯 Model Training

Using the Scikit-learn API, the workflow was straightforward:

1. 🤖 Create the model
2. 🏋️ Train it using the training data
3. 🔮 Predict values for the test set
4. 📊 Evaluate the predictions

## 📊 Model Evaluation

To understand how well the model performed, I used three evaluation metrics:

- 📏 MAE (Mean Absolute Error)
- 📉 RMSE (Root Mean Squared Error)
- 📈 R² Score

These metrics helped measure how close the predictions were to the actual values.

## 🧪 Hands-On Lab

Applied Linear Regression on the Diabetes dataset:

- 📥 Loaded and prepared the dataset
- 🤖 Trained a Linear Regression model
- 📊 Displayed the learned coefficients
- ⭐ Identified the feature with the strongest effect
- 📈 Evaluated the model using MAE, RMSE, and R²
- ⚖️ Compared the model against a baseline prediction
- 💭 Interpreted the final results

## 📈 Results

The trained model achieved a lower RMSE than the baseline model, showing
that it successfully learned meaningful patterns from the dataset instead of
simply predicting the average value.

The feature with the strongest influence on the prediction was:

- 🫀 Heart Disease

## 🩺 Dataset

Diabetes Prediction Dataset containing patient information such as age,
BMI, hypertension, heart disease, smoking history, HbA1c level, blood
glucose level, and diabetes outcome.

## 🛠️ Tools

Python, NumPy, Pandas, Scikit-learn, Jupyter Notebook
