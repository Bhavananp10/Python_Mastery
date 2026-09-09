# Module 2 — Booleans, Comparisons, Logical & Bitwise Operators

> Stage: 02-control-flow · Status: In progress · Last updated: 2026-09-09
> Notes compiled by: BHAVANA

## Summary

The layer that turns raw values into decisions: Booleans, comparisons, logical operators (`and`/`or`/`not`), truthiness, and bitwise operators — the vocabulary control flow (Module 2, part 2) is built on.

```text
   DATA → COMPARISON → True/False → DECISION
```

Runnable practice for everything in this note: [practice_operators.py](practice_operators.py).

---

## 1. Booleans

Python has exactly two Boolean values, and unlike JavaScript, both are capitalized:

```python
True
False
type(True)   # <class 'bool'>
```

Booleans exist to answer: *is this true? is this false? should this code run? should this loop continue?*

---

## 2. Comparisons Produce Booleans

| Operator | Meaning |
|---|---|
| `==` | equal |
| `!=` | not equal |
| `<` | less than |
| `>` | greater than |
| `<=` | less than or equal |
| `>=` | greater than or equal |

```python
x, y = 10, 20
x < y   # True
```

**Reminder** (from [Module 1](../01-python-basics/01-data-variables-operators-and-io.md)): `=` assigns, `==` compares. Never mix them up in a condition.

```python
age = 22
is_adult = age >= 18   # a Boolean expression → feeds directly into decisions
```

### Chained comparisons

Python lets you chain comparisons directly, evaluating each intermediate expression once:

```python
x = 15
if 10 < x < 20:      # equivalent to: 10 < x and x < 20
    print("Between 10 and 20")
```

---

## 3. Arithmetic Operators — Quick Recap, Applied

Covered in [Module 1](../01-python-basics/01-data-variables-operators-and-io.md); here they're applied to real formulas (area, circumference, weight, density) instead of bare numbers — connecting operators to something worth calculating:

```python
radius = 10
area_of_circle = 3.14 * radius ** 2        # note: ** binds tighter than *

length, width = 10, 20
area_of_rectangle = length * width

mass, gravity = 75, 9.81
weight = mass * gravity                     # in Newtons

volume = 0.075                               # cubic meters
density = mass / volume                      # kg/m^3
```

See [practice_operators.py](practice_operators.py) for the runnable version with labeled output.

---

## 4. Logical Operators — `and`, `or`, `not`

Python spells these out as keywords rather than symbols (`&&`, `||`, `!` in many other languages).

### `and` — both must be true

| A | B | `A and B` |
|---|---|---|
| False | False | False |
| False | True | False |
| True | False | False |
| True | True | **True** |

### `or` — at least one must be true

| A | B | `A or B` |
|---|---|---|
| False | False | False |
| False | True | **True** |
| True | False | **True** |
| True | True | **True** |

### `not` — flips truth

```python
not True    # False
not False   # True
```

### Precedence: `and` binds tighter than `or`

```python
a, b, c = True, False, True
a or b and c
```

is `a or (b and c)`, **not** `(a or b) and c`. When it matters, add parentheses — readable beats clever:

```python
if (age >= 18) and (has_license or is_supervised):
    ...
```

### Identity vs. equality: `is` vs. `==`

```python
a, b = 1, 1
a == b   # True — same value
a is b   # True — CPython caches small ints, so they're also the same object
```

`==` asks "same value?"; `is` asks "same object in memory?" They usually agree for small integers and interned strings (a CPython implementation detail), but this is not guaranteed in general — prefer `==` unless you specifically mean identity (e.g. `x is None`).

Also useful:

```python
"coding" in "coding for all"   # True  — substring/element membership
"B" not in "team"                # True — negated membership
```

---

## 5. Truthiness — You Don't Always Need an Actual `True`/`False`

Python treats certain values as **falsy** in a Boolean context, everything else as **truthy**:

```text
False   None   0   0.0   ""   []   {}   set()
```

```python
items = []
if items:
    print("There are items")
else:
    print("Empty")     # this runs — an empty list is falsy
```

Checking explicitly: `bool(0)` → `False`, `bool("hello")` → `True`, `bool([])` → `False`, `bool([1, 2])` → `True`.

This pattern — `if some_list:` instead of `if len(some_list) > 0:` — is idiomatic, professional Python.

---

## 6. Logical vs. Bitwise — Don't Confuse These

| | Logical (`and`, `or`, `not`) | Bitwise (`&`, `\|`, `^`, `~`, `<<`, `>>`) |
|---|---|---|
| Operates on | whole Boolean/truthy values | individual bits of integers |
| Short-circuits? | Yes — stops as soon as the result is certain | No — evaluates every bit |
| Typical use | linking conditions in `if` statements | flags/permissions, cryptography, hardware/networking, low-level formats |

```python
is_active, is_admin = False, True
if is_active and is_admin:      # short-circuits on is_active=False, never checks is_admin
    print("Access granted")
```

### Binary, worked out

```text
5 = 0101
3 = 0011
```

| Expression | Bit math | Result |
|---|---|---|
| `5 & 3` (AND) | `0101 & 0011 = 0001` | `1` |
| `5 \| 3` (OR) | `0101 \| 0011 = 0111` | `7` |
| `5 ^ 3` (XOR — 1 where bits differ) | `0101 ^ 0011 = 0110` | `6` |

### Why an AI engineer should still know this

Bit-level thinking resurfaces in binary formats, permission flags, networking, compression, cryptography, systems/GPU programming, and quantization — not everyday Python, but not disposable trivia either.

---

## Key Vocabulary

| Term | Meaning |
|---|---|
| Boolean expression | An expression that evaluates to `True`/`False` |
| Truthy / falsy | How a non-Boolean value behaves in a Boolean context |
| Short-circuit evaluation | Stopping evaluation once the logical result is already determined |
| Bitwise operator | Operates on the binary representation of integers, bit by bit |

## References

- [Python Tutorial — More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
- [Python Language Reference — Expressions](https://docs.python.org/3/reference/expressions.html) (Boolean operations, comparisons, bitwise operations, chained comparisons)
- [30 Days of Python](https://github.com/Asabeneh/30-Days-Of-Python) by Asabeneh Wolde Giorgis — original inspiration for the Day 3 practice exercises this note and [practice_operators.py](practice_operators.py) are built from
