"""
Module 6 practice — Dictionary methods, views & iteration.
Notes: 02-dictionary-methods-and-views.md
Author: Bhavana
"""


def demo_update():
    print("== update() ==")
    person = {"name": "Bhavana", "age": 22}
    person.update({"age": 23, "country": "India"})
    print(person)
    person.update(age=24, city="Vizag")
    print(person)


def demo_removal():
    print("\n== Removing items: del / pop / popitem / clear ==")
    person = {"name": "Bhavana", "age": 22, "country": "India"}

    age = person.pop("age")
    print("popped age:", age, " remaining:", person)

    print("pop missing with default:", person.pop("salary", None))

    del person["country"]
    print("after del country:", person)

    try:
        del person["salary"]
    except KeyError as e:
        print(f"del on missing key raised KeyError as expected: {e}")

    person2 = {"name": "Bhavana", "age": 22, "country": "India"}
    print("popitem():", person2.popitem(), " remaining:", person2)

    person2.clear()
    print("after clear():", person2)


def demo_copy_vs_assignment():
    print("\n== copy() vs plain assignment ==")
    a = {"x": 1}
    b = a
    b["x"] = 99
    print("plain assignment - a also changed:", a)

    a = {"x": 1}
    b = a.copy()
    b["x"] = 99
    print("with .copy() - a is unaffected:", a, " b:", b)


def demo_views_and_iteration():
    print("\n== Views & iteration ==")
    person = {"name": "Bhavana", "age": 22}
    print("keys():  ", person.keys())
    print("values():", person.values())
    print("items(): ", person.items())
    print("list(keys()):", list(person.keys()))

    for key in person:
        print("  key:", key)
    for value in person.values():
        print("  value:", value)
    for key, value in person.items():
        print(f"  {key} -> {value}")


def demo_comprehension():
    print("\n== Dictionary comprehension ==")
    squares = {x: x ** 2 for x in range(5)}
    print(squares)
    evens_squared = {x: x ** 2 for x in range(10) if x % 2 == 0}
    print(evens_squared)


def demo_building_from_other_data():
    print("\n== Building from other data ==")
    keys = ["name", "age", "country"]
    values = ["Bhavana", 22, "India"]
    print("dict(zip(...)):", dict(zip(keys, values)))
    print("fromkeys, no default:", dict.fromkeys(keys))
    print("fromkeys, default 0: ", dict.fromkeys(keys, 0))


def demo_setdefault_vs_get():
    print("\n== setdefault() vs get() ==")
    person = {"name": "Bhavana"}

    print("get('age', 22):", person.get("age", 22))
    print("'age' in person after get():", "age" in person)

    print("setdefault('age', 22):", person.setdefault("age", 22))
    print("'age' in person after setdefault():", "age" in person)

    print("setdefault('name', 'Anu') keeps existing value:", person.setdefault("name", "Anu"))


def demo_equality_and_order():
    print("\n== Equality vs order ==")
    a = {"name": "Bhavana", "age": 22}
    b = {"age": 22, "name": "Bhavana"}
    print("a == b:", a == b)

    d = {"z": 1, "a": 2}
    print("list(d):    ", list(d))
    print("sorted(d):   ", sorted(d))

    scores = {"A": 80, "B": 95, "C": 70}
    print("sorted by value asc: ", sorted(scores.items(), key=lambda item: item[1]))
    print("sorted by value desc:", sorted(scores.items(), key=lambda item: item[1], reverse=True))


if __name__ == "__main__":
    demo_update()
    demo_removal()
    demo_copy_vs_assignment()
    demo_views_and_iteration()
    demo_comprehension()
    demo_building_from_other_data()
    demo_setdefault_vs_get()
    demo_equality_and_order()
