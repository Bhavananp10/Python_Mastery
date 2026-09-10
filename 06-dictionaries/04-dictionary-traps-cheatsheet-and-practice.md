# Module 6 (cont.) — Traps, Cheat Sheet & Practice

> Stage: 06-dictionaries · Status: In progress · Last updated: 2026-09-09
> Notes compiled by: BHAVANA

## Summary

The consolidated "don't get bitten by this" list, a dict-vs-other-collections comparison, a one-page method cheat sheet, and the Day 8 exercises to solve yourself.

Runnable practice: [practice_dict_traps.py](practice_dict_traps.py)

---

## Ten Traps Worth Memorizing

| # | Trap | Fix |
|---|---|---|
| 1 | `d["missing"]` → `KeyError` | `d.get("missing")` → `None`, or `d.get("missing", default)` |
| 2 | `"value" in d` checks **keys**, not values | `"value" in d.values()` |
| 3 | `b = a` does **not** copy — both names share one dict | `b = a.copy()` |
| 4 | Duplicate keys in a literal silently collapse — last one wins | be deliberate; duplicates are usually a typo |
| 5 | `d.pop(key)` really removes the key (unlike `.get()`, which only reads) | expected behavior — just don't confuse the two |
| 6 | `d.get(key, default)` does **not** insert `key` | use `d.setdefault(key, default)` if you want it inserted |
| 7 | `d.keys()`/`.values()`/`.items()` are **views**, not lists | wrap in `list(...)` if you need an actual list |
| 8 | `for x in d:` gives **keys**, not values | `for v in d.values():` / `for k, v in d.items():` |
| 9 | Dictionaries preserve **insertion order**, but are not automatically **sorted** | `sorted(d)` for sorted keys, `sorted(d.items(), key=...)` for sorted pairs |
| 10 | A `list` (or `dict`/`set`) can't be a dictionary key | only hashable (usually immutable) types can be keys |

---

## Dictionary vs. List vs. Set vs. Tuple

| Structure | Main idea | Example | Accessed by |
|---|---|---|---|
| List | Ordered collection | `[10, 20, 30]` | index |
| Tuple | Ordered, immutable collection | `(10, 20, 30)` | index |
| Set | Unique, unordered collection | `{10, 20, 30}` | membership |
| Dictionary | Key → value mapping | `{"age": 22}` | key |

Reach for a **dictionary** specifically when data needs meaningful labels rather than positions — `person["age"]` instead of remembering that age happens to be `person[2]`.

---

## Method Cheat Sheet

| Method / operator | Purpose | Example → result |
|---|---|---|
| `len(d)` | count of key-value pairs | `len({"a":1,"b":2})` → `2` |
| `d[key]` | access (raises if missing) | `d["name"]` → `"Bhavana"` |
| `d.get(key)` / `.get(key, default)` | safe access | `d.get("x", 0)` → `0` |
| `d[key] = value` | add or update | — |
| `d.update(other)` | merge in multiple keys | — |
| `d.pop(key)` / `.pop(key, default)` | remove + return value | `d.pop("age")` → `22` |
| `d.popitem()` | remove + return last-inserted pair | → `("age", 22)` |
| `del d[key]` | remove (raises if missing) | — |
| `d.clear()` | remove everything | → `{}` |
| `d.copy()` | shallow copy | — |
| `d.setdefault(key, default)` | get, inserting if missing | — |
| `dict.fromkeys(keys, value)` | build with a shared default | `dict.fromkeys(["a","b"], 0)` → `{'a':0,'b':0}` |
| `key in d` / `key not in d` | key existence | — |
| `d.keys()` / `.values()` / `.items()` | views | — |
| `sorted(d)` | sorted **keys**, as a list | — |
| `sorted(d.items(), key=lambda kv: kv[1])` | sorted **pairs**, by value | — |
| `d1 == d2` | equality (ignores insertion order) | — |

### Patterns worth memorizing

```python
value = d.get("key")                     # safe access
value = d.get("key", default)              # safe access with fallback
if "key" in d: ...                           # check
for key in d: ...                              # iterate keys
for value in d.values(): ...                     # iterate values
for key, value in d.items(): ...                   # iterate both
d["key"] = value                                     # add / update
d.pop("key")                                           # remove
d["outer"]["inner"]                                      # nested access
{x: x ** 2 for x in range(5)}                              # dict comprehension
```

## The core mental model

```text
                 DICTIONARY
                     │
              key ──→ value
                     │
        ┌────────────┼─────────────┐
        ↓            ↓             ↓
     ACCESS        CHECK         ITERATE
        │            │             │
    d["key"]      "key" in d    d.items()
    d.get()                      d.keys()
                                 d.values()

ADD / UPDATE → d[key] = value
REMOVE       → pop(), del
NEST         → d["a"]["b"]
COPY         → d.copy()   (shallow!)
TRANSFORM    → comprehension
```

This is the foundation you'll reuse constantly in JSON, REST APIs, config objects, and structured model output.

---

## Practice — Day 8 Exercises

Solve these yourself; no solutions are included in [practice_dict_traps.py](practice_dict_traps.py).

- [ ] Create an empty dictionary called `dog`; add `name`, `color`, `breed`, `legs`, `age` to it.
- [ ] Create a `student` dictionary with keys `first_name`, `last_name`, `gender`, `age`, `marital_status`, `skills`, `country`, `city`, `address`.
- [ ] Get the length of the `student` dictionary.
- [ ] Get the value of `skills` and confirm its type is `list`.
- [ ] Modify `skills` by adding one or two more skills.
- [ ] Get the dictionary's keys as a list.
- [ ] Get the dictionary's values as a list.
- [ ] Convert the dictionary to a list of tuples using `.items()`.
- [ ] Delete one of the items in the dictionary.
- [ ] Delete the dictionary itself (`del`).

## References

- [30 Days of Python — Day 8: Dictionaries](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/08_Day_Dictionaries) by Asabeneh Wolde Giorgis — source of the exercise list above
- [Python Standard Library — Mapping Types (`dict`)](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
