"""
Module 3 practice — String formatting: %, .format(), f-strings.
Notes: 03-string-formatting.md
Author: Bhavana
"""


def demo_percent_style():
    print("== Old-style % formatting ==")
    first_name, last_name, language = "Bhavana", "Buddha", "Python"
    print("I am %s %s. I teach %s" % (first_name, last_name, language))

    radius, pi = 10, 3.14
    area = pi * radius ** 2
    print("The area of a circle with radius %d is %.2f." % (radius, area))


def demo_format_method():
    print("\n== .format() ==")
    first_name, last_name, language = "Bhavana", "Buddha", "Python"
    print("I am {} {}. I teach {}".format(first_name, last_name, language))

    a, b = 4, 3
    print("{} + {} = {}".format(a, b, a + b))
    print("{} / {} = {:.2f}".format(a, b, a / b))


def demo_fstrings():
    print("\n== f-strings ==")
    name, age = "Bhavana", 22
    print(f"My name is {name} and I am {age} years old.")

    a, b = 4, 3
    print(f"{a} + {b} = {a + b}")
    print(f"{a} / {b} = {a / b:.2f}")
    print(f"{name.upper()}")

    price = 1234.5678
    print(f"{price:.2f}")

    population = 1_000_000
    print(f"{population:,}")


def demo_alignment_and_width():
    print("\n== Alignment & width ==")
    name = "Python"
    print(f"[{name:>10}]")   # right-aligned
    print(f"[{name:<10}]")     # left-aligned
    print(f"[{name:^10}]")      # centered


if __name__ == "__main__":
    demo_percent_style()
    demo_format_method()
    demo_fstrings()
    demo_alignment_and_width()
