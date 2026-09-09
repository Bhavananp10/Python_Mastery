"""
Module 2 practice — Booleans, comparisons, logical & bitwise operators.
Notes: 01-booleans-comparisons-and-operators.md
Author: Bhavana

Run this file directly to see every demo execute in order.
"""


def demo_arithmetic():
    print("== Arithmetic operators ==")
    print("Addition:      ", 1 + 2)
    print("Subtraction:   ", 2 - 1)
    print("Multiplication:", 2 * 3)
    print("Division:      ", 4 / 2)    # division always returns a float
    print("Division:      ", 7 / 2)
    print("Floor division:", 7 // 2)    # drops the remainder
    print("Modulus:       ", 3 % 2)      # the remainder itself
    print("Exponentiation:", 2 ** 3)      # 2 * 2 * 2


def demo_floats_and_complex():
    print("\n== Floats & complex numbers ==")
    print("Pi:            ", 3.14)
    print("Gravity:       ", 9.81)
    print("Complex number:", 1 + 1j)
    print("Product:       ", (1 + 1j) * (1 - 1j))


def demo_labeled_arithmetic():
    print("\n== Labeled arithmetic on named variables ==")
    # `total` instead of `sum` on purpose: `sum` is a built-in, don't shadow it
    num_one, num_two = 3, 4

    total = num_one + num_two
    diff = num_two - num_one
    product = num_one * num_two
    division = num_two / num_one
    remainder = num_two % num_one
    floor_division = num_two // num_one
    power = num_one ** num_two

    print("total:          ", total)
    print("difference:     ", diff)
    print("product:        ", product)
    print("division:       ", division)
    print("remainder:      ", remainder)
    print("floor division: ", floor_division)
    print("power:          ", power)


def demo_geometry():
    print("\n== Operators applied to real formulas ==")

    radius = 10
    area_of_circle = 3.14 * radius ** 2
    print(f"Area of circle (r={radius}):", area_of_circle)

    length, width = 10, 20
    area_of_rectangle = length * width
    print(f"Area of rectangle ({length}x{width}):", area_of_rectangle)

    mass, gravity = 75, 9.81
    weight = mass * gravity
    print(f"Weight (mass={mass}kg):", weight, "N")

    volume = 0.075
    density = mass / volume
    print(f"Density (mass={mass}kg, volume={volume}m^3):", density, "kg/m^3")


def demo_comparison_operators():
    print("\n== Comparison operators ==")
    print(3 > 2)     # True
    print(3 >= 2)      # True
    print(3 < 2)        # False
    print(2 <= 3)         # True
    print(3 == 2)          # False
    print(3 != 2)            # True
    print(len("mango") == len("avocado"))   # False
    print(len("mango") < len("avocado"))     # True
    print(len("milk") == len("meat"))          # True


def demo_membership_and_identity():
    print("\n== Membership (in / not in) and identity (is / is not) ==")
    a, b = 1, 1
    x, y = 4, 2 ** 2
    # `is` compares object identity, not value — use variables, not literals,
    # to avoid Python's own SyntaxWarning ("is" with a literal).
    print("a is b (1 is 1):       ", a is b)                       # True — small ints are cached by CPython
    print("a is not 2:            ", a is not 2)                    # True
    print("'B' in 'Bhavana':      ", "B" in "Bhavana")                # True — starts with a capital B
    print("'A' in 'Bhavana':      ", "A" in "Bhavana")                 # False — no capital A in "Bhavana"
    print("'coding' in sentence:  ", "coding" in "coding for all")      # True
    print("x is y (4 is 2 ** 2):  ", x is y)                              # True — same cached small-int object


def demo_logical_operators():
    print("\n== Logical operators (and / or / not) ==")
    print(3 > 2 and 4 > 3)   # True  — both true
    print(3 > 2 and 4 < 3)    # False — second is false
    print(3 > 2 or 4 < 3)      # True  — first is true, short-circuits
    print(not 3 > 2)            # False — negates a True
    print(not not True)           # True


if __name__ == "__main__":
    demo_arithmetic()
    demo_floats_and_complex()
    demo_labeled_arithmetic()
    demo_geometry()
    demo_comparison_operators()
    demo_membership_and_identity()
    demo_logical_operators()
