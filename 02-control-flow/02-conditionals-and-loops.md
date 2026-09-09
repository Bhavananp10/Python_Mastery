# Module 2 (cont.) — Control Flow: Conditionals & Loops

> Stage: 02-control-flow · Status: In progress · Last updated: 2026-09-09
> Notes compiled by: BHAVANA

## Summary

How a program chooses what to execute (`if`/`elif`/`else`) and what to repeat (`while`/`for`, `break`/`continue`) — built directly on the Booleans and operators from [01-booleans-comparisons-and-operators.md](01-booleans-comparisons-and-operators.md).

```text
        CONDITION
            │
      True/False
       /       \
   PATH A      PATH B
       └───┬────┘
           ▼
         LOOP
           │
     repeat / stop
```

Runnable practice for everything here: [practice_control_flow.py](practice_control_flow.py).

---

## 1. `if` / `if-else` / `if-elif-else`

```python
if age >= 18:
    print("Adult")
```

Both branches:

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Multiple paths, checked top to bottom — the first true branch runs, the rest are skipped:

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"
```

### Nested `if` vs. a combined condition

```python
# works, but unnecessarily nested
if age >= 18:
    if has_license:
        print("Can drive")

# usually cleaner
if age >= 18 and has_license:
    print("Can drive")
```

### Real-world pattern: tiered logic

```python
order_total = 150.00
membership_status = "Premium"

if order_total >= 200.00:
    discount = 0.20
elif order_total >= 100.00 or membership_status == "Premium":
    discount = 0.10
else:
    discount = 0.00

final_price = order_total * (1 - discount)
print(f"Applied discount: {discount * 100}% | Final price: ${final_price:.2f}")
```

This is the same `if/elif/else` mechanics as the grade example, just applied to a pricing-tier decision instead of a letter grade.

---

## 2. `while` — Repeat While a Condition Holds

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

Every `while` loop needs the same four pieces:

```text
initialization → condition → body → update → (back to condition)
```

Forget the update, and you've written an **infinite loop**:

```python
count = 0
while count < 5:
    print(count)     # count never changes — this never stops
```

---

## 3. `for` — Iterate Over an Iterable

Python's `for` iterates directly over the items of something iterable — no manual counter needed:

```python
for number in [10, 20, 30]:
    print(number)
```

### `range()`

```python
range(5)          # 0 1 2 3 4        — stop is excluded
range(2, 6)        # 2 3 4 5
range(0, 10, 2)     # 0 2 4 6 8
range(10, 0, -2)     # 10 8 6 4 2
```

`range()` produces values lazily — it doesn't build the whole list in memory up front.

### If you need the index too: `enumerate()`

```python
# avoid
for i in range(len(numbers)):
    print(i, numbers[i])

# prefer
for i, value in enumerate(numbers):
    print(i, value)
```

---

## 4. `break` vs. `continue`

```text
break     → exit the loop immediately
continue  → skip the rest of this iteration, move to the next one
```

```python
for x in range(10):
    if x == 3:
        continue     # skip 3, keep going
    if x == 7:
        break         # stop entirely at 7
    print(x)
# 0 1 2 4 5 6
```

### Real-world pattern: process, skip, or abort

```python
transactions = [12.50, 0.99, 450.00, -5.00, 89.90]   # note the negative — an error case

for amount in transactions:
    if amount < 0:
        print(f"CRITICAL ERROR: negative transaction detected ({amount})!")
        break                                            # check this first — -5.00 is also <= 1.00

    if amount <= 1.00:
        print(f"Skipping minor transaction: ${amount} (below threshold)")
        continue                                          # small amounts: skip, keep going

    print(f"Processed transaction: ${amount}")
```

**Order matters here** — checking `amount < 0` *before* `amount <= 1.00` is deliberate: `-5.00` also satisfies `<= 1.00`, so if the skip-check ran first, the negative amount would get silently skipped instead of triggering the critical-error `break`.

---

## 5. Nested Loops

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

For each `i`, the *entire* inner loop over `j` runs before `i` advances. This is the pattern behind matrix/grid traversal in [03-lists-slicing-and-multidimensional-data.md](03-lists-slicing-and-multidimensional-data.md).

---

## 6. Composable Loop Patterns

Three shapes you'll reuse constantly — recognize them as patterns, not one-off examples.

**Filter** — keep only what matches:

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
# [2, 4, 6]
```

