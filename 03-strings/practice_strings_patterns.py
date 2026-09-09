"""
Module 3 practice — Comparison, truthiness traps, and common string patterns.
Notes: 04-string-comparison-truthiness-and-patterns.md
Author: Bhavana

The exercises at the bottom are intentionally left unsolved as TODOs.
"""

from collections import Counter


def demo_equality_vs_identity():
    print("== == vs is ==")
    a, b = "Python", "Python"
    print("a == b:", a == b)   # always the right tool for comparing string VALUE
    print("a is b:", a is b, "<- may be True due to interning, but never rely on this")


def demo_ordering_ord_chr():
    print("\n== Lexicographic ordering, ord() & chr() ==")
    print("'apple' < 'banana':", "apple" < "banana")
    print("'Z' < 'a':          ", "Z" < "a")
    print("ord('Z'):", ord("Z"), " ord('a'):", ord("a"))
    print("chr(65):", chr(65), " chr(97):", chr(97))


def demo_truthiness_traps():
    print("\n== Truthiness traps ==")
    print("bool(''):     ", bool(""))
    print("bool(' '):     ", bool(" "))
    print("bool('False'):  ", bool("False"), "<- the TEXT 'False' is truthy!")

    if "False":
        print("if 'False': this DOES run")


def demo_str_vs_repr():
    print("\n== str() vs repr() ==")
    s = "Hello\nWorld"
    print("str(s):", str(s))
    print("repr(s):", repr(s))


def demo_reverse_sort_minmax():
    print("\n== Reverse, sorted(), min(), max() ==")
    s = "python"
    print("s[::-1]:              ", s[::-1])
    print("''.join(reversed(s)):", "".join(reversed(s)))
    print("sorted(s):             ", sorted(s), "<- a list, not a string")
    print("''.join(sorted(s)):    ", "".join(sorted(s)))
    print("min(s):", min(s), " max(s):", max(s))


def demo_enumerate_strings():
    print("\n== enumerate() with strings ==")
    for index, char in enumerate("Python"):
        print(index, char)


def demo_efficient_building():
    print("\n== Efficient string building ==")
    source = "python"
    parts = []
    for char in source:
        parts.append(char.upper())
    result = "".join(parts)
    print("built via list + join:", result)


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def is_anagram(a: str, b: str) -> bool:
    return Counter(a) == Counter(b)


def dedupe_preserve_order(s: str) -> str:
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)


def count_vowels(s: str) -> int:
    count = 0
    for char in s.lower():
        if char in "aeiou":
            count += 1
    return count


def demo_common_patterns():
    print("\n== Common patterns ==")
    print("is_palindrome('madam'):", is_palindrome("madam"))
    print("is_anagram('listen', 'silent'):", is_anagram("listen", "silent"))
    print("dedupe_preserve_order('banana'):", dedupe_preserve_order("banana"))
    print("count_vowels('Python Programming'):", count_vowels("Python Programming"))
    print("Counter('banana'):", Counter("banana"))

    messy = " hello \n world \t python "
    print("strip only edges:", repr(messy.strip()))
    print("split + join removes ALL whitespace:", repr("".join(messy.split())))


if __name__ == "__main__":
    demo_equality_vs_identity()
    demo_ordering_ord_chr()
    demo_truthiness_traps()
    demo_str_vs_repr()
    demo_reverse_sort_minmax()
    demo_enumerate_strings()
    demo_efficient_building()
    demo_common_patterns()


# ---------------------------------------------------------------------------
# TODO — solve these yourself; no solutions provided.
# ---------------------------------------------------------------------------
#
# 1. Write your own palindrome checker WITHOUT slicing ([::-1]) — use a loop
#    or two pointers instead.
# 2. Write your own anagram checker WITHOUT sorted() or Counter — count
#    characters manually with a plain dict.
# 3. Given a sentence, find the position of the LAST occurrence of a
#    repeated word using rfind()/rindex().
# 4. Join ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'] into
#    "Django# Flask# Bottle# Pyramid# Falcon".
# 5. Reproduce this table with \t, using your own details:
#      Name      Age     Country   City
#      Bhavana   ??      ??        ??
# 6. Using string formatting, reproduce:
#      The area of a circle with radius 10 is 314.00 meters square.
# 7. Using string formatting, reproduce all seven lines:
#      8 + 6 = 14
#      8 - 6 = 2
#      8 * 6 = 48
#      8 / 6 = 1.33
#      8 % 6 = 2
#      8 // 6 = 1
#      8 ** 6 = 262144
