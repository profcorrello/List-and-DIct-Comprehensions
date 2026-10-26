# Module: `sample_data.py`

## Purpose

Holds the shared sample data used by every demonstration in this lesson. Keeping the data in one place means the demos stay focused on *how* comprehensions work instead of re-declaring inputs.

## Public API

| Name | Type | Description |
| --- | --- | --- |
| `WORD_LIST` | `List[str]` | Six fruit names of varying length; used to demonstrate filtering and mapping. |
| `SCORE_DATA` | `List[Tuple[str, int]]` | `(student, score)` tuples used to build a dictionary. |

## Example

```python
from sample_data import WORD_LIST, SCORE_DATA

print(WORD_LIST)   # ['apple', 'banana', 'kiwi', 'grapefruit', 'fig', 'mango']
print(SCORE_DATA)  # [('Alice', 95), ('Bob', 88), ('Charlie', 92)]
```

## Design Notes

- `WORD_LIST` deliberately mixes short words (`fig`, `kiwi`) with longer ones so the `len(item) > 5` filter produces a meaningful subset.
- `SCORE_DATA` is a list of 2-tuples so it can be unpacked directly inside a comprehension: `for student, score in data`.
