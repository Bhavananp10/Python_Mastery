# Module 6 (cont.) — Nested Dictionaries & a Worked Example

> Stage: 06-dictionaries · Status: In progress · Last updated: 2026-09-09
> Notes compiled by: BHAVANA

## Summary

Dictionaries nest inside lists, lists nest inside dictionaries, dictionaries nest inside dictionaries — this is exactly the shape of real JSON/API data. This file works through a realistic `person` record end-to-end, including a classification problem that exposes a subtle but important bug pattern: **`if`/`elif` branch ordering can silently hide a condition that's also true.**

Runnable practice: [practice_dict_nested_and_worked_example.py](practice_dict_nested_and_worked_example.py)

---

## 1. Nested Dictionaries

```python
person = {
    "name": "Bhavana",
    "address": {
        "street": "Space street",
        "zipcode": "02210",
    },
}

person["address"]["street"]     # "Space street"
```

```text
person
 ├── name
 └── address
       ├── street
       └── zipcode
```

## 2. Lists Inside Dictionaries

```python
person["skills"] = ["JavaScript", "React", "Node", "MongoDB", "Python"]

person["skills"][0]                                  # "JavaScript"
person["skills"][len(person["skills"]) // 2]           # index 5 // 2 == 2 → "Node"
```

## 3. Dictionaries Inside Lists Inside Dictionaries

The shape you'll see constantly in real APIs:

```python
data = {
    "users": [
        {"name": "Bhavana", "age": 22},
        {"name": "Anu", "age": 24},
    ]
}

data["users"][0]["name"]     # "Bhavana"
```

## 4. `.copy()` Is Shallow — Nested Data Is Still Shared

```python
person = {"name": "Bhavana", "skills": ["Python"]}
copy = person.copy()

copy["skills"].append("SQL")     # mutates the LIST in place
person["skills"]                   # ['Python', 'SQL'] — the original sees it too!
```

`.copy()` only duplicates the *top-level* dictionary — nested lists/dicts inside it are still the same shared objects. A true deep copy needs `copy.deepcopy()` (covered later, when we get to modules/packages).

---

## 5. Worked Example: the `person` Record

```python
person = {
    "first_name": "Bhavana",
    "last_name": "Buddha",
    "age": 22,
    "country": "Finland",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {
        "street": "Space street",
        "zipcode": "02210",
    },
}
```

```text
person
 ├── first_name → str
 ├── last_name  → str
 ├── age        → int
 ├── country    → str
 ├── is_married → bool
 ├── skills     → list[str]
 └── address    → dict
                    ├── street  → str
                    └── zipcode → str
```

### a) Does `skills` exist, and what's the middle one?

```python
if "skills" in person:
    skills = person["skills"]
    middle_index = len(skills) // 2      # 5 // 2 == 2
    print("Middle skill:", skills[middle_index])   # "Node"
```

### b) Does the person know Python?

```python
"Python" in person.get("skills", [])
```

Prefer `person.get("skills", [])` over `person["skills"]` here: if `"skills"` were missing, `.get(..., [])` degrades to checking membership in an empty list (`False`) instead of raising `KeyError`.

### c) Classify as frontend / backend / fullstack — the branch-ordering trap

Naive attempt, checking each profile with plain membership:

```python
skills = person.get("skills", [])

if "JavaScript" in skills and "React" in skills and len(skills) == 2:
    result = "frontend"
elif "Node" in skills and "Python" in skills and "MongoDB" in skills:
    result = "backend"
elif "React" in skills and "Node" in skills and "MongoDB" in skills:
    result = "fullstack"
else:
    result = "unknown"
```

For this person's skills (`JavaScript, React, Node, MongoDB, Python`), **both** the backend condition and the fullstack condition are actually true. Because `elif` stops at the first match, whichever check comes first wins — here, `backend` — even though `fullstack` is arguably the better description.

**This is a general principle, not just a dictionary quirk:** if condition A can be true whenever a more specific condition B is also true, and A is checked first, B's branch becomes unreachable for those cases. Order your `elif` chain from most specific to least specific.

Fixed — using `set.issubset()` and checking the more specific case first:

```python
skills = set(person.get("skills", []))

if {"React", "Node", "MongoDB"}.issubset(skills):
    result = "fullstack developer"
elif {"Node", "Python", "MongoDB"}.issubset(skills):
    result = "backend developer"
elif skills == {"JavaScript", "React"}:
    result = "frontend developer"
else:
    result = "unknown title"
```

`required.issubset(skills)` reads as "are all of `required`'s items present in `skills`?" — cleaner than chaining `and`s, and it doesn't care about extra skills the person also has. For this person: `fullstack developer`.

### d) Married and living in Finland?

```python
if person["is_married"] and person["country"] == "Finland":
    full_name = person["first_name"] + " " + person["last_name"]
    print(f"{full_name} lives in {person['country']}. They are married.")
```

Output: `Bhavana Buddha lives in Finland. They are married.`

## References

- [Python Tutorial — Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python Standard Library — `frozenset`/`set.issubset`](https://docs.python.org/3/library/stdtypes.html#frozenset.issubset)
