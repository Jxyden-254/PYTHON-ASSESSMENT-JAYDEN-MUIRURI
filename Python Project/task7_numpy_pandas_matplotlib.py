"""
Task 7: Scientific Modules – NumPy, Pandas & Matplotlib
File: task7_numpy_pandas_matplotlib.py

Install libraries first:
    pip install numpy pandas matplotlib

Demonstrates array operations, DataFrame creation/filtering and charts.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ── NUMPY ─────────────────────────────────────────────────────────────────
print("=" * 50)
print("       NUMPY OPERATIONS")
print("=" * 50)

# (a) Create a 1-D array of 10 numbers
array_1d = np.array([4, 8, 15, 16, 23, 42, 7, 3, 19, 11])
print("1-D Array       :", array_1d)
print("Mean            :", np.mean(array_1d))
print("Sum             :", np.sum(array_1d))

# Reshape to 2 × 5
array_2d = array_1d.reshape(2, 5)
print("\nReshaped (2×5)  :\n", array_2d)

# (b) Element-wise arithmetic on two arrays
a = np.array([10, 20, 30, 40, 50])
b = np.array([5, 4, 3, 2, 1])
print("\nArray a  :", a)
print("Array b  :", b)
print("a + b    :", a + b)
print("a - b    :", a - b)
print("a * b    :", a * b)
print("a / b    :", a / b)

# ── PANDAS ────────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("       PANDAS DATAFRAME")
print("=" * 50)

# (c) Create a DataFrame from a dictionary (student data)
data = {
    "Name": ["Alice", "Bob", "Carol", "David", "Eve"],
    "Age": [20, 22, 21, 23, 20],
    "Course": ["CS", "IT", "CS", "Maths", "IT"],
    "Marks": [78, 45, 88, 62, 34],
}

df = pd.DataFrame(data)
print("Full Student DataFrame:")
print(df.to_string(index=False))

# (d) Filter rows where Marks > 50
print("\nStudents with Marks > 50:")
filtered_df = df[df["Marks"] > 50]
print(filtered_df.to_string(index=False))

# ── MATPLOTLIB – Bar Chart ────────────────────────────────────────────────
print("\n" + "=" * 50)
print("       MATPLOTLIB – BAR CHART")
print("=" * 50)

fig, ax = plt.subplots(figsize=(8, 5))

bars = ax.bar(df["Name"], df["Marks"], color="steelblue", edgecolor="black")
ax.set_title("Students' Names vs Marks", fontsize=14, fontweight="bold")
ax.set_xlabel("Student Name", fontsize=12)
ax.set_ylabel("Marks", fontsize=12)
ax.set_ylim(0, 100)

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 1,
        str(height),
        ha="center",
        va="bottom",
        fontsize=10,
    )

plt.tight_layout()
plt.savefig("bar_chart.png", dpi=150)
plt.show()
print("Bar chart saved as bar_chart.png")

# ── MATPLOTLIB – Line Graph (Trend) ───────────────────────────────────────
print("\n" + "=" * 50)
print("       MATPLOTLIB – LINE GRAPH (TREND)")
print("=" * 50)

# Weekly study hours trend over 8 weeks
weeks = ["Week 1", "Week 2", "Week 3", "Week 4",
         "Week 5", "Week 6", "Week 7", "Week 8"]
study_hours = [5, 6, 8, 7, 9, 10, 11, 13]

fig2, ax2 = plt.subplots(figsize=(8, 5))

ax2.plot(weeks, study_hours, marker="o", color="darkorange",
         linewidth=2, markersize=7, label="Study Hours")
ax2.set_title("Weekly Study Hours Trend", fontsize=14, fontweight="bold")
ax2.set_xlabel("Week", fontsize=12)
ax2.set_ylabel("Hours Studied", fontsize=12)
ax2.legend()
ax2.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig("line_graph.png", dpi=150)
plt.show()
print("Line graph saved as line_graph.png")
