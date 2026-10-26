# Module: `list_comprehensions.py`

## Purpose

Demonstrates the two most common uses of list comprehensions — **filtering** and **mapping** — by showing the traditional `for` loop version side by side with the comprehension version.

## Public API

### `demonstrate_list_comprehension(data: List[str]) -> None`

Prints a formatted comparison of loop vs. comprehension for each demo.

| Argument | Type | Description |
| --- | --- | --- |
| `data` | `List[str]` | Strings to filter and transform. |

Returns `None`; all results are printed.

## Concepts Shown

### 1. Filtering

Select items that satisfy a condition.

```python
# Traditional loop
filtered: List[str] = []
for item in data:
    if len(item) > 5:
        filtered.append(item)

# Comprehension
filtered = [item for item in data if len(item) > 5]
```

Syntax: `[expression for item in iterable if condition]`

### 2. Mapping / Transformation

Apply an expression to every item.

```python
# Traditional loop
upper: List[str] = []
for item in data:
    upper.append(item.upper())

# Comprehension
upper = [item.upper() for item in data]
```

Syntax: `[expression for item in iterable]`

## Example

```python
from list_comprehensions import demonstrate_list_comprehension
from sample_data import WORD_LIST

demonstrate_list_comprehension(WORD_LIST)
```

## Design Notes

- Both the loop and the comprehension are shown for each demo so students can compare line count and readability directly.
- The comprehension versions are intentionally written on a single line — that is the point of the lesson.
- Use a plain `for` loop instead when the body has multiple statements or side effects (logging, printing, I/O).
