"""
Module 3 practice — String creation, indexing, slicing & immutability.
Notes: 01-string-basics-creation-and-immutability.md
Author: Bhavana
"""


def demo_creation_and_escapes():
    print("== Creation, quotes, escapes & raw strings ==")
    name = "Bhavana"
    language = 'Python'
    print(name, language)

    multiline = """Line one
Line two
Line three"""
    print(multiline)

    print("Days\tTopics\tExercises")
    print("This is a backslash symbol (\\)")

    standard_path = "C:\\new_folder\\test.txt"   # escaped, so it's safe
    raw_path = r"C:\new_folder\test.txt"           # raw string, also safe
    print("standard_path:", standard_path)
    print("raw_path:      ", raw_path)


def demo_empty_and_spaces():
    print("\n== Empty strings & spaces-as-characters ==")
    empty = ""
    print("len(''):", len(empty))
    print("'Python' == ' Python':", "Python" == " Python")
    print("len('Python'):", len("Python"), " len(' Python'):", len(" Python"))


def demo_indexing():
    print("\n== Indexing ==")
    s = "Python"
    print("s[0]: ", s[0])
    print("s[-1]:", s[-1])
    print("s[-2]:", s[-2])

    try:
        s[len(s)]
    except IndexError as e:
        print(f"s[len(s)] raised IndexError as expected: {e}")


def demo_slicing():
    print("\n== Slicing ==")
    token = "SECURE_9845_AUTH"
    print("token[0:6]: ", token[0:6])
    print("token[7:11]:", token[7:11])
    print("token[::-1]:", token[::-1])

    s = "Python"
    print("s[:3]:   ", s[:3])
    print("s[3:]:    ", s[3:])
    print("s[0:6:2]:  ", s[0:6:2])
    print("s[1::2]:    ", s[1::2])
    print("s[5:1:-1]:   ", s[5:1:-1])

    # slicing tolerates out-of-range bounds; plain indexing does not
    print("s[0:100]:     ", s[0:100])
    try:
        s[100]
    except IndexError as e:
        print(f"s[100] raised IndexError as expected: {e}")


def demo_immutability():
    print("\n== Immutability ==")
    framework = "Django"
    try:
        framework[0] = "T"
    except TypeError as e:
        print(f"framework[0] = 'T' raised TypeError as expected: {e}")

    framework = "T" + framework[1:]   # correct way: build a new string
    print("rebuilt framework:", framework)

    s = "Python"
    s.upper()          # does nothing to `s` — the returned value is discarded
    print("s after s.upper() with no assignment:", s)
    s = s.upper()        # this is what actually changes what `s` refers to
    print("s after s = s.upper():", s)


if __name__ == "__main__":
    demo_creation_and_escapes()
    demo_empty_and_spaces()
    demo_indexing()
    demo_slicing()
    demo_immutability()
