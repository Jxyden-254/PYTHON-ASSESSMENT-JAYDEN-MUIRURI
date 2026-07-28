"""
Task 10: Machine Learning with Scikit-Learn – KNN & Naïve Bayes
File: task10_ml_knn_naive_bayes.py

Install scikit-learn first:
    pip install scikit-learn pandas

Uses the built-in Iris dataset (no download required).
"""

# ── Step 1: Confirm scikit-learn installation ─────────────────────────────
import sklearn
print("scikit-learn version:", sklearn.__version__)

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

# ══════════════════════════════════════════════════════════════════════════
# Step 2: Load Dataset with Pandas and display first 5 rows
# ══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("       IRIS DATASET – FIRST 5 ROWS")
print("=" * 60)

iris = load_iris()

# Build a readable DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df["species"] = [iris.target_names[t] for t in iris.target]

print(df.head())
print(f"\nDataset shape : {df.shape}  (rows × columns)")

# ══════════════════════════════════════════════════════════════════════════
# Step 3: Prepare Features and Labels, then split
# ══════════════════════════════════════════════════════════════════════════
X = iris.data           # features      (4 numerical columns)
y = iris.target         # labels    (0 = setosa, 1 = versicolor, 2 = virginica)

# 80 % train – 20 % test, random_state for reproducibility
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)
print(f"\nTraining samples : {X_train.shape[0]}")
print(f"Testing samples  : {X_test.shape[0]}")

# ══════════════════════════════════════════════════════════════════════════
# KNN – K-Nearest Neighbours
# ══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("       K-NEAREST NEIGHBOURS (KNN)  k=3")
print("=" * 60)

"""
Mathematics behind KNN
──────────────────────
KNN is a non-parametric, instance-based learning algorithm. To classify a
new point Q, it finds the k training examples closest to Q using the
Euclidean distance:

    d(P, Q) = √[ Σ (Pᵢ – Qᵢ)² ]   for i = 1 … n features

Steps:
  1. Compute d(Q, every training point).
  2. Select the k points with the smallest distance (nearest neighbours).
  3. Assign Q the class that is most common among those k neighbours
     (majority vote).

Choosing k:
  • Small k (e.g. 1) → low bias, high variance, sensitive to noise.
  • Large k → high bias, low variance, smoother decision boundaries.
  • Common practice: try odd values (1, 3, 5 …) and pick the k that gives
    the best cross-validation accuracy. k = 3 is a safe starting point.
"""

# Step 4: Instantiate, fit, predict
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)               # train on training data
knn_predictions = knn.predict(X_test)   # predict on test data

# Step 5: Evaluate KNN
knn_accuracy = accuracy_score(y_test, knn_predictions)
print(f"KNN Accuracy : {knn_accuracy * 100:.2f}%")
print("\nClassification Report (KNN):")
print(classification_report(y_test, knn_predictions,
                             target_names=iris.target_names))

# ══════════════════════════════════════════════════════════════════════════
# Naïve Bayes
# ══════════════════════════════════════════════════════════════════════════
print("=" * 60)
print("       NAÏVE BAYES (Gaussian NB)")
print("=" * 60)

"""
Mathematics behind Naïve Bayes
───────────────────────────────
Naïve Bayes applies Bayes' Theorem to compute the probability that a
data point belongs to each class, then picks the class with the highest
probability.

Bayes' Theorem:
    P(C | X) = [ P(X | C) × P(C) ] / P(X)

Where:
    P(C | X)  = posterior  – probability of class C given features X
    P(X | C)  = likelihood – probability of seeing X given class C
    P(C)      = prior      – overall frequency of class C in training data
    P(X)      = evidence   – constant denominator (same for all classes)

'Naïve' assumption: features are conditionally independent given the class,
so:
    P(X | C) = P(x₁|C) × P(x₂|C) × … × P(xₙ|C)

Gaussian NB (used here) models P(xᵢ | C) as a Gaussian (normal)
distribution, estimating the mean (μ) and variance (σ²) of each
feature from the training data:

    P(xᵢ | C) = (1 / √(2πσ²)) × exp(−(xᵢ − μ)² / (2σ²))

Decision: choose class C* = argmax_C [ P(C) × Π P(xᵢ | C) ]
"""

# Step 7: Instantiate, fit, predict
nb = GaussianNB()
nb.fit(X_train, y_train)                # train
nb_predictions = nb.predict(X_test)    # predict

# Step 8: Evaluate Naïve Bayes
nb_accuracy = accuracy_score(y_test, nb_predictions)
print(f"Naïve Bayes Accuracy : {nb_accuracy * 100:.2f}%")

print("\nConfusion Matrix (Naïve Bayes):")
cm = confusion_matrix(y_test, nb_predictions)

# Print a labelled confusion matrix
print(f"\n{'':>15}", end="")
for name in iris.target_names:
    print(f"{name:>12}", end="")
print()
for i, row in enumerate(cm):
    print(f"{iris.target_names[i]:>15}", end="")
    for val in row:
        print(f"{val:>12}", end="")
    print()

# ── Summary Comparison ────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("       MODEL COMPARISON SUMMARY")
print("=" * 60)
print(f"  KNN (k=3) Accuracy   : {knn_accuracy * 100:.2f}%")
print(f"  Naïve Bayes Accuracy : {nb_accuracy * 100:.2f}%")
print("=" * 60)
