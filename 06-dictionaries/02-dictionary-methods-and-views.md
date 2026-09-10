# Module 6 (cont.) — Dictionary Methods, Views & Iteration

> Stage: 06-dictionaries · Status: In progress · Last updated: 2026-09-09
> Notes compiled by: BHAVANA

## Summary

The full toolkit for updating, removing, copying, and iterating dictionaries — plus the two methods (`get()` vs. `setdefault()`) that look similar but behave very differently.

Runnable practice: [practice_dict_methods.py](practice_dict_methods.py)

---

## 1. `update()` — Add/Update Several Keys at Once

```python
person = {"name": "Bhavana", "age": 22}

person.update({"age": 23, "country": "India"})
# {'name': 'Bhavana', 'age': 23, 'country': 'India'}   — existing keys updated, new keys added

person.update(age=24, city="Vizag")   # keyword form works when keys are valid identifiers
```

---

## 2. Removing Items

| Method | Behavior |
|---|---|
| `del d[key]` | removes the key; `KeyError` if missing |
| `d.pop(key)` | removes the key, **returns its value**; `KeyError` if missing |
| `d.pop(key, default)` | removes the key, returns its value, or `default` if missing — no error |
| `d.popitem()` | removes and returns the **last-inserted** key-value pair, as a tuple |
| `d.clear()` | removes everything, leaving `{}` |

```python
person = {"name": "Bhavana", "age": 22, "country": "India"}

age = person.pop("age")            # age == 22, "age" is now gone
person.pop("salary", None)           # None — no KeyError

del person["country"]                  # removes "country"; KeyError if it didn't exist

person = {"name": "Bhavana", "age": 22, "country": "India"}
person.popitem()                          # ('country', 'India') — order matters, see below
```

---

## 3. `copy()` vs. Plain Assignment — the Big Trap

```python
a = {"x": 1}
b = a              # NOT a copy — b and a refer to the SAME dictionary

b["x"] = 99
a["x"]        # 99 — mutating b also changed a
```

```text
a ───┐
     ▼
  {dictionary}
     ▲
b ───┘
```

To actually get an independent dictionary, use `.copy()`:

```python
a = {"x": 1}
b = a.copy()

b["x"] = 99
a["x"]     # still 1 — a and b are now separate dictionaries
```

(`.copy()` is a **shallow** copy — nested dicts/lists inside are still shared. More on that in [03-nested-dictionaries-and-worked-example.md](03-nested-dictionaries-and-worked-example.md).)

---

## 4. Views: `.keys()`, `.values()`, `.items()`

These return **view objects**, not plain lists — they stay live if the dictionary changes, and you'd wrap them in `list(...)` if you specifically need a list:

```python
person = {"name": "Bhavana", "age": 22}

person.keys()      # dict_keys(['name', 'age'])
person.values()      # dict_values(['Bhavana', 22])
person.items()         # dict_items([('name', 'Bhavana'), ('age', 22)])

list(person.keys())      # ['name', 'age'] — an actual list, if you need one
```

### Iteration patterns — memorize these three

```python
for key in person:                     # iterating a dict directly gives its KEYS
    ...

for value in person.values():
    ...

for key, value in person.items():        # the one you'll use constantly
    ...
```

---

## 5. Dictionary Comprehension

```python
squares = {x: x ** 2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

evens_squared = {x: x ** 2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

General shape: `{key_expr: value_expr for item in iterable if condition}`.

---

## 6. Building Dictionaries from Other Data

```python
keys = ["name", "age", "country"]
values = ["Bhavana", 22, "India"]

dict(zip(keys, values))
# {'name': 'Bhavana', 'age': 22, 'country': 'India'}
```

```python
dict.fromkeys(["name", "age", "country"])          # {'name': None, 'age': None, 'country': None}
dict.fromkeys(["name", "age", "country"], 0)          # {'name': 0, 'age': 0, 'country': 0}
```

---

## 7. `setdefault()` vs. `get()` — Easy to Confuse

Both return a fallback if the key is missing. **Only `setdefault()` actually inserts it.**

```python
person = {"name": "Bhavana"}

person.get("age", 22)         # returns 22, but "age" is still NOT in person
"age" in person                  # False

person.setdefault("age", 22)       # returns 22, AND inserts "age": 22
"age" in person                      # True

person.setdefault("name", "Anu")       # "name" already exists → returns "Bhavana" unchanged
```

> `get()` peeks. `setdefault()` peeks *and* fills in the gap if there was one.

---

## 8. Equality vs. Order

```python
a = {"name": "Bhavana", "age": 22}
b = {"age": 22, "name": "Bhavana"}
a == b     # True — dictionary equality compares key-value mappings, not insertion order
```

Modern Python dictionaries **do** preserve insertion order for iteration — but that's a separate fact from equality, and it's not the same thing as being sorted:

```python
d = {"z": 1, "a": 2}
list(d)        # ['z', 'a'] — insertion order, NOT alphabetical

sorted(d)         # ['a', 'z'] — sorted() gives you a sorted list of keys; it doesn't reorder the dict itself
```

Sorting by value, when you need it:

```python
scores = {"A": 80, "B": 95, "C": 70}
sorted(scores.items(), key=lambda item: item[1])              # ascending by score
sorted(scores.items(), key=lambda item: item[1], reverse=True)  # descending
```

## References

- [Python Tutorial — Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python Standard Library — Mapping Types (`dict`)](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) (all methods in this file: `update`, `pop`, `popitem`, `setdefault`, `fromkeys`, view objects)
