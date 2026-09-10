"""
Module 2 practice — Lists, slicing, and multidimensional data.
Notes: 03-lists-slicing-and-multidimensional-data.md
Author: Bhavana

Demo functions below are runnable examples. The matrix challenges at the
bottom are intentionally left unsolved as TODOs.
"""


def demo_list_basics():
    print("== List basics: indexing & mutation ==")
    numbers = [10, 20, 30, 40]
    print("numbers:      ", numbers)
    print("numbers[0]:   ", numbers[0])
    print("numbers[-1]:  ", numbers[-1])

    numbers[1] = 99
    print("after numbers[1] = 99:", numbers)

    numbers.append(50)
    print("after append(50):     ", numbers)


def demo_iteration_and_enumerate():
    print("\n== Iterating with & without enumerate() ==")
    numbers = [10, 20, 30, 40]

    for number in numbers:
        print("value:", number)

    for i, value in enumerate(numbers):
        print(f"index {i} -> {value}")


def demo_slicing():
    print("\n== Slicing ==")
    numbers = [10, 20, 30, 40, 50]
    print("numbers[1:4]:   ", numbers[1:4])
    print("numbers[0:5:2]: ", numbers[0:5:2])

    x = [0, 1, 2, 3, 4, 5]
    print("x[:3]:  ", x[:3])
    print("x[3:]:   ", x[3:])
    print("x[::-1]:  ", x[::-1])


def demo_nested_lists_matrix():
    print("\n== Nested lists as a matrix ==")
    grades = [
        ["Bhavana", 92, 88],
        ["Riya", 75, 81],
    ]

    print("grades[0][0]:", grades[0][0])   # "Bhavana"
    print("grades[1][2]:", grades[1][2])    # 81

    for row in grades:
        for value in row:
            print(value, end=" | ")
        print()


def demo_warehouse_grid_audit():
    print("\n== Real-world pattern: grid audit (if + continue + break + enumerate) ==")
    warehouse_grid = [
        [15, 22, 0, 8],     # Aisle 0
        [40, 99, 12, 5],     # Aisle 1
        [0, 11, 88, 14],      # Aisle 2
    ]

    for aisle_id, bins in enumerate(warehouse_grid[:2]):   # audit only aisles 0 and 1
        print(f"Auditing aisle {aisle_id}...")
        for bin_id, stock in enumerate(bins):
            if stock == 0:
                print(f"  bin {bin_id}: empty - skipping")
                continue
            if stock > 90:
                print(f"  bin {bin_id}: overcapacity ({stock}) — halting audit")
                break
            print(f"  bin {bin_id}: nominal ({stock} units)")


if __name__ == "__main__":
    demo_list_basics()
    demo_iteration_and_enumerate()
    demo_slicing()
    demo_nested_lists_matrix()
    demo_warehouse_grid_audit()


# ---------------------------------------------------------------------------
# TODO — Matrix challenges. Solve these yourself; no solutions provided.
# ---------------------------------------------------------------------------
#
# 1. Matrix traversal — print [[1,2,3],[4,5,6],[7,8,9]] row by row with
#    nested loops, then compute its sum (45) WITHOUT using sum().
#
# 2. Matrix maximum — find the largest value in [[12,4,8],[23,7,19],[5,31,2]]
#    (31) WITHOUT using max().
