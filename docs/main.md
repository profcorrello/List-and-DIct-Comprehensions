# Module: `main.py`

## Purpose

Entry point for the command-line version of the demo. It prints the banner, loads the shared sample data, runs each demonstration module in order, and prints the conclusion.

## Public API

### `main() -> None`

Orchestrates the full demonstration.

```python
from dict_comprehensions import demonstrate_dict_comprehension
from list_comprehensions import demonstrate_list_comprehension
from sample_data import SCORE_DATA, WORD_LIST


def main() -> None:
    print("# PYTHONIC CODE DEMO: LOOPS VS. COMPREHENSIONS (CIS 186) #")

    demonstrate_list_comprehension(WORD_LIST)
    demonstrate_dict_comprehension(SCORE_DATA)

    print("✨ CONCLUSION: Comprehensions are generally faster, cleaner, and more readable.")
```

Calling `main()` is guarded by the standard idiom:

```python
if __name__ == "__main__":
    main()
```

so the module can be imported without side effects.

## Run It

```bash
python main.py
```

## Module Map

| Module | Responsibility |
| --- | --- |
| `sample_data.py` | Shared input data |
| `list_comprehensions.py` | Filtering and mapping demos |
| `dict_comprehensions.py` | Dictionary-building demo |
| `main.py` | Banner, ordering, conclusion |
