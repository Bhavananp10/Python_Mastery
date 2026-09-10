# Module 6 — Dictionaries: Basics & Access

> Stage: 06-dictionaries · Status: In progress · Last updated: 2026-09-09
> Notes compiled by: BHAVANA

## Summary

A dictionary (`dict`) stores data as **key → value** pairs, accessed by key rather than by numeric position. It's the single most-used data structure once you touch JSON, APIs, configs, or any structured data. (Lists, tuples & sets are covered later, per plan.)

```text
DICTIONARY
    │
key ──→ value
```

Runnable practice: [practice_dict_basics.py](practice_dict_basics.py)

---

## 1. Creating a Dictionary

```python
person = {
    "name": "Bhavana",
    "age": 22,
    "is_student": True,
}

empty = {}          # or: dict()
```

```python
type(person)   # <class 'dict'>
```

Unlike a list, you don't access items by numeric position:

```python
person[0]     # KeyError — dictionaries are accessed by KEY, not index
```

---

## 2. Keys Must Be Hashable

Immutable types (`str`, `int`, `float`, `bool`, `tuple`) can be keys. Mutable types (`list`, `dict`, `set`) cannot:

```python
{"name": "Bhavana", 1: "one", 3.14: "pi", (1, 2): "tuple"}   # all fine

{[1, 2]: "hello"}     # TypeError: unhashable type: 'list'
```

Rule of thumb: **if it can change in place, it can't be a key.**

---

## 3. Accessing Values — `[]` vs. `get()`

```python
person = {"name": "Bhavana"}

person["name"]      # "Bhavana"
person["age"]         # KeyError — "age" doesn't exist

person.get("name")      # "Bhavana"
person.get("age")         # None — no error
person.get("age", 0)        # 0    — an explicit fallback instead of None
```

```text
d["key"]        → KeyError if missing
d.get("key")      → None if missing
d.get("key", x)     → x if missing
```

**Use `get()` whenever a key might legitimately be absent** — this is the normal case with API/JSON data, where fields aren't guaranteed to exist.

---

## 4. Dictionary Length

```python
person = {"name": "Bhavana", "age": 22, "country": "India"}
len(person)    # 3 — counts key-value PAIRS, not characters or nested elements
```

---

## 5. Adding & Updating Items

Same syntax does both — Python decides based on whether the key already exists:

```python
person = {"name": "Bhavana", "age": 22}

person["country"] = "India"   # key didn't exist → added
person["age"] = 23              # key existed → updated, not duplicated
```

---

## 6. Keys Are Unique — Later Values Win

```python
person = {"name": "Bhavana", "name": "Anu"}
person   # {'name': 'Anu'} — the second value silently overwrites the first
```

---

## 7. Checking Whether a Key Exists

```python
person = {"name": "Bhavana", "age": 22}

"name" in person       # True
"salary" in person        # False
"salary" not in person      # True
```

### Trap: `in` checks **keys**, not values

```python
"Bhavana" in person            # False — "Bhavana" is a VALUE here, not a key
"Bhavana" in person.values()     # True — check values explicitly when that's what you mean
```

## References

- [Python Tutorial — Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python Standard Library — Mapping Types (`dict`)](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
