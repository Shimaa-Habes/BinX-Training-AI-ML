# 🎮 Week 4 — Day 4: Feature Engineering & Hyperparameter Tuning

> **BINX AI Game Lab**
> Turning raw gaming data into better features, then tuning a model to find a stronger configuration. 🎯

---

## 🕹️ Day Overview

Today I focused on two important Machine Learning concepts:

**Feature Engineering** — creating or transforming features so they provide more useful information to the model.

**Hyperparameter Tuning** — testing different model settings systematically instead of choosing them manually.

For the practical work, I used the **Video Game Sales & Ratings** dataset and applied these concepts directly to gaming data.

---

## 🎮 Dataset

### Video Game Sales & Ratings

The dataset contains information about video games, including:

* 🎮 Platform
* 🧩 Genre
* 📅 Release year
* 🏢 Publisher and Developer
* 🌍 Regional and Global sales
* ⭐ Critic and User scores
* 🔞 ESRB Rating

I chose this dataset because it contains both **numerical and categorical features**, which makes it a good fit for practicing different feature engineering techniques.

---

## 🧠 4.1 Why Feature Engineering Matters

One of the main ideas from this day was that a more complicated model is not always the best solution.

Sometimes, creating better and more meaningful features can help a model learn patterns more effectively without changing the model itself.

In this notebook, I tried to make the gaming data more useful before moving on to model tuning.

---

## 🧩 4.2 Common Feature Engineering Techniques

I practiced several techniques using the gaming dataset:

| Technique              | Example                                         |
| ---------------------- | ----------------------------------------------- |
| 🧩 Creating Features   | Combining regional sales                        |
| 📦 Binning             | Converting `Critic_Score` into categories       |
| 🔤 One-Hot Encoding    | Converting `Genre` into binary columns          |
| 📅 Datetime Extraction | Extracting useful information from date values  |
| ⚖️ Scaling             | Applying `StandardScaler` to numerical features |

I also created three useful engineered features:

* `Total_Regional_Sales`
* `Game_Age`
* `Average_Score`

These features were created to provide additional information about sales, the age of a game, and its overall reception.

---

## ⚙️ 4.3 Hyperparameters vs. Parameters

I reviewed the difference between model parameters and hyperparameters.

**Parameters** are learned automatically by the model during training.

**Hyperparameters** are selected before training and control how the model behaves.

Some examples are:

* 🌳 `max_depth` → Decision Tree / Random Forest
* 🔎 `k` → k-NN
* 🧮 `alpha` → Ridge

Understanding this difference is important because hyperparameters can be tuned to improve model performance.

---

## 🔍 4.4 GridSearchCV

For the tuning stage, I used **GridSearchCV** with **5-fold cross-validation**.

The parameter grid for the Decision Tree was:

```python
param_grid = {
    'max_depth': [3, 5, 10, None],
    'min_samples_split': [2, 5, 10]
}
```

This gives:

**4 × 3 = 12 combinations**

With 5-fold cross-validation:

**12 × 5 = 60 model fits**

For larger search spaces, `RandomizedSearchCV` can be more efficient because it tests only a selected number of combinations instead of checking every possible combination.

---

# 🧪 Hands-On Lab

## 🎮 Step 1 — Create Engineered Features

I created new features from the existing gaming data:

* `Total_Regional_Sales`
* `Game_Age`
* `Average_Score`

Each feature was created to capture information that might be useful for the model.

---

## 🌳 Step 2 — Choose the Model & Define the Grid

For this lab, I used the **Decision Tree Classifier** from Week 3.

I chose it because its hyperparameters are easy to understand and give a clear example of how model settings affect performance.

The main hyperparameters I tuned were:

* `max_depth`
* `min_samples_split`

---

## 🔍 Step 3 — Run GridSearchCV

I used:

* **5-fold cross-validation**
* **F1 score** as the evaluation metric
* **GridSearchCV** to test all parameter combinations

The search automatically selected the configuration with the highest cross-validated F1 score.

---

## 🏆 Step 4 — Compare the Tuned Model with the Baseline

Before tuning, I evaluated the default Decision Tree as a baseline.

Then, I compared its cross-validated F1 score with the score of the tuned model.

This comparison showed whether hyperparameter tuning actually improved the model instead of assuming that it would.

---

## 🧠 Step 5 — Find What Mattered Most

Finally, I examined:

* ⭐ Feature importance from the tuned Decision Tree
* ⚙️ The best hyperparameters selected by GridSearchCV
* 📈 The difference between the baseline and tuned F1 scores

This helped me understand which features were most useful and which hyperparameter configuration performed best.

---

## 🛠️ Debugging Note

While checking the scaling results, I noticed that some values in `Total_Regional_Sales` were still quite large after applying `StandardScaler`.

At first, I thought the scaling had not worked correctly, so I checked the column statistics and used ChatGPT to help investigate the result.

After checking the mean, standard deviation, minimum, and maximum values, I found that the scaling was actually correct.

The large values were caused by **extreme sales outliers** in the dataset.

This helped me understand that `StandardScaler` does **not** force every value between `-1` and `1`. Instead, it centers the data around zero and scales it according to the standard deviation.

---

## 🛠️ Tools Used

* 🐍 Python
* 🐼 Pandas
* 🔢 NumPy
* 🤖 Scikit-learn
* 📓 Jupyter Notebook
* 🎮 Video Game Sales & Ratings Dataset

---

## ✅ Day 4 Completed

* ✅ Dataset loaded and explored
* ✅ Feature engineering applied
* ✅ Feature creation practiced
* ✅ Binning practiced
* ✅ One-Hot Encoding applied
* ✅ Feature scaling practiced
* ✅ Parameters vs. hyperparameters reviewed
* ✅ Decision Tree baseline evaluated
* ✅ GridSearchCV with 5-fold cross-validation completed
* ✅ Tuned model compared with the baseline
* ✅ Feature importance examined

---

## 🏁 Final Takeaway

This day showed me that improving a Machine Learning model is not only about choosing a more advanced algorithm.

Sometimes, the biggest improvement comes from **creating better features and carefully tuning the model's hyperparameters**.

> 🎮 **Better Features + Smart Tuning = Better Model Decisions**

