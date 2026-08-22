# Train / Validation / Test Splits

**BinX Tech AI & ML Internship Program — Phase 2, Week 4, Day 1**

## Summary

This module covers why a single train/test split is not enough once a model starts being tuned, and introduces the three-way split (train, validation, test) as the standard, leakage-free approach. The lab applies this on the Titanic dataset, training a Decision Tree classifier and selecting its `max_depth` hyperparameter using only the validation set, before a single, final evaluation on the untouched test set.

## Topics Covered

| Section | Topic                              | Key Idea                                                                                     |
| ------- | ---------------------------------- | -------------------------------------------------------------------------------------------- |
| 1.1     | The Problem With a Single Test Set | Repeatedly checking the test set during tuning leaks information into model decisions        |
| 1.2     | The Three-Way Split                | Train, validation, and test sets each serve one distinct purpose                             |
| 1.3     | Creating the Split in Code         | Two calls to `train_test_split` produce a 60/20/20 split                                     |
| 1.4     | Why This Isn't Always Enough       | A single validation split can still mislead on smaller datasets, motivating cross-validation |

## Hands-On Lab

1. **Three-way split** — The Titanic dataset (`Pclass`, `Age`, `SibSp`, `Parch`, `Fare` as features, `Survived` as target) is split into 428 training, 143 validation, and 143 test samples.
2. **Model tuning** — A Decision Tree classifier is trained at four `max_depth` values (2, 4, 6, None), evaluated only on the validation set. `max_depth=6` performs best (72.73% validation accuracy).
3. **Final test evaluation** — The tuned model is evaluated exactly once on the held-out test set, achieving 69.93% accuracy — consistent with the validation result, indicating no overfitting to the validation set.
4. **Discussion** — A Markdown cell explains why tuning against the test set directly would produce an overly optimistic and misleading final score.

## Tools

Python · Pandas · Scikit-learn (`train_test_split`, `DecisionTreeClassifier`) · Jupyter Notebook

## Reproducibility

All splits and model training use `random_state=42` to ensure consistent results across runs.
