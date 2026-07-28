"""
##Task 2: Python Syntax, Zen of Python & PEP 8##
#File: task2_syntax_pep8.py#

##Two Principles from the Zen of Python ##
##1. "Readability counts." -> Code is read more often than it is written.
      Writing clear, well-named code reduces bugs and makes collaboration easier.
##2. "Explicit is better than implicit." ->It is better to spell out what your
    code does rather than relying on hidden or 'magic' behaviour. For example,
    always name the variables and functions clearly so the reader never has to
    guess what they do.
"""


 # ── Principle demonstration ───────────────────────────────────────────────────────────


def greet_student(student_name):
    """Return a personalised greeting for a student.#

    Args:
        student_name (str): The full name of the student./#

    Returns:
        str: A greeting message./#
    """
    # Build the greeting string using explicit concatenation
    greeting = "Hello, " + student_name + "! Welcome to Python."
    return greeting


# ── Variable declarations using snake_case ───────────────────────────────────────────────────────────


# Assignment 1 – integer
student_age = 20

# Assignment 2 – string
course_name = "Python Programming"

# Assignment 3 – float
gpa_score = 3.75

# ── Main script ───────────────────────────────────────────────────────────

# Print the greeting using the function defined above
full_name = "Alice Mwangi"
print(greet_student(full_name))

# Display the three variables and their values
print("Age        :", student_age)
print("Course     :", course_name)
print("GPA Score  :", gpa_score)
