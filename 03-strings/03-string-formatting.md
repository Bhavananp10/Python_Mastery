# Module 3 (cont.) — String Formatting

> Stage: 03-strings · Status: In progress · Last updated: 2026-09-09
> Notes compiled by: BHAVANA

## Summary

Three generations of string formatting exist in Python: `%`-formatting (old), `.format()` (Python 3's first replacement), and f-strings (Python 3.6+, the modern default). All three end up producing a plain string — pick f-strings for new code unless you're maintaining something older.

Runnable practice: [practice_strings_formatting.py](practice_strings_formatting.py)

---

## 1. Old-Style `%` Formatting

```python
first_name, last_name, language = "Bhavana", "Buddha", "Python"
"I am %s %s. I teach %s" % (first_name, last_name, language)
# "I am Bhavana Buddha. I teach Python"
```

| Specifier | Meaning |
|---|---|
| `%s` | string (or anything with a string representation) |
| `%d` | integer |
| `%f` | floating point |
| `%.2f` | floating point, fixed to 2 digits after the decimal |

```python
radius, pi = 10, 3.14
area = pi * radius ** 2
"The area of a circle with radius %d is %.2f." % (radius, area)
# "The area of a circle with radius 10 is 314.00."
```

You'll mostly *read* this style in older codebases rather than write it going forward.

---

## 2. `.format()` — Python 3's First Replacement

```python
"I am {} {}. I teach {}".format(first_name, last_name, language)
# "I am Bhavana Buddha. I teach Python"
```

```python
a, b = 4, 3
"{} / {} = {:.2f}".format(a, b, a / b)     # "4 / 3 = 1.33"
```

Same `{:.2f}` format-spec syntax carries over into f-strings below.

---

## 3. f-Strings — the Modern Default (3.6+)

```python
name, age = "Bhavana", 22
f"My name is {name} and I am {age} years old."
```

Expressions — not just variable names — are allowed inside `{}`:

```python
a, b = 4, 3
f"{a} + {b} = {a + b}"       # "4 + 3 = 7"
f"{a} / {b} = {a / b:.2f}"     # "4 / 3 = 1.33"

f"{name.upper()}"               # "BHAVANA" — method calls work too
```

### Format specs you'll use constantly

```python
price = 1234.5678
f"{price:.2f}"          # "1234.57"           — 2 decimal places

population = 1000000
f"{population:,}"         # "1,000,000"          — thousands separator
```

### Alignment and width — useful for tables/CLI output

```python
name = "Python"
f"{name:>10}"      # "    Python"    — right-aligned, width 10
f"{name:<10}"       # "Python    "     — left-aligned
f"{name:^10}"        # "  Python  "      — centered
```

---

## Which Style Should You Use?

| Style | When |
|---|---|
| `%` | Reading legacy code only — avoid for new code |
| `.format()` | Fine, but mostly superseded |
| f-strings | **Default choice for all new code** |

## References

- [Python Standard Library — `printf`-style `%` Formatting](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)
- [Python Standard Library — Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) (covers both `.format()` and f-string format specs)
- [Python Tutorial — f-strings](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)
