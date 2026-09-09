# Module 0 — How Computers, Programs, Languages & Python Actually Work

> Stage: 00-getting-started · Status: In progress · Last updated: 2026-09-09
> Notes compiled by: BHAVANA

## Summary

Before writing Python syntax, this note builds the mental model underneath it: what a computer does, what a programming language is, how source code becomes execution, and where Python (and specifically CPython) sits in that stack. Goal: be able to explain, from memory, what happens between typing `python app.py` and the CPU doing work — not just "Python is interpreted."

```text
Computer → Machine Code → Programming Languages → Python → Your Program
```

---

## 1. What a Computer Actually Does

A computer stores data and executes instructions that manipulate that data, using three main hardware components:

| Component | Role |
|---|---|
| **CPU** (Central Processing Unit) | The "brain" — performs calculations, logical decisions, executes commands |
| **RAM** (Random Access Memory) | Fast, temporary workspace for data/programs currently in use |
| **Storage** (SSD/HDD) | Permanent space for files, OS, and programs when powered off |

```text
             COMPUTER
                 │
       ┌─────────┴─────────┐
       │                   │
     CPU                 Memory
       │                   │
   executes             stores
   instructions         data/code
       │
       ▼
     Output
```

The CPU works with very simple instructions (`LOAD`, `ADD`, `STORE`, `COMPARE`, `JUMP`, ...), defined by an instruction set (x86-64, ARM64, etc.). The **fetch–decode–execute cycle** is the CPU pulling an instruction from memory (fetch), figuring out what it commands (decode), and performing the action (execute) — repeatedly, extremely fast.

Ultimately, everything reduces to **binary code**: electronic signals representing 0s and 1s. Humans write readable **source code** instead of binary directly.

---

## 2. Why Programming Languages Exist: Abstraction

Directly programming the CPU (raw machine instructions) is possible but impractical. Something as simple as:

```python
total = price * quantity
```

becomes, at the CPU level, several explicit steps: load `price`, load `quantity`, multiply registers, store result — and beneath that, binary machine instructions.

Programming languages exist as a layer of **abstraction** so humans don't need to think at that level:

```text
Human intent
     ↓
Python source        ("total = price * quantity")
     ↓
Compiler / Interpreter
     ↓
Lower-level representation
     ↓
Machine instructions
     ↓
CPU / electrical operations
```

Each layer hides the complexity of the layer below it. You don't need to know how a transistor switches to write `x = 10 + 20` — this is one of the most important ideas in computer science.

---

## 3. What Defines a Programming Language

A programming language is a formal system for expressing computation. It's defined by:

- **Syntax** — the strict grammar/spelling rules (where parentheses, colons, etc. go). `x = 10` is valid Python; `10 = x` is not.
- **Semantics** — the *meaning* of valid code. `x = 10` means the name `x` is bound to an integer object representing `10`.
- **Grammar specifications** — formal rules (often in Backus–Naur Form) that language creators use to define what's valid, similar to how English grammar defines `subject + verb + object`.

Python's syntax and core semantics are defined in its official **Language Reference**.

### Language vs. Implementation — an important distinction

**Python** is the language (its syntax, semantics, grammar). **CPython** is an *implementation* of that language, written primarily in C. Python's own documentation explicitly makes this distinction and lists CPython, PyPy, and Jython as implementations of the same language.

```text
                 PYTHON (the language)
                       │
        ┌──────────────┼──────────────┐
        │              │              │
     CPython          PyPy          Jython
    (C/C++,          (Python/C,     (targets the
   the default        with a JIT)    JVM ecosystem)
   implementation)
```

This distinction matters later for interpreters, compilers, bytecode, JIT, performance, and the GIL.

---

## 4. Compilation vs. Interpretation

- **Compilation** — a compiler translates *all* of the source code into native machine code *before* the program runs (e.g. C, C++). Produces an executable; typically runs very fast.
- **Interpretation** — an interpreter translates and executes source code line by line, in real time, as the program runs. More flexible, typically slower.

```text
Compiled:                          Interpreted:
source → compiler → machine code   source → interpreter → executed directly
            → executable → CPU                (at runtime)
```

**The common oversimplification** — "C is compiled, Python is interpreted" — is a useful beginner heuristic but technically incomplete. Python's own glossary says this distinction is blurry because Python has a bytecode compiler.

### Python's actual (hybrid) model

Python first **compiles** source code into an intermediate format called **bytecode**, and then a virtual machine (the Python runtime) **interprets** that bytecode:

```text
Python source
     ↓  (compiled)
Python bytecode
     ↓  (interpreted)
CPython runtime / interpreter
     ↓
Machine operations → CPU
```

You can inspect this bytecode yourself:

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
```

**Why bytecode exists:** it's a portable intermediate representation, decoupling your Python source from the exact CPU architecture — one reason the same `.py` file can run on Windows, Linux, and macOS, given an appropriate Python implementation.

**Correction to a common mental model:** Python does *not* execute strictly "line by line" in the naive sense — there is parsing and compilation into bytecode first. This matters later for understanding syntax errors vs. runtime errors, `.pyc` files, and execution frames.

---

## 5. What Python Is and Where It Sits

Python is a **high-level, general-purpose** programming language created by Guido van Rossum, released in 1991. It prioritizes human readability and clean syntax via whitespace indentation.

**Positioning:** Python trades raw execution speed for speed of *writing* code and developer productivity. It dominates data science, AI/ML, web backend development, and automation/scripting.

### High-level vs. low-level

```text
HIGH LEVEL                     Easier for humans, more abstraction
  Python, Java, JavaScript, C#
  C
  Assembly
  Machine code
