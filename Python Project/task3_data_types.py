"""
Task 3: Python Data Types
File: task3_data_types.py

Demonstrates integers, floats, booleans, strings, lists, tuples,
sets, dictionaries and type casting.
"""

# ── 1. Integer ─────────────────────────────────────────────────────────────
student_marks = 85                          # declare an integer
print("Integer value :", student_marks)
print("Type          :", type(student_marks))   # confirm type

# ── 2. Float ───────────────────────────────────────────────────────────────
temperature = 36.6                          # declare a float
print("\nFloat value   :", temperature)
print("Type          :", type(temperature))
print("temperature x 2 =", temperature * 2)    # arithmetic on float

# ── 3. Boolean ─────────────────────────────────────────────────────────────
is_passed = True                            # declare a boolean
print("\nBoolean value :", is_passed)

# Use boolean in a conditional expression
if is_passed:
    print("Result: Student has PASSED.")
else:
    print("Result: Student has FAILED.")

# ── 4. String ──────────────────────────────────────────────────────────────
first_name = "Alice"
last_name = "Mwangi"

# Concatenation
full_name = first_name + " " + last_name
print("\nFull name (concatenation):", full_name)

# Slicing – first 5 characters
print("Sliced              :", full_name[0:5])

# Length
print("Length of full_name      :", len(full_name))

# ── 5. List ────────────────────────────────────────────────────────────────
fruits = ["mango", "banana", "apple", "orange", "grape"]
print("\nOriginal list :", fruits)

fruits.append("pawpaw")                     # add an element
print("After append  :", fruits)

fruits.remove("banana")                     # remove an element
print("After remove  :", fruits)

print("Index [0]     :", fruits[0])         # indexing

# ── 6. Tuple ───────────────────────────────────────────────────────────────
coordinates = (10.5, 20.3, 30.7)
print("\nTuple         :", coordinates)
print("Element [1]   :", coordinates[1])

# Demonstrate immutability – catch the TypeError
try:
    coordinates[0] = 99.9               # this will raise a TypeError
except TypeError as error:
    print("Immutability error caught:", error)

# ── 7. Set ─────────────────────────────────────────────────────────────────
# Duplicate values are removed automatically
numbers_with_duplicates = {1, 2, 2, 3, 3, 3, 4}
print("\nSet (duplicates removed):", numbers_with_duplicates)

# ── 8. Dictionary ──────────────────────────────────────────────────────────
student = {
    "name": "Bob Kamau",
    "age": 21,
    "course": "Computer Science",
}
print("\nDictionary    :", student)

# Access a value
print("Name          :", student["name"])

# Add a new key-value pair
student["admission"] = "t00/304042/2025"
print("After add     :", student)

# Delete a key
del student["age"]
print("After delete  :", student)

# ── 9. Type Casting ────────────────────────────────────────────────────────
original_int = 42
original_float = 9.99
original_str = "100"

print("\nType casting:")
print("int → float :", float(original_int))          # int to float
print("float → int :", int(original_float))           # float to int (truncates)
print("str → int   :", int(original_str))             # string to int
print("int → str   :", str(original_int), type(str(original_int)))  # int to string