**Search** — stop at the first match:

```python
numbers = [10, 20, 40, 70, 90]
for number in numbers:
    if number > 50:
        print(number)   # 70
        break
```

**Skip** — ignore certain values, keep looping:

```python
numbers = [10, -2, 30, -5, 40]
for number in numbers:
    if number < 0:
        continue
    print(number)        # 10 30 40
```

---

## Mastery Checkpoint

Trace this by hand, without running it:

```python
numbers = [12, 7, 18, 3, 25, 10]
result = []
for x in numbers:
    if x > 10 and x % 2 == 0:
        result.append(x)
```

```text
12 → >10 yes, even yes → keep
7  → >10 no
18 → >10 yes, even yes → keep
3  → >10 no
25 → >10 yes, even no
10 → >10 no

result = [12, 18]
```

Being able to trace code like this in your head matters more than memorizing syntax.

---

## Practice

Work these in a blank `.py` file — no tutorial, no AI assistant — before checking your solution against anything. Stub these into [practice_control_flow.py](practice_control_flow.py) yourself; solutions are intentionally not included there.

**Blank-IDE challenges**

- [ ] Number classifier — read a number, print `Positive even` / `Positive odd` / `Negative even` / `Negative odd` / `Zero`.
- [ ] Grade calculator — read a score `0–100`, print `A`/`B`/`C`/`D`/`F` using `if/elif/else`.
- [ ] Number search — in `[12, 45, 7, 89, 34, 90, 23]`, find the first number greater than `50` using `for`/`if`/`break`.
- [ ] Filtering — from `[12, 5, 8, 21, 30, 7, 44]`, build a new list of only the numbers divisible by 2.
- [ ] Reverse — reverse `[1, 2, 3, 4, 5]` with a loop, without `.reverse()` or `[::-1]`.
- [ ] Bitwise prediction — predict, then verify: `5 & 3`, `5 | 3`, `5 ^ 3`, `5 << 1`, `8 >> 1`.

**Day 3 exercises** (from the 30 Days of Python course — see references)

- [ ] Declare age (`int`), height (`float`), and a complex-number variable.
- [ ] Triangle area from user-entered base and height (`area = 0.5 * b * h`).
- [ ] Triangle perimeter from three user-entered sides.
- [ ] Rectangle area & perimeter from user-entered length/width.
- [ ] Circle area & circumference from a user-entered radius (`pi = 3.14`).
- [ ] Slope and y-intercept of `y = 2x - 2`; slope + Euclidean distance between `(2, 2)` and `(6, 10)`; compare the two slopes.
- [ ] Evaluate `y = x^2 + 6x + 9` for several `x`; find the `x` where `y == 0`.
- [ ] Compare `len('python')` vs `len('dragon')` with a falsy comparison statement.
- [ ] Use `and` to check whether `'on'` is in both `'python'` and `'dragon'`.
- [ ] Use `in` to check whether `'jargon'` appears in a sentence of your choice.
- [ ] Convert `len('python')` to `float`, then to `str`.
- [ ] Check whether a number is even using `%`.
- [ ] Check whether `7 // 3 == int(2.7)`.
- [ ] Check whether `type('10') == type(10)` and whether `int('9.8') == 10`.
- [ ] Weekly pay from user-entered hours and rate per hour.
- [ ] Seconds lived, from a user-entered number of years (assume a 100-year lifespan for scale).
- [ ] Print a multiplication table (1–5) using nested loops.

## References

- [Python Tutorial — More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (`if`, `for`, `range`, `break`, `continue`)
- [30 Days of Python](https://github.com/Asabeneh/30-Days-Of-Python) by Asabeneh Wolde Giorgis — source of the Day 3 exercise list above
