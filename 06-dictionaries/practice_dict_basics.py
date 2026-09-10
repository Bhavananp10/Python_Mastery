"""
Module 6 practice — Dictionary basics & access.
Notes: 01-dictionary-basics.md
Author: Bhavana
"""


def demo_creation():
    print("== Creating a dictionary ==")
    person = {"name": "Bhavana", "age": 22, "is_student": True}
    print(person)
    print(type(person))

    empty = {}
    print("empty:", empty, type(empty))


def demo_hashable_keys():
    print("\n== Keys must be hashable ==")
    d = {"name": "Bhavana", 1: "one", 3.14: "pi", (1, 2): "tuple"}
    print(d)

    try:
        {[1, 2]: "hello"}
    except TypeError as e:
        print(f"list as a key raised TypeError as expected: {e}")


def demo_access():
    print("\n== Accessing values: [] vs get() ==")
    person = {"name": "Bhavana"}
    print("person['name']:", person["name"])

    try:
        person["age"]
    except KeyError as e:
        print(f"person['age'] raised KeyError as expected: {e}")

    print("person.get('name'):    ", person.get("name"))
    print("person.get('age'):     ", person.get("age"))
    print("person.get('age', 0):  ", person.get("age", 0))


def demo_length():
    print("\n== Length ==")
    person = {"name": "Bhavana", "age": 22, "country": "India"}
    print("len(person):", len(person))


def demo_add_and_update():
    print("\n== Adding & updating items ==")
    person = {"name": "Bhavana", "age": 22}
    person["country"] = "India"   # add
    person["age"] = 23              # update
    print(person)


def demo_duplicate_keys():
    print("\n== Duplicate keys collapse to the last value ==")
    person = {"name": "Bhavana", "name": "Anu"}
    print(person)


def demo_membership():
    print("\n== Checking key existence ==")
    person = {"name": "Bhavana", "age": 22}
    print("'name' in person:  ", "name" in person)
    print("'salary' in person:", "salary" in person)
    print("'salary' not in person:", "salary" not in person)

    # trap: `in` checks KEYS, not values
    print("'Bhavana' in person:         ", "Bhavana" in person)
    print("'Bhavana' in person.values():", "Bhavana" in person.values())


if __name__ == "__main__":
    demo_creation()
    demo_hashable_keys()
    demo_access()
    demo_length()
    demo_add_and_update()
    demo_duplicate_keys()
    demo_membership()
