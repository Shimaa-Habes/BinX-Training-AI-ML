# Probability & Distributions

**BinX Tech AI & ML Internship Program — Phase 1, Week 2, Day 2**

## Summary

This module covers the probability foundations that underpin machine learning: the core rules of probability, conditional probability, Bayes' theorem, and the three distributions most commonly encountered in ML work (normal, binomial, and uniform). Each concept is paired with a worked numerical example and, where relevant, verified through simulation.

## Topics Covered

| Section | Topic                   | Key Result                                                                                                          |
| ------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------- |
| 2.1     | Probability Basics      | Probability as favorable outcomes over total outcomes                                                               |
| 2.2     | Core Rules              | Complement, addition, and multiplication rules, applied to a die roll                                               |
| 2.3     | Conditional Probability | P(King \| Face card) computed from a standard deck                                                                  |
| 2.4     | Bayes' Theorem          | Medical test example showing how a rare condition keeps the posterior probability low even with a 95%-accurate test |
| 2.5     | Common Distributions    | Normal, binomial, and uniform distributions visualized side by side                                                 |

## Hands-On Lab

The lab applies the day's concepts through simulation, with a fixed random seed for reproducibility.

1. **Coin flip simulation** — 10,000 simulated flips converge to a heads proportion of approximately 0.5, illustrating the Law of Large Numbers.
2. **Normal distribution sampling** — 10,000 samples drawn from a normal distribution (mean = 50, std = 10) reproduce the expected bell-shaped histogram, with sample statistics closely matching the generating parameters.
3. **Conditional probability verification** — A two-dice scenario is solved analytically (P(A|B) = 4/6 ≈ 0.667) and confirmed via a 100,000-trial simulation.
4. **Documentation** — Each result is interpreted in a Markdown cell explaining what it demonstrates.

## Tools

Python · NumPy · Matplotlib · Jupyter Notebook

## Reproducibility

All random processes in this notebook use `np.random.seed(42)` to ensure results are consistent across runs.
