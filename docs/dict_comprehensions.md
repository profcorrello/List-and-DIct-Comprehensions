# Module: `dict_comprehensions.py`

## Purpose

Shows how to build a dictionary from an iterable of key-value pairs in a single line using a dictionary comprehension, replacing the initialize-then-assign loop pattern.

## Public API

### `demonstrate_dict_comprehension(data: List[Tuple[str, int]]) -> None`

Prints a formatted comparison of the traditional loop and the dictionary comprehension.

| Argument | Type | Description |
| --- | --- | --- |
| `data` | `List[Tuple[str, int]]` | `(key, value)` tuples to place into the dictionary. |

Returns `None`; results are printed.

## Concepts Shown

```python
# Traditional loop: initialize, then assign each pair
student_scores: Dict[str, int] = {}
for student, score in data:
    student_scores[student] = score

# Dictionary comprehension: one expression, one line
student_scores = {student: score for student, score in data}
```

Syntax: `{key_expression: value_expression for item in iterable}`

Because each element of `data` is a 2-tuple, it unpacks directly into `student, score` in the `for` clause.

## Example

```python
from dict_comprehensions import demonstrate_dict_comprehension
from sample_data import SCORE_DATA

demonstrate_dict_comprehension(SCORE_DATA)
# {'Alice': 95, 'Bob': 88, 'Charlie': 92}
```

## Design Notes

- Conditions work the same way as in list comprehensions:
  `{student: score for student, score in data if score >= 90}`
- Duplicate keys keep the last value, just like with loop assignment.
