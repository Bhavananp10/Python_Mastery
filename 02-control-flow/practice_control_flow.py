"""
Module 2 practice — Conditionals, loops, and loop control.
Notes: 02-conditionals-and-loops.md
Author: Bhavana

Demo functions below are runnable examples of each concept.
The blank-IDE challenges and Day-3 exercises at the bottom are intentionally
left unsolved as TODOs — solve those yourself in a separate scratch file
before checking any solution.
"""


def demo_if_elif_else():
    print("== if / elif / else - discount tiers ==")
    order_total = 150.00
    membership_status = "Premium"

    if order_total >= 200.00:
        discount = 0.20
    elif order_total >= 100.00 or membership_status == "Premium":
        discount = 0.10
    else:
        discount = 0.00

    final_price = order_total * (1 - discount)
    print(f"Applied discount: {discount * 100:.0f}% | Final price: ${final_price:.2f}")


def demo_while_loop():
    print("\n== while loop ==")
    count = 0
    while count < 5:
        print(count)
        count += 1   # never forget the update, or this never stops


def demo_for_and_range():
    print("\n== for loop & range() ==")
    for i in range(5):
        print(i)

    print("range(2, 6):", list(range(2, 6)))
    print("range(0, 10, 2):", list(range(0, 10, 2)))

    numbers = [10, 20, 30]
    for i, value in enumerate(numbers):
        print(f"index {i} -> {value}")


def demo_break_and_continue():
    print("\n== break vs continue - transaction processing ==")
    transactions = [12.50, 0.99, 450.00, -5.00, 89.90]   # includes an error case

    for amount in transactions:
        if amount < 0:
            print(f"CRITICAL ERROR: negative transaction detected ({amount})!")
            break                      # check this first — a negative amount is also <= 1.00

        if amount <= 1.00:
            print(f"Skipping minor transaction: ${amount} (below threshold)")
            continue

        print(f"Processed transaction: ${amount}")


def demo_nested_loops():
    print("\n== nested loops ==")
    for i in range(3):
        for j in range(3):
            print(i, j)


def demo_filter_search_skip_patterns():
    print("\n== filter / search / skip patterns ==")

    numbers = [1, 2, 3, 4, 5, 6]
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    print("filter (evens):", even_numbers)

    search_list = [10, 20, 40, 70, 90]
    for number in search_list:
        if number > 50:
            print("search (first > 50):", number)
            break

    skip_list = [10, -2, 30, -5, 40]
    kept = []
    for number in skip_list:
        if number < 0:
            continue
        kept.append(number)
    print("skip (drop negatives):", kept)


if __name__ == "__main__":
    demo_if_elif_else()
    demo_while_loop()
    demo_for_and_range()
    demo_break_and_continue()
    demo_nested_loops()
    demo_filter_search_skip_patterns()


# ---------------------------------------------------------------------------
# TODO — Blank-IDE challenges. Solve these yourself; no solutions provided.
# ---------------------------------------------------------------------------
#
# 1. Number classifier — read a number, print Positive/Negative even/odd, or Zero.
# 2. Grade calculator — read a score 0-100, print A/B/C/D/F using if/elif/else.
# 3. Number search — in [12, 45, 7, 89, 34, 90, 23], find the first number > 50.
# 4. Filtering — from [12, 5, 8, 21, 30, 7, 44], keep only numbers divisible by 2.
# 5. Reverse — reverse [1, 2, 3, 4, 5] with a loop (no .reverse(), no [::-1]).
# 6. Bitwise prediction — predict, then verify: 5 & 3, 5 | 3, 5 ^ 3, 5 << 1, 8 >> 1.


# ---------------------------------------------------------------------------
# TODO — Day 3 exercises (30 Days of Python). Solve these yourself too.
# ---------------------------------------------------------------------------
#
#  1. Declare age (int), height (float), and a complex-number variable.
#  2. Triangle area from user-entered base and height (area = 0.5 * b * h).
#  3. Triangle perimeter from three user-entered sides.
#  4. Rectangle area & perimeter from user-entered length/width.
#  5. Circle area & circumference from a user-entered radius (pi = 3.14).
#  6. Slope & y-intercept of y = 2x - 2; slope + Euclidean distance between
#     (2, 2) and (6, 10); compare the two slopes.
#  7. Evaluate y = x^2 + 6x + 9 for several x; find the x where y == 0.
#  8. Compare len('python') vs len('dragon') with a falsy comparison.
#  9. Use `and` to check whether 'on' is in both 'python' and 'dragon'.
# 10. Use `in` to check whether 'jargon' appears in a sentence of your choice.
# 11. Convert len('python') to float, then to str.
# 12. Check whether a number is even using %.
# 13. Check whether 7 // 3 == int(2.7).
# 14. Check whether type('10') == type(10), and whether int('9.8') == 10.
# 15. Weekly pay from user-entered hours and rate per hour.
# 16. Seconds lived, from a user-entered number of years (assume 100-year lifespan).
# 17. Print a multiplication table (1-5) using nested loops.
