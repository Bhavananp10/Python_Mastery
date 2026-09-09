# Module 3 — Strings: Creation, Indexing, Slicing & Immutability

> Stage: 03-strings · Status: In progress · Last updated: 2026-09-09
> Notes compiled by: BHAVANA

## Summary

A Python string (`str`) is an **ordered, immutable sequence of Unicode characters**. Ordered means every character has a position (index); immutable means once created, a string can never be changed in place — every "modification" actually produces a brand-new string object. This file covers how strings are created and how their sequence mechanics (indexing/slicing) work; operators, methods, formatting and comparison traps are in the other files in this stage.

```text
STRING → ordered (index/slice) + immutable (no in-place edits, ever)
```

Runnable practice: [practice_strings_basics.py](practice_strings_basics.py)

---

## 1. Creating Strings

```python
name = "Bhavana"     # double quotes
language = 'Python'   # single quotes — functionally identical
```

Prefer double quotes when the text itself contains an apostrophe, to avoid escaping:

```python
"It's a beautiful day"      # clean
'It\'s a beautiful day'      # works, but noisier
```

### Triple quotes — multiline strings and docstrings

```python
query = """
SELECT user_id, email
FROM production.users
WHERE account_status = 'Active';
"""
```

Triple quotes preserve line breaks and whitespace exactly as typed; they're also how docstrings are written.

### Escape sequences

A backslash introduces a control sequence: `\n` newline, `\t` tab, `\\` a literal backslash, `\'`/`\"` a literal quote.

```python
print("Days\tTopics\tExercises")
print("This is a backslash symbol (\\)")
```

### Raw strings — `r"..."`

Tells Python to treat every backslash as a literal character, ignoring escape sequences. Essential for Windows paths and regex patterns:

```python
standard_path = "C:\new_folder\test.txt"   # bug: \n becomes a newline, \t becomes a tab
raw_path = r"C:\new_folder\test.txt"        # safe: backslashes stay literal
pattern = r"\d+"                              # regex — you want the literal backslash-d
```

---

## 2. Empty Strings and Spaces-as-Characters

```python
s = ""
len(s)   # 0
```

Spaces are real characters and count toward length — a very common source of subtle bugs:

```python
"Python" == " Python"   # False — leading space makes them different
len("Python")            # 6
len(" Python")            # 7
```

---

## 3. Indexing — Zero-Based, and Negative from the End

```python
s = "Python"
#    P y t h o n
#    0 1 2 3 4 5      → positive indices, left to right
#   -6-5-4-3-2-1      → negative indices, right to left

s[0]    # "P"
s[-1]    # "n"   (last character)
s[-2]     # "o"
```

### Classic trap: `s[len(s)]`

```python
s = "Python"
s[len(s)]     # IndexError
```

`len(s)` is `6`, but valid indices only go up to `5` — the length itself is always one past the last valid index.

---

## 4. Slicing

```python
string[start:stop:step]     # start included, stop EXCLUDED, step defaults to 1
```

```python
token = "SECURE_9845_AUTH"
token[0:6]     # "SECURE"
token[7:11]     # "9845"
```

### Defaults — missing start/stop

```python
s = "Python"
s[:3]      # same as s[0:3]   → "Pyt"
s[3:]       # same as s[3:len(s)]  → "hon"
s[:]         # "Python"  (a full copy)
```

### Step, and reversing

```python
s = "Python"
s[0:6:2]      # "Pto"   — indices 0, 2, 4
s[::-1]        # "nohtyP" — step -1 walks backward through the whole string
```

```python
token = "SECURE_9845_AUTH"
token[::-1]     # "HTUA_5489_ERUCES"
```

### More confusing slices worth internalizing

```python
s = "Python"
s[1::2]        # "yhn"          — start at 1, every 2nd character
s[5:1:-1]        # "noht"        — start at 5, step backward, stop BEFORE index 1
```

### Slicing tolerates out-of-range bounds; indexing does not

```python
s = "Python"
s[0:100]     # "Python"  — no error, Python just clamps to the actual length
s[100]        # IndexError — a single out-of-range index always fails
```

---

## 5. Immutability — and the Proof

```python
framework = "Django"
framework[0] = "T"     # TypeError: 'str' object does not support item assignment
```

You cannot change a character in place. The correct approach is to **build a new string**:

```python
framework = "T" + framework[1:]     # "Tjango" — a new string object, reassigned to the same name
```

`s.upper()`, `s.replace(...)`, and every other "modifying" method behave the same way: they return a new string and leave the original untouched.

```python
s = "Python"
s.upper()
print(s)     # still "Python" — upper() returned a new string, but nothing captured it

s = s.upper()   # this is what actually changes what `s` refers to
print(s)     # "PYTHON"
```

---

## Key Vocabulary

| Term | Meaning |
|---|---|
| Sequence | An ordered collection where each element has an index |
| Immutable | Cannot be changed in place; every "edit" creates a new object |
| Escape sequence | `\`+ character, encoding a control character (`\n`, `\t`, ...) |
| Raw string | `r"..."` — backslashes are treated as literal text |
| Slice | `s[start:stop:step]` — extracts a sub-sequence; `stop` is exclusive |

## References

- [Python Tutorial — Strings](https://docs.python.org/3/tutorial/introduction.html#strings)
- [Python Standard Library — Text Sequence Type `str`](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [30 Days of Python — Day 4: Strings](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/04_Day_Strings) by Asabeneh Wolde Giorgis
