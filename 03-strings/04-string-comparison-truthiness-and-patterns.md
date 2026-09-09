# Module 3 (cont.) — Comparison, Truthiness & Common String Patterns

> Stage: 03-strings · Status: In progress · Last updated: 2026-09-09
> Notes compiled by: BHAVANA

## Summary

The "gotcha" layer — the things that look obvious until they bite you in an interview or a real bug — plus the handful of loop/string patterns (palindrome, anagram, dedupe, frequency count) that recur constantly.

Runnable practice: [practice_strings_patterns.py](practice_strings_patterns.py)

---

## 1. `==` vs. `is` — Use `==` for String Comparison, Always

```python
a, b = "Python", "Python"
a == b     # True  — compares VALUE — this is what you want
a is b       # may also be True, but only because CPython sometimes "interns" small/simple strings
```

**Never rely on `is` for string equality.** Interning is a CPython implementation detail, not a language guarantee — it can differ across strings, versions, and even how the string was built (literal vs. concatenated at runtime). Use `is` only for identity checks that are actually about identity, like `x is None`.

---

## 2. Lexicographic Comparison — `ord()` and `chr()`

Strings compare based on Unicode code points, left to right:

```python
"apple" < "banana"   # True
"Z" < "a"               # True — surprising until you check the code points
```

```python
ord("Z")    # 90
ord("a")     # 97
```

`chr()` is the inverse of `ord()`:

```python
chr(65)     # "A"
chr(97)      # "a"
```

Useful whenever a problem is really about character *codes* rather than characters as text (e.g. Caesar ciphers, alphabet-index tricks).

---

## 3. Truthiness Traps

An empty string is falsy; almost everything else is truthy — **including strings that merely look false**:

```python
bool("")          # False
bool(" ")           # True  — a single space is a non-empty string
bool("False")        # True  — !! the TEXT "False" is still a non-empty string, so it's truthy
```

```python
if "False":
    print("this runs")   # it does — don't test string content by dropping it straight into `if`
```

If you actually need to interpret text as a Boolean (e.g. from a config file or user input), compare explicitly: `value.lower() == "true"`.

---

## 4. `str()` vs. `repr()`

```python
s = "Hello\nWorld"
print(str(s))     # prints an actual newline
print(repr(s))       # 'Hello\nWorld'  — shows the escape sequence, unambiguous for debugging
```

Reach for `repr()` (or just evaluate the variable in a REPL) when you need to see *exactly* what's in a string, whitespace and all.

---

## 5. Reversing, Sorting, Min/Max

```python
s = "Python"
s[::-1]                           # "nohtyP"  — the idiomatic way

"".join(reversed(s))               # also "nohtyP" — but reversed() alone returns an ITERATOR, not a string
```

```python
sorted("python")     # ['h', 'n', 'o', 'p', 't', 'y']  — sorted() ALWAYS returns a list, even from a string
"".join(sorted("python"))     # "hnopty" — join it back into a string if that's what you need

min("python")     # 'h' — compares by character/Unicode value
max("python")      # 'y'
```

---

## 6. `enumerate()` with Strings

```python
for index, char in enumerate("Python"):
    print(index, char)
```

Cleaner than `for i in range(len(s)): ... s[i] ...` whenever you need both the position and the character.

---

## 7. Building Strings Efficiently

```python
# works, but can be costly for large inputs — every += creates a whole new string
result = ""
for char in some_long_string:
    result += char
```

Because strings are immutable, repeated `+=` in a loop keeps allocating new strings. Prefer collecting into a list and joining once at the end:

```python
parts = []
for char in some_long_string:
    parts.append(char)
result = "".join(parts)
```

---

## 8. Recurring String Patterns

### Palindrome check

```python
s = "madam"
s == s[::-1]     # True
```

Case-insensitive version:

```python
s = "Madam".casefold()
s == s[::-1]
```

### Anagram check

```python
a, b = "listen", "silent"
sorted(a) == sorted(b)     # True — simple, O(n log n)

from collections import Counter
Counter(a) == Counter(b)     # True — O(n), and clearer once you know Counter
```

### Vowel counting — iterate + condition, the pattern behind a lot of string problems

```python
s = "Python Programming"
count = 0
for char in s.lower():
    if char in "aeiou":
        count += 1
```

### Removing duplicate characters while keeping first-occurrence order

```python
s = "banana"
seen = set()
result = []
for char in s:
    if char not in seen:
        seen.add(char)
        result.append(char)
"".join(result)     # "ban"
```

`"".join(set(s))` is tempting but **wrong** here — a `set` doesn't preserve order, so the character order in the output isn't guaranteed to match the original.

### Character frequency — reach for `Counter` over hand-rolled loops

```python
from collections import Counter
Counter("banana")     # Counter({'a': 3, 'n': 2, 'b': 1})
```

### Stripping *all* whitespace (not just the edges)

```python
s = " hello \n world \t python "
"".join(s.split())     # "helloworldpython"
```

`s.strip()` only removes whitespace from the two ends — it won't touch the tabs/newlines in the middle. `split()` (no argument) followed by `join("")` removes it everywhere.

---

## Practice

Work these yourself — solutions aren't included in [practice_strings_patterns.py](practice_strings_patterns.py):

- [ ] Write your own palindrome checker without slicing (`[::-1]`) — use a loop or two pointers instead.
- [ ] Write your own anagram checker without `sorted()` or `Counter` — count characters manually with a `dict`.
- [ ] Given a sentence, find the position of the **last** occurrence of a repeated word using `rfind()`/`rindex()`.
- [ ] Given `['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']`, join it into `"Django# Flask# Bottle# Pyramid# Falcon"`.
- [ ] Reproduce this table using `\t`, with your own name in place of the example:
  ```text
  Name      Age     Country   City
  Bhavana   ??      ??        ??
  ```
- [ ] Using string formatting (any of the three styles), reproduce: `The area of a circle with radius 10 is 314.00 meters square.`
- [ ] Using string formatting, reproduce all seven lines of: `8 + 6 = 14`, `8 - 6 = 2`, `8 * 6 = 48`, `8 / 6 = 1.33`, `8 % 6 = 2`, `8 // 6 = 1`, `8 ** 6 = 262144`.

## References

- [30 Days of Python — Day 4: Strings](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/04_Day_Strings) by Asabeneh Wolde Giorgis — source of the exercise list above
- [Python Standard Library — `collections.Counter`](https://docs.python.org/3/library/collections.html#collections.Counter)
