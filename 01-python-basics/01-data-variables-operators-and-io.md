# Module 1 — Data, Variables, Operators, Expressions, Input & Output

> Stage: 01-python-basics · Status: In progress · Last updated: 2026-09-09
> Notes compiled by: BHAVANA

## Summary

Foundational layer used everywhere later (ML, APIs, data processing, debugging, LLM engineering): what "data" is in Python, how variables actually work (names bound to objects, not boxes), operators/expressions/precedence, type conversion, and reading/writing data via `input()`/`print()`.

```text
                 PYTHON PROGRAM
                       │
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
      DATA          VARIABLES       OPERATORS
        │              │              │
        └──────────────┼──────────────┘
                       ↓
                  EXPRESSIONS
                       ↓
                    VALUES
                       ↓
              OUTPUT / INPUT
```

---

## 1. Data — Python's Built-in Types

`22` in `age = 22` is **data** — specifically, an integer object. Python represents different kinds of data as different object types.

| Type | Meaning | Example |
|---|---|---|
| `int` | Integers | `age = 22` |
| `float` | Decimal numbers | `price = 99.50` |
| `complex` | Complex numbers | `z = 3 + 4j` |
| `bool` | True / False | `is_logged_in = True` |
| `str` | Text | `name = "Bhavana"` |
| `None` | Absence of a value | `result = None` |

Collections (`list`, `tuple`, `set`, `dict`) are covered separately in [03-data-structures](../03-data-structures/).

### `int` — arbitrary precision

Unlike fixed-size integers in C/C++, Python's `int` can grow arbitrarily large (limited only by memory):

```python
x = 999999999999999999999999999999999999   # perfectly valid
```

### `float` — an approximation, not exact decimal arithmetic

```python
0.1 + 0.2
# 0.30000000000000004
```

Binary floating-point can't represent many decimal fractions exactly. Matters later for ML, finance, and any precision-sensitive computation — **`float` is an approximation, not arbitrary-precision decimal arithmetic.**

### `complex`

```python
z = 3 + 4j
z.real   # 3.0
z.imag   # 4.0
```

Python uses `j`, not `i`, for the imaginary part. Rare in ordinary AI engineering, but good to know it exists.

### `bool` — a subtype of `int`

```python
True == 1    # True
False == 0   # True
```

Useful to know it exists; don't overuse this fact in real code.

### `str`

```python
name = "Bhavana"   # double or single quotes — same type either way
name = 'Bhavana'
```

### `"22"` is NOT `22` — one of the most important beginner concepts

```python
type(22)     # <class 'int'>
type("22")   # <class 'str'>
```

```text
22    → a number
"22"  → text containing the characters 2 and 2
```

Matters constantly when receiving data from users, APIs, files, databases, or CLI args — it always arrives as text until you convert it.

### `None`

Represents "no value / no meaningful result here." Distinct from `0`, `False`, and `""` — they mean different things and are not interchangeable with `None`.

---

## 2. Variables — a Name Bound to an Object

The common beginner analogy — "a box called `x` holding `10`" — is useful but not how Python actually works. Python's real model:

> **A name is bound to an object.**

```text
       x
       │
       ▼
    ┌─────┐
    │ 10  │
    │ int │
    └─────┘
```

```python
x = 10
```

means: create/find the integer object `10`, then bind the name `x` to it. This distinction becomes essential later for mutability, references, memory, lists, functions, object identity, and copying.

**Reassignment changes the binding, not the object:**

```python
x = 10
x = 20   # x is now bound to 20 — you did not "modify" the integer 10
```

---

## 3. Assignment vs. Equality

```text
=    assignment   → bind a name to a value
==   comparison   → is the value equal to this?
```

```python
x = 10          # assignment: bind x to 10
print(x == 10)  # comparison: True
```

This confusion is one of the most common beginner mistakes once conditions (`if`) show up.

### Multiple / swap assignment

```python
x, y = 10, 20      # x → 10, y → 20
x, y = y, x         # swap — no temp variable needed → x → 20, y → 10
```

---

## 4. Naming Variables

Identifiers can contain letters, digits, and underscores, but can't start with a digit; keywords can't be used as identifiers.

