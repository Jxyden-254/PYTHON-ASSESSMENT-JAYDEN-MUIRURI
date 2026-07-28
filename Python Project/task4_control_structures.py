"""
Task 4: Control Structures – Selection & Looping
File: task4_control_structures.py

Demonstrates if-elif-else, for loops, while loops, break/continue
and nested loops (multiplication table).
"""

# ── 1. Grade Classifier – if-elif-else ────────────────────────────────────
print("=" * 45)
print("       GRADE CLASSIFIER")
print("=" * 45)

marks = int(input("Enter student marks (0 – 100): "))

if marks >= 80:
    grade = "A"
    comment = "Excellent"
elif marks >= 60:
    grade = "B"
    comment = "Good"
elif marks >= 50:
    grade = "C"
    comment = "Average"
elif marks >= 40:
    grade = "D"
    comment = "Below Average"
else:
    grade = "F"
    comment = "Fail"

print(f"Marks: {marks}  |  Grade: {grade}  |  Remark: {comment}")

# ── 2. For loop – iterate over a list of fruits ────────────────────────────
print("\n" + "=" * 45)
print("       FRUITS LIST")
print("=" * 45)

fruits = ["mango", "banana", "apple", "orange", "grape"]

for fruit in fruits:
    print(f"  Fruit: {fruit}")



# ── 4. break and continue ─────────────────────────────────────────────────
print("\n" + "=" * 45)
print("       break AND continue DEMO")
print("=" * 45)

print("Skipping 3 (continue) and stopping at 7 (break):")
for number in range(1, 11):
    if number == 3:
        print(f"  Skipping {number} …")
        continue                  # skip the rest of the loop body for 3
    if number == 7:
        print(f"  Reached {number}, breaking out of loop.")
        break                     # exit the loop entirely at 7
    print(f"  {number}")

# ── 5. Nested loop – 3 × 3 Multiplication Table ───────────────────────────
print("\n" + "=" * 45)
print("       3 × 3 MULTIPLICATION TABLE")
print("=" * 45)

# Print column headers
print("    ", end="")
for col in range(1, 4):
    print(f"{col:>6}", end="")
print()                           # newline after headers
print("    " + "-" * 18)

for row in range(1, 4):
    print(f" {row}  |", end="")          # row label
    for col in range(1, 4):
        result = row * col
        print(f"{result:>6}", end="")    # right-align each result in 6 chars
    print()                              # newline at end of each row
# ── 3. While loop – print even numbers from 1 to 10 ───────────────────────
print("\n" + "=" * 45)
print("       EVEN NUMBERS (1 – 10)")
print("=" * 45)

counter = 1
while counter <= 10:
    if counter % 2 == 0:          # check if the number is even
        print(f"  {counter}")
    counter += 1                  # increment to avoid infinite loop