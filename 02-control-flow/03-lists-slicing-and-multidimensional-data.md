# Module 2 (cont.) — Lists, Slicing & Multidimensional Data

> Stage: 02-control-flow · Status: In progress · Last updated: 2026-09-09
> Notes compiled by: BHAVANA

## Summary

Where loops meet data: lists, indexing, slicing, and nested lists as a stand-in for matrices — the last stop before NumPy/PyTorch tensors.

```text
LIST → index / slice / iterate → nested lists → multidimensional data → (later) tensors
```

Runnable practice for everything here: [practice_lists.py](practice_lists.py).

---

## 1. Lists — Ordered & Mutable

```python
numbers = [10, 20, 30, 40]
```

```text
index:    0    1    2    3
value:   10   20   30   40
```

### Indexing — zero-based, and negative from the end

```python
numbers[0]    # 10
numbers[-1]   # 40   — last item
numbers[-2]   # 30   — second-to-last
```

### Mutation — unlike strings, list elements can be changed in place

```python
numbers[1] = 99
# [10, 99, 30]

numbers.append(40)
# [10, 99, 30, 40]
```

Other key methods to know exist (covered properly in [03-data-structures](../03-data-structures/)): `extend()`, `insert()`, `remove()`, `pop()`, `clear()`, `sort()`, `reverse()`.

### Iterating — direct, or with the index via `enumerate()`

```python
for number in numbers:
    print(number)

for i, value in enumerate(numbers):
    print(i, value)
```

---

## 2. Slicing

```python
list[start:stop:step]     # start included, stop excluded, step defaults to 1
```

```python
numbers = [10, 20, 30, 40, 50]
numbers[1:4]      # [20, 30, 40]     — index 4 is the boundary, not included
numbers[0:5:2]     # [10, 30, 50]     — every second item
```

### Patterns worth memorizing

```python
x = [0, 1, 2, 3, 4, 5]
x[:3]      # [0, 1, 2]         first 3
x[3:]       # [3, 4, 5]         from index 3 onward
x[:]         # shallow copy of the whole list
x[::-1]       # [5, 4, 3, 2, 1, 0]   reversed
```

### Why this matters beyond toy examples

Slicing shows up constantly in real AI/ML code:

```python
tokens[:context_window]     # truncate to a model's context window
documents[:top_k]            # keep only the top-k retrieved documents
batch[start:end]              # a mini-batch out of a larger dataset
conversation[-5:]              # last five messages in a chat history
```

---

## 3. Nested Lists as Matrices

Python's `list` has no dedicated matrix type — a matrix is just a list of lists:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
```

```text
        col: 0  1  2
row 0 →     1  2  3
row 1 →     4  5  6
row 2 →     7  8  9
```

Access with `matrix[row][column]`:

```python
matrix[0][0]   # 1
matrix[1][2]   # 6
```

Traverse with nested loops:

```python
for row in matrix:
    for value in row:
        print(value)
```

### Real-world pattern: grid auditing

```python
warehouse_grid = [
    [15, 22, 0, 8],     # Aisle 0
    [40, 99, 12, 5],     # Aisle 1
    [0, 11, 88, 14],      # Aisle 2
]

for aisle_id, bins in enumerate(warehouse_grid[:2]):     # audit only aisles 0 and 1
    print(f"Auditing aisle {aisle_id}...")
    for bin_id, stock in enumerate(bins):
        if stock == 0:
            print(f"  bin {bin_id}: empty — skipping")
            continue
        if stock > 90:
            print(f"  bin {bin_id}: overcapacity ({stock}) — halting audit")
            break
        print(f"  bin {bin_id}: nominal ({stock} units)")
```

This is the same three loop-control ideas from [02-conditionals-and-loops.md](02-conditionals-and-loops.md) — `if`, `continue`, `break` — just operating over a 2D structure instead of a flat list.

---

## 4. A Preview of 3D Data and Tensors

Nesting one level deeper gives 3D data:

```python
data = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
]
data[0][1][1]   # 4 — read as depth → row → column
```

This is exactly the mental model behind tensors in NumPy/PyTorch, just before the specialized library takes over:

```text
1D: [1, 2, 3]
2D: [[1, 2], [3, 4]]
3D: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
```

You'll later see shapes like `(32, 512, 768)` — `batch size, sequence length, embedding dimension`. Understanding nested-list indexing now makes that far less mysterious later.

**Don't confuse a Python list-of-lists with a NumPy array** — `np.array([[1, 2], [3, 4]])` is a specialized numerical structure with vectorized operations; a nested Python list is just plain objects. More on this when NumPy is introduced in [15-popular-libraries](../15-popular-libraries/).

---

## Practice

Solve these yourself first — no solutions are provided in [practice_lists.py](practice_lists.py):

- [ ] Matrix traversal — print `[[1,2,3],[4,5,6],[7,8,9]]` row by row with nested loops, then compute its sum (`45`) without using `sum()`.
- [ ] Matrix maximum — find the largest value in `[[12,4,8],[23,7,19],[5,31,2]]` (`31`) without using `max()`.

## References

- [Python Tutorial — Data Structures](https://docs.python.org/3/tutorial/datastructures.html) (list methods, list comprehensions, nesting)
- [Python Tutorial — More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (`range`, `enumerate` show up here too)
