"""
Module 6 practice — Traps recap & cheat-sheet patterns.
Notes: 04-dictionary-traps-cheatsheet-and-practice.md
Author: Bhavana

The Day 8 exercises at the bottom are intentionally left unsolved as TODOs.
"""


def demo_traps_recap():
    print("== Traps recap ==")
    d = {"a": 1}

    try:
        d["b"]
    except KeyError as e:
        print(f"1. d['b'] -> KeyError: {e}")
    print("   fix: d.get('b') ->", d.get("b"))

    print("2. 'b' in d.values()? ->", "b" in d.values(), " ('b' is not even a value here)")

    a = {"x": 1}
    b = a
    b["x"] = 2
    print("3. b = a shares state -> a:", a)

    dup = {"a": 1, "a": 2}
    print("4. duplicate keys collapse ->", dup)

    d2 = {"a": 1}
    d2.pop("a")
    print("5. pop() actually removes ->", d2)

    d3 = {}
    d3.get("age", 22)
    print("6. get() with default does NOT insert -> 'age' in d3:", "age" in d3)
    d3.setdefault("age", 22)
    print("   setdefault() DOES insert -> 'age' in d3:", "age" in d3)

    print("7. keys() is a view, not a list ->", type({"a": 1}.keys()))

    for x in {"a": 1, "b": 2}:
        pass
    print("8. iterating a dict directly yields KEYS (see loop above)")

    d4 = {"z": 1, "a": 2}
    print("9. insertion order preserved, not sorted ->", list(d4), " sorted:", sorted(d4))

    try:
        {[1, 2]: "x"}
    except TypeError as e:
        print(f"10. list as key -> TypeError: {e}")


if __name__ == "__main__":
    demo_traps_recap()


# ---------------------------------------------------------------------------
# TODO — Day 8 exercises. Solve these yourself; no solutions provided.
# ---------------------------------------------------------------------------
#
# 1. Create an empty dictionary called `dog`; add name, color, breed, legs, age.
# 2. Create a `student` dictionary with keys: first_name, last_name, gender,
#    age, marital_status, skills, country, city, address.
# 3. Get the length of the student dictionary.
# 4. Get the value of skills and confirm its type is list.
# 5. Modify skills by adding one or two more skills.
# 6. Get the dictionary's keys as a list.
# 7. Get the dictionary's values as a list.
# 8. Convert the dictionary to a list of tuples using .items().
# 9. Delete one of the items in the dictionary.
# 10. Delete the dictionary itself (del).
