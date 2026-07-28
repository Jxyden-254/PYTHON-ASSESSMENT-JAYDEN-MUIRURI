"""
Task 5: Functions in Python
File: task5_functions.py

Demonstrates built-in functions, user-defined functions, default parameters,
*args, lambda with map(), and variable scope.
"""

# ── 1. Built-in Functions: len(), max(), sorted() ─────────────────────────
print("=" * 45)
print("       BUILT-IN FUNCTIONS")
print("=" * 45)

scores = [55, 82, 47, 91, 63, 78]

print("List              :", scores)
print("len(scores)       :", len(scores))        # number of elements
print("max(scores)       :", max(scores))        # largest value
print("sorted(scores)    :", sorted(scores))     # sorted copy (ascending)

# ── 2. User-Defined Function: calculate_area() ────────────────────────────
print("\n" + "=" * 45)
print("       AREA CALCULATOR")
print("=" * 45)


def calculate_area(length, width):
    """Calculate and return the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width  (float): The width of the rectangle.

    Returns:
        float: The calculated area.
    """
    area = length * width
    return area


# Call the function
room_area = calculate_area(8.5, 5.0)
print(f"Area of 8.5 × 5.0 rectangle = {room_area} sq units")

# ── 3. Default Parameter Values ────────────────────────────────────────────
print("\n" + "=" * 45)
print("       DEFAULT PARAMETERS")
print("=" * 45)


def greet(name, greeting="Hello"):

    """Greet a person with an optional custom greeting.

    Args:
        name     (str): Person's name.
        greeting (str): Greeting word (default: 'Hello').
    """
    print(f"{greeting}, {name}!")


greet("Alice")                    # uses default greeting
greet("Bob","Good morning")      # overrides the default

# ── 4. *args – Variable Number of Arguments ────────────────────────────────
print("\n" + "=" * 45)
print("       *args DEMO")
print("=" * 45)


def sum_all(*args):
    """Return the sum of any number of numeric arguments.

    Args:
        *args: Variable-length list of numbers.

    Returns:
        int/float: The total sum.
    """
    total = 0
    for value in args:
        total += value
    return total


print("Sum of 3, 7        :", sum_all(3, 7))
print("Sum of 1, 2, 3, 4  :", sum_all(1, 2, 3, 4))
print("Sum of 10, 20, 5   :", sum_all(10, 20, 5))

# ── 5. Lambda with map() ───────────────────────────────────────────────────
print("\n" + "=" * 45)
print("       LAMBDA + map()")
print("=" * 45)

# Lambda function to square a number
square = lambda x: x ** 2

numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))     # apply lambda to every element

print("Original numbers :", numbers)
print("Squared numbers  :", squared)

# ── 6. Variable Scope – local vs global ────────────────────────────────────
print("\n" + "=" * 45)
print("       VARIABLE SCOPE")
print("=" * 45)

institution = "The Co-operative University"         # global variable


def show_scope():
    """Demonstrate local and global variable scope."""
    local_department = "Computer Science"    # local variable

    global institution                       # reference the global variable
    institution = "The Co-operative University (Updated)"  # modify the global variable

    print("Inside function – local_department :", local_department)
    print("Inside function – institution      :", institution)


show_scope()
print("Outside function – institution     :", institution)

# local_department is not accessible here – would raise NameError
# print(local_department)   # ← uncomment to see the NameError
