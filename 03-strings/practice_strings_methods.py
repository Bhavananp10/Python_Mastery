"""
Module 3 practice — String operators & built-in methods.
Notes: 02-string-operators-and-methods.md
Author: Bhavana
"""


def demo_operators():
    print("== Operators: concatenation, repetition, membership ==")
    print("Hello" + " " + "World")
    print("=" * 20)
    print("Hi" * 0, "<- empty string")
    print("Hi" * -2, "<- also empty")

    payload = "System Alert: Unauthorized API Access Attempt"
    print("'Alert' in payload:", "Alert" in payload)

    age = 22
    try:
        "Age: " + age
    except TypeError as e:
        print(f"'Age: ' + age raised TypeError as expected: {e}")
    print("Age: " + str(age))
    print(f"Age: {age}")


def demo_case_methods():
    print("\n== Case methods ==")
    print("python".capitalize())
    print("python programming language".title())
    print("PyThOn".swapcase())
    print("HELLO".casefold() == "hello".casefold())


def demo_whitespace_methods():
    print("\n== Whitespace methods ==")
    padded = "   Python   "
    print(repr(padded.strip()))
    print(repr(padded.lstrip()))
    print(repr(padded.rstrip()))

    # strip(chars) removes a CHARACTER SET from the edges, not a substring —
    # "banana" has no "na" substring at either end, yet strip("na") still
    # removes 3 characters from the right (a, n, a — each individually in {n, a})
    print("'banana'.strip('na'):     ", "banana".strip("na"))
    print("'---Python---'.strip('-'):", "---Python---".strip("-"))


def demo_search_methods():
    print("\n== Search methods ==")
    s = "Python"
    print("s.find('th'): ", s.find("th"))
    print("s.find('xyz'):", s.find("xyz"))
    try:
        s.index("xyz")
    except ValueError as e:
        print(f"s.index('xyz') raised ValueError as expected: {e}")

    print("'banana'.count('a'): ", "banana".count("a"))
    print("'aaa'.count('aa'):   ", "aaa".count("aa"), "<- non-overlapping, not 2")

    print("startswith:", "Python Programming".startswith("Python"))
    print("endswith:  ", "report.pdf".endswith(".pdf"))


def demo_split_and_join():
    print("\n== split() & join() ==")
    print("split():        ", "Python is powerful".split())
    print("split() collapse:", "hello   world".split())
    print("split(' '):       ", "hello   world".split(" "), "<- keeps empty strings")
    print("maxsplit=2:        ", "one two three four".split(" ", 2))
    print("rsplit('-', 1):     ", "one-two-three".rsplit("-", 1))

    words = ["Python", "is", "fun"]
    print("' '.join(words):", " ".join(words))

    numbers = [1, 2, 3]
    try:
        ",".join(numbers)
    except TypeError as e:
        print(f"','.join(numbers) raised TypeError as expected: {e}")
    print("','.join(map(str, numbers)):", ",".join(map(str, numbers)))


def demo_testing_methods():
    print("\n== Testing methods (all return bool) ==")
    print("'Python'.isalpha():    ", "Python".isalpha())
    print("'Python3'.isalpha():   ", "Python3".isalpha())
    print("'123'.isdigit():       ", "123".isdigit())
    print("'Python123'.isalnum():", "Python123".isalnum())
    print("'Python_123'.isalnum():", "Python_123".isalnum())
    print("'   '.isspace():        ", "   ".isspace())
    print("'python'.islower():      ", "python".islower())
    print("'PYTHON'.isupper():       ", "PYTHON".isupper())

    print("'my_variable'.isidentifier():", "my_variable".isidentifier())
    print("'123abc'.isidentifier():      ", "123abc".isidentifier())
    print("'class'.isidentifier():        ", "class".isidentifier(), "<- looks valid, but 'class' is a keyword")


if __name__ == "__main__":
    demo_operators()
    demo_case_methods()
    demo_whitespace_methods()
    demo_search_methods()
    demo_split_and_join()
    demo_testing_methods()
