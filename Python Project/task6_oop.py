"""
Task 6: Object-Oriented Python
File: task6_oop.py

Demonstrates classes, objects, instance methods, class variables,
inheritance, method overriding and encapsulation with private attributes.
"""

# ── Base Class: Animal ─────────────────────────────────────────────────────
class Animal:
    """Represent a generic animal.

    Class Variables:
        species (str): Broad biological category (all animals share this).
        counter (int): Tracks the total number of Animal instances created.
    """

    species = "Mammal"      # class variable shared by all instances
    counter = 0             # class variable to count instances

    def __init__(self, name, sound):
        """Initialise an Animal with a name and sound.

        Args:
            name  (str): The animal's name.
            sound (str): The sound the animal makes.
        """
        self.name = name        # instance variable
        self.sound = sound      # instance variable
        self.__age = 0          # private attribute (encapsulation)

        Animal.counter += 1     # increment the class counter on each creation

    def speak(self):
        """Print the animal's name and the sound it makes."""
        print(f"{self.name} says: {self.sound}")

    # ── Getter and Setter for the private __age attribute ─────────────────
    def get_age(self):
        """Return the animal's age (getter)."""
        return self.__age

    def set_age(self, age):
        """Set the animal's age after validation (setter).

        Args:
            age (int): Age in years; must be a non-negative integer.
        """
        if age < 0:
            print("Error: Age cannot be negative.")
        else:
            self.__age = age


# ── Subclass: Dog (inherits from Animal) ──────────────────────────────────
class Dog(Animal):
    """Represent a Dog; extends Animal and overrides speak()."""

    def __init__(self, name):
        """Initialise a Dog (sound is always 'Woof').

        Args:
            name (str): The dog's name.
        """
        super().__init__(name, "Woof")   # call the parent __init__

    def speak(self):
        """Override speak() with a dog-specific message."""
        print(f"{self.name} barks loudly: {self.sound}! {self.sound}!")


# ══════════════════════════════════════════════════════════════════════════
# Main demonstration
# ══════════════════════════════════════════════════════════════════════════

print("=" * 50)
print("       ANIMAL CLASS DEMONSTRATION")
print("=" * 50)

# Create two Animal instances
cat = Animal("Whiskers", "Meow")
lion = Animal("Simba", "Roar")

cat.speak()
lion.speak()

print(f"\nClass variable – species : {Animal.species}")
print(f"Total Animal instances   : {Animal.counter}")

# ── Encapsulation demo ────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("       ENCAPSULATION (private __age)")
print("=" * 50)

cat.set_age(3)                          # set via setter
print(f"{cat.name}'s age (via getter) : {cat.get_age()}")

cat.set_age(-1)                         # demonstrate validation in setter

# Direct access would fail: print(cat.__age)  ← AttributeError
print("Direct access of __age is not allowed outside the class.")

# ── Inheritance & Method Overriding ───────────────────────────────────────
print("\n" + "=" * 50)
print("       INHERITANCE – Dog subclass")
print("=" * 50)

my_dog = Dog("Rex")
my_dog.speak()                          # calls overridden speak() in Dog

# Dog also inherits speak() count through counter
print(f"\nTotal Animal (+ subclass) instances : {Animal.counter}")
print(f"Dog species (inherited)             : {my_dog.species}")

# Demonstrate getter/setter on Dog instance too
my_dog.set_age(5)
print(f"{my_dog.name}'s age : {my_dog.get_age()}")
