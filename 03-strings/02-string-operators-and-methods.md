# Module 3 (cont.) — String Operators & Built-in Methods

> Stage: 03-strings · Status: In progress · Last updated: 2026-09-09
> Notes compiled by: BHAVANA

## Summary

Strings support a handful of algebraic-looking operators repurposed for sequences (`+`, `*`, `in`), plus a large set of built-in methods. Every method here **returns a new string (or list) — none of them mutate the original**, because strings are immutable (see [01-string-basics-creation-and-immutability.md](01-string-basics-creation-and-immutability.md)).

Runnable practice: [practice_strings_methods.py](practice_strings_methods.py)

---

## 1. Core Operators

```python
"Hello" + " " + "World"    # "Hello World"      — concatenation
"=" * 20                     # "===================="  — repetition
"Alert" in payload              # membership test → bool
```

### Edge cases worth knowing

```python
"Hi" * 0     # ""   — zero repetitions
"Hi" * -2      # ""   — negative repeat count also gives an empty string
```

### Concatenation only works string-to-string

```python
age = 22
"Age: " + age          # TypeError — str + int
"Age: " + str(age)       # "Age: 22" — convert explicitly
f"Age: {age}"              # "Age: 22" — or just use an f-string
```

---

## 2. Method Categories at a Glance

| Category | Methods |
|---|---|
| Case | `upper()` `lower()` `capitalize()` `title()` `swapcase()` `casefold()` |
| Whitespace | `strip()` `lstrip()` `rstrip()` |
| Search | `find()` `rfind()` `index()` `rindex()` `count()` `startswith()` `endswith()` |
| Split / join | `split()` `rsplit()` `splitlines()` `join()` |
| Modify | `replace()` |
| Testing (`bool`) | `isalpha()` `isdigit()` `isdecimal()` `isnumeric()` `isalnum()` `isspace()` `islower()` `isupper()` `isidentifier()` |

---

## 3. Case Methods

```python
"python".capitalize()    # "Python"        — only the first character
"python programming language".title()   # "Python Programming Language"
"PyThOn".swapcase()       # "pYtHoN"
```

**`casefold()` vs. `lower()`**: for plain English, `lower()` is enough. `casefold()` is the more aggressive, Unicode-aware version, meant specifically for caseless comparisons:

```python
"HELLO".casefold() == "hello".casefold()   # True — the intended way to compare case-insensitively
```

---

## 4. Whitespace Methods

```python
"   Python   ".strip()      # "Python"    — trims both ends only
"   Python   ".lstrip()       # "Python   "
"   Python   ".rstrip()        # "   Python"
```

### Trap: `strip(chars)` removes a *character set*, not a substring

```python
"banana".strip("na")     # "b"  — NOT "removes the substring 'na' from each end"
```

`strip("na")` removes any leading/trailing characters that are `n` *or* `a` — a **set** of characters, applied repeatedly from both ends until a character outside the set is hit. There's no `"na"` substring at either end of `"banana"` to begin with, yet three characters still get stripped from the right (`a`, `n`, `a`) because each one individually belongs to the set `{n, a}`.

```python
"---Python---".strip("-")     # "Python" — this simpler case looks like substring removal, but it's really the same character-set rule
```

`strip("noth")` removes any leading/trailing characters that are `n`, `o`, `t`, or `h` — a *set*, not a phrase.

---

## 5. Search Methods

### `find()` vs. `index()` — the trap that shows up in interviews

| Method | Substring not found |
|---|---|
| `find()` | returns `-1` |
| `index()` | raises `ValueError` |

```python
s = "Python"
s.find("th")     # 2
s.find("xyz")      # -1          — safe to check with an if
s.index("xyz")       # ValueError  — must be wrapped in try/except if uncertain
```

`rfind()` / `rindex()` are the same pair, searching from the right instead.

### `count()` counts non-overlapping occurrences only

```python
"banana".count("a")     # 3
"aaa".count("aa")          # 1, not 2 — after matching the first "aa", it continues from *after* the match
```

### `startswith()` / `endswith()` — clean boundary checks

```python
"Python Programming".startswith("Python")   # True
"report.pdf".endswith(".pdf")                  # True — the idiomatic way to check a file extension
```

---

## 6. Split & Join

### `split()` — the default (no argument) collapses all whitespace

```python
"Python is powerful".split()      # ['Python', 'is', 'powerful']
```

### Trap: `split()` vs. `split(" ")` are NOT the same on messy whitespace

```python
"hello   world".split()           # ['hello', 'world']                — collapses repeated whitespace
"hello   world".split(" ")          # ['hello', '', '', 'world']         — splits on every literal space
```

### `maxsplit` limits the number of *splits*, not the result length

```python
"one two three four".split(" ", 2)     # ['one', 'two', 'three four']   — 2 splits → 3 pieces
```

### `rsplit()` splits from the right — handy for filenames/paths

```python
"one-two-three".rsplit("-", 1)     # ['one-two', 'three']
```

### `join()` — the separator calls the method, not the list

```python
words = ["Python", "is", "fun"]
" ".join(words)      # "Python is fun"    — correct: separator.join(iterable)
words.join(" ")        # AttributeError — lists don't have .join()
```

`join()` requires every element to already be a string:

```python
numbers = [1, 2, 3]
",".join(numbers)               # TypeError
",".join(map(str, numbers))      # "1,2,3" — convert first
```

---

## 7. Testing Methods (all return `bool`)

```python
"Python".isalpha()          # True
"Python3".isalpha()           # False — digits aren't alphabetic
"hello world".isalpha()         # False — space isn't alphabetic either

"123".isdigit()               # True
"Python123".isalnum()           # True   (letters + digits)
"Python_123".isalnum()           # False  — underscore doesn't count
"   ".isspace()                    # True

"python".islower()               # True
"PYTHON".isupper()                 # True
"123".islower()                     # False — no cased characters at all, so neither is/upper holds
```

### The `isdecimal()` / `isdigit()` / `isnumeric()` hierarchy

They accept progressively broader sets of "numeric-looking" Unicode characters:

```text
isdecimal()  ⊆  isdigit()  ⊆  isnumeric()
```

For plain ASCII digits like `"123"`, all three agree (`True`). They diverge on special Unicode characters (e.g. `"½".isnumeric()` is `True`, but `"½".isdecimal()` is `False`). For everyday problems, `isdigit()` is the common default.

### `isidentifier()` — valid identifier ≠ valid variable name

```python
"my_variable".isidentifier()      # True
"123abc".isidentifier()             # False — can't start with a digit
"class".isidentifier()               # True — syntactically it LOOKS like a valid name...
```

...but `class` is a reserved keyword, so Python would still reject it as an actual variable name. `isidentifier()` only checks the shape of the string, not whether it's a keyword.

## References

- [Python Standard Library — String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