LOW LEVEL                      More control over hardware, less abstraction
```

### Python's characteristics

- **General-purpose** — web, automation, AI, ML, scripting, data engineering, APIs, tooling. Not "just a scripting language" — you can build anything from a small script to a distributed backend or ML pipeline.
- **Dynamically typed** — `x = 10`, not `int x = 10;` (deep dive comes later).
- **Garbage-collected** — you generally don't manually free objects.
- **Multi-paradigm** — supports procedural, object-oriented, and functional styles.
- **Compiled-to-bytecode + interpreted**, in its standard (CPython) implementation.

### Why is Python everywhere in AI?

Python itself usually isn't doing the heavy numerical computation — it's the **orchestration layer** on top of code written in C/C++/CUDA:

```text
Python           (you write this: model.generate(...))
   ↓
PyTorch
   ↓
C++ kernels
   ↓
CUDA
   ↓
GPU
```

This is why understanding "what's underneath Python" is directly useful for AI engineering, not just trivia.

---

## 6. Python 2 vs. Python 3, and Versioning

| | Python 2 (2000) | Python 3 (2008) |
|---|---|---|
| Status | End-of-life since **Jan 1, 2020** — no longer supported | The modern global standard |
| Compatibility | Legacy syntax | **Backward-incompatible** with Python 2 — Python 2 code usually needs changes to run on Python 3 |
| Recommendation | **Do not learn this for your career** | **Target this** |

### Reading a version number: `3.14.7`

```text
3   = major version
14  = minor version
7   = maintenance / patch release
```

Newer minor releases (3.10, 3.11, 3.12, 3.13, 3.14, ...) can change: new language syntax, standard library additions, interpreter performance, deprecations, and eventual removals of old APIs. Python publishes a "What's New" document per release covering this.

**Recent progression (context, not to memorize):** 3.11 brought significant interpreter performance improvements; 3.12 continued runtime/language improvements; 3.13 introduced an experimental free-threaded build; 3.14 (released Oct 7, 2025) made free-threaded mode officially supported plus further interpreter/stdlib improvements.

**Practical rule of thumb:** use the latest stable Python unless a project's dependencies require an older version — e.g. a library like PyTorch or another dependency may not yet support the newest release, so a real project might pin to an older minor version deliberately. Professional environments track Python version + package versions + OS + hardware (CPU/GPU/CUDA) + dependencies together.

Don't confuse **version** (`Python 3.14`, the language/runtime release) with **implementation** (`CPython`, `PyPy`, `Jython` — how Python is realized) — e.g. "CPython 3.14" combines both dimensions.

---

## 7. Types of Errors — Distinguish These Early

| Type | What it means | Example |
|---|---|---|
| **Syntax error** | Code violates Python's grammar; can't even be parsed | `if x > 10\n    print(x)` (missing colon) |
| **Runtime error** | Syntactically valid, but something fails while running | `x / 0` → `ZeroDivisionError` |
| **Logical error** | Code runs fine, but the logic/intent is wrong | `final_price = price + discount` (meant to subtract) |

Logical errors are the hardest category — the program runs successfully and produces a *plausible but wrong* result. This is especially relevant in AI/ML work, where silently-wrong output is a common failure mode.

---

## 8. Key Vocabulary

| Term | Meaning |
|---|---|
| Computer | Machine that executes instructions |
| CPU | Executes machine instructions |
| Memory | Stores data/instructions while programs run |
| Program | A set of instructions |
| Source code | Human-readable program text |
| Programming language | Formal system for expressing computation |
| Syntax | Rules for valid structure |
| Semantics | Meaning of valid code |
| Compiler | Transforms source into another representation |
| Interpreter | Runtime that executes a program representation |
| Bytecode | Intermediate instruction representation |
| Runtime | Environment responsible for executing a program |
| Implementation | A concrete realization of a language (e.g. CPython) |
| CPython | The main/reference Python implementation |
| Machine code | CPU-specific instructions |

---

## 9. Mastery Self-Test

Answer these from memory before moving to the next topic.

**Level 1 — foundations**
1. What is a computer program?
2. What does a CPU do?
3. What is source code?
4. What is a programming language?
5. What is syntax? What is semantics?

**Level 2 — execution model**
6. What is compilation? What is interpretation?
7. What is bytecode, and why does it exist?
8. Why isn't "Python is interpreted" a complete explanation?
9. What is CPython, and how does it differ from "Python"?

**Level 3 — applied**
10. What actually happens when you run `python app.py`?
11. Why can the same Python program run on Windows and Linux?
12. Why might a real project deliberately use Python 3.12 instead of the latest 3.14?
13. Why is Python popular in AI despite being slower than C/C++ for many CPU-bound operations?

**Golden question** — explain this pipeline in your own words:

```text
print("Hello")
   → Python source
   → CPython (compiles to bytecode)
   → bytecode
   → runtime / interpreter
   → OS
   → CPU
```

If you can explain that unaided, this module's foundation has landed.

---

---