| Valid | Invalid | Why |
|---|---|---|
| `name`, `_name`, `name2`, `user_name` | `2name` | can't start with a digit |
| | `user-name` | parsed as `user - name` (subtraction), not one identifier |
| | `class` | reserved keyword |

### Conventions

| Kind | Convention | Example |
|---|---|---|
| Variables / functions | `snake_case` | `total_price`, `calculate_total()` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_RETRIES = 3` |
| Classes | `PascalCase` / CapWords | `UserAccount`, `RAGPipeline` |

### Write meaningful names

```python
# bad
a = 20
b = 30
c = a * b

# better
price = 20
quantity = 30
total = price * quantity
```

### Don't shadow built-ins

Avoid naming variables `list`, `str`, `int`, `dict`, `set`, `sum`, `input`, `print`, etc. — doing so hides the built-in for the rest of that scope:

```python
sum = 100
sum([1, 2, 3])   # breaks — `sum` is now your int, not the built-in function
```

---

## 5. Operators

```text
+   addition
-   subtraction
*   multiplication
/   division           → always returns a float
//  floor division     → discards the remainder
%   remainder / modulo
**  exponentiation      (NOT `^` — that's bitwise XOR)
```

```python
10 / 5     # 2.0   (float, always)
17 // 3    # 5     (floor division)
17 % 3     # 2     (remainder)
2 ** 3     # 8     (power)
2 ^ 3      # 1     (bitwise XOR — NOT power; a common beginner trap)
```

**Modulo is a common even/odd check:**

```python
number % 2 == 0   # True if number is even
```

### Operator precedence (simplified, highest → lowest)

```text
()
**
+x, -x            (unary plus/minus)
*, /, //, %
+, -
comparisons (==, !=, <, >, <=, >=)
not
and
or
```

```python
5 + 3 * 2        # 11 — multiplication before addition
2 + 3 * 4        # 14
(2 + 3) * 4      # 20 — parentheses override precedence
```

Use parentheses even when not strictly required if they make intent clearer:

```python
result = (price * quantity) + tax
```

### Comparison operators

`==`, `!=`, `<`, `>`, `<=`, `>=` — all produce a `bool`:

```python
age = 22
age >= 18   # True
```

### Logical operators

`and`, `or`, `not`:

```python
age >= 18 and has_id
```

(Deeper coverage with control flow in [02-control-flow](../02-control-flow/).)

### Augmented assignment operators

```python
x += 5   # same as x = x + 5
x -= 2
x *= 3
x /= 4
x //= 2
x %= 2
x **= 2
```

### The walrus operator `:=` (Python 3.8+)

Assigns *and* returns a value in one expression:

```python
if (n := len(data)) > 10:
    print(n)
```

Not a priority to use yet — just recognize it when you see it.

---

## 6. Expressions vs. Statements

An **expression** is anything Python can evaluate to produce a value: `10`, `x`, `x + 10`, `price * quantity`, `x > 10`, `name.upper()`.

An **assignment statement** *uses* an expression's result but isn't itself a value:

```text
2 + 3            → expression → 5
x = 2 + 3        → assignment statement → binds x to 5
```

Bigger expressions are built from smaller ones:

```python
total = price * quantity + tax
```

contains the sub-expressions `price`, `quantity`, `price * quantity`, `tax`, and the whole `price * quantity + tax` — evaluated according to precedence, innermost/highest-precedence first.

**Vocabulary:** in `price * quantity`, `price` and `quantity` are **operands**, `*` is the **operator**, and `price * quantity` is the **expression**.

---

## 7. Type Compatibility & Conversion

Not every operator works across every type:

```python
10 + 20      # fine
10 + "20"    # TypeError — int + str is not defined; Python won't guess your intent
```

Some numeric types *do* interact naturally — Python promotes `int` to `float` automatically when mixed:

```python
4 * 3.75     # 15.0
5 + 2.5      # 7.5     (int + float → float)
```

**String operators work too** — but only between compatible types:

```python
"Hello " + "World"   # "Hello World"   (concatenation)
"ha" * 3              # "hahaha"        (repetition)
"Age: " + 22          # TypeError — str + int is invalid
"Age: " + str(22)     # "Age: 22"       — must convert explicitly
```

### Explicit conversion functions

```python
int("42")            # 42
int(3.9)              # 3           — truncates, doesn't round
int("3.9")             # ValueError — not an integer-shaped string
int(float("3.9"))       # 3           — convert to float first, then int

float("3.14")          # 3.14
float(10)               # 10.0

str(22)                 # "22"

bool(1)                  # True
bool(0)                   # False
```

### Truthy / falsy values

Common falsy values: `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`. Everything else is truthy. (Deeper coverage with control flow.)

### Why `+` behaves differently by type (preview of polymorphism)

```text
             +
            / \
         int  int  →  add
         str  str  →  concatenate
```

Same operator, different behavior depending on operand types — this is an early glimpse of polymorphism / Python's data model (`__add__`, etc.), covered properly in [05-oop](../05-oop/).

---

## 8. Output — `print()`

```python
print("Hello")                          # Hello
print(name, age)                         # space-separated by default
print("Hello", "World", sep="-")          # Hello-World
print("Hello", end=" "); print("World")   # Hello World  (no newline after first)
```

### f-strings — the default formatting technique

```python
print(f"My name is {name} and I am {age}")
print(f"Total: {price * quantity}")        # expressions work inside {}
```

### Format specs

```python
f"{price:.2f}"          # 2 decimal places      → 1234.57
f"{population:,}"        # thousands separator    → 123,456,789
f"{accuracy:.2%}"         # percentage              → 95.67%
```

---

## 9. Input — `input()` Always Returns a `str`

**The single most important fact about `input()`:** whatever the user types comes back as a string — even if it looks like a number.

```text
User types: 22  →  input()  →  "22"  (str, not int)
```

```python
age = input("Age: ")
next_year = age + 1        # TypeError — str + int
```

Fix — convert explicitly:

```python
age = int(input("Age: "))
next_year = age + 1        # works: "22" → int() → 22 → +1 → 23
```

The pattern `value = int(input(...))` / `value = float(input(...))` is one to internalize.

**Conversion can fail** — if the user types `"twenty-two"` instead of `"22"`, `int(...)` raises `ValueError`. Handling that properly needs `try`/`except`, covered below and more fully in [08-error-handling](../08-error-handling/).

---

## 10. Putting It Together

```python
name = input("Name: ")
age = int(input("Age: "))
salary = float(input("Monthly salary: "))

next_year_age = age + 1
annual_salary = salary * 12

print("----- PROFILE -----")
print(f"Name: {name}")
print(f"Current age: {age}")
print(f"Age next year: {next_year_age}")
print(f"Annual salary: ₹{annual_salary:,.2f}")
```

```text
input:  Name: Bhavana / Age: 22 / Monthly salary: 40000
output:
----- PROFILE -----
Name: Bhavana
Current age: 22
Age next year: 23
Annual salary: ₹480,000.00
```

This one small program already uses: input, type conversion, variables, assignment, expressions, operators, `float`/`int`, f-strings, formatting, and output.

**Full data-flow trace, for `price = float(input("Price: "))`:**

```text
input("Price: ")  →  user types "99.50"  →  input() returns "99.50" (str)
     ↓
float("99.50")  →  99.5 (float)
     ↓
assignment: price → 99.5
```

---

## 11. Ten Things to Remember

1. `x = 10` is **assignment**, not equality.
2. `x == 10` is **comparison**.
3. A variable is a **name bound to an object**, not a labeled box.
4. `input()` always returns a **string**.
5. Convert user input explicitly: `age = int(input(...))`.
6. `/` always produces a **float**: `5 / 2 → 2.5`.
7. `//` is **floor division**: `5 // 2 → 2`.
8. `%` gives the **remainder**: `5 % 2 → 1`.
9. Use **f-strings** for formatted output: `f"Age: {age}"`.
10. An **expression produces a value**; a statement (like assignment) does not.

---

## 12. Practice Problems

Work these independently in a blank `.py` file before checking anything against a tutorial or AI tool — that's the point.

- [ ] Calculate `num_one` to the power of `num_two`, assign to `exp`.
- [ ] Find the floor division of `num_one` by `num_two`, assign to `floor_division`.
- [ ] A circle has radius `30` meters — calculate its area, assign to `area_of_circle`.
- [ ] Calculate the same circle's circumference, assign to `circum_of_circle`.
- [ ] Take the radius as user input instead, and calculate the area.
- [ ] Use `input()` to collect first name, last name, country, and age, storing each in its own variable.
- [ ] Compare the length of your first name vs. last name.

**Blank-IDE challenge** (bigger, no tutorial/AI tool while attempting it):

> Ask the user for name, age, monthly income, and monthly expenses. Calculate annual income, annual expenses, monthly savings, annual savings, and savings percentage. Display a clean, formatted report.

Then deliberately enter invalid input into your own program and watch what breaks — that's the bridge from "I can write Python" to "I understand what Python is doing when my program breaks."

---

## 13. Debugging Notes — Real Mistakes & Fixes

Lessons from actually running the practice problems above, not just reading theory.

### `sum()` expects an iterable, not two separate numbers

```python
num1 = 5
num2 = 4
total = sum(num1, num2)   # TypeError: 'int' object is not iterable
```

`sum()` expects a single iterable (list/tuple/etc.) of numbers to add up — `sum(5, 4)` tries to iterate over `5`, which fails. Fix:

```python
total = num1 + num2          # correct tool for adding two numbers
# or, if sum() specifically is wanted:
total = sum([num1, num2])    # pass them wrapped in a list
```

### Comparing name lengths — cleaner version

Correct but verbose:

```python
first = "Bhavana"
last = "buddha"
a = len(first)
b = len(last)
print(max(a, b))
```

More Pythonic — skip the intermediate variables, call `len()` directly inside `max()`:

```python
first = "Bhavana"
last = "buddha"
print(max(len(first), len(last)))
```

More descriptive, if the goal is a readable report rather than just a number:

```python
print(f"First name length: {len(first)}")
print(f"Last name length: {len(last)}")
print(f"Maximum length: {max(len(first), len(last))}")
```

### `input()` silently accepts garbage — because it's always a string

```python
first_name = input("Enter your first name: ")
country    = input("Enter your country: ")
age        = input("Enter your age: ")
```

Typing `123` for country, or `2hsg` for age, doesn't error at the `input()` call — both are perfectly valid *strings*. The problem only surfaces later, when you try to use `age` as a number.

### `int(input(...))` crashes on bad input — that's sometimes fine, sometimes not

```python
age = int(input("Enter your age: "))   # ValueError if user types "2hsg"
```

This is a legitimate choice, not automatically wrong:

- **Fine to use as-is** for simple/trusted scripts, or when you deliberately want the program to **fail fast** on bad input.
- **Not fine** when the program needs to keep running and give the user another chance.

For the "keep running" case, loop with `try`/`except` as a safety net:

```python
while True:
    try:
        age = int(input("Enter your age: "))
        break                      # only reached if int() succeeded
    except ValueError:
        print("Invalid input! Please enter a valid number for your age.")
```

Optionally validate names contain only letters using `str.isalpha()`:

```python
while True:
    first_name = input("Enter your first name: ")
    if first_name.isalpha():
        break
    print("Invalid name! Please use letters only.")
```

`try`/`except` is covered properly in [08-error-handling](../08-error-handling/) — this is a first preview, triggered by hitting the problem directly rather than reading about it first.

---

## References

- [Python Tutorial — Numbers, Strings & Basic Expressions](https://docs.python.org/3/tutorial/introduction.html)
- [Python Language Reference — Expressions](https://docs.python.org/3/reference/expressions.html) (operator precedence, evaluation order)
- [Python Language Reference — Execution Model](https://docs.python.org/3/reference/executionmodel.html) (names, bindings)
- [Python Language Reference — Lexical Analysis, Identifiers](https://docs.python.org/3/reference/lexical_analysis.html#identifiers)
- [What's New in Python 3.8](https://docs.python.org/3/whatsnew/3.8.html) — introduces the walrus operator `:=`
