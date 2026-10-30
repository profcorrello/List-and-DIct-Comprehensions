# Assignment: Mastering Python List Comprehensions

## Objective
This assignment is designed to solidify your understanding and proficiency with Python's list comprehensions. List comprehensions provide a concise and efficient way to create lists, often replacing multiple lines of traditional `for` loops. You will progress through three parts, moving from simple element transformation to advanced filtering and functional integration.

## Prerequisites
*   Python 3.12+ environment.
*   Basic understanding of lists, tuples, and conditional logic (`if`/`else`).

## Instructions
Complete the functions provided in the `student_analyzer.py` file by replacing the placeholder logic with the appropriate list comprehension structure. Remember to utilize modern Python syntax and type hinting for clarity.

### Part 1: Basic Transformation (Mapping)
Given a list of integer scores, create a new list where every score is squared. This demonstrates basic mapping.

### Part 2: Filtering and Transformation (Filtering + Mapping)
Given a list of student records (tuples of `(name: str, score: int)`), create a list of names for students who passed (score >= 70). This requires both filtering (`if` clause) and selecting a specific element.

### Part 3: Advanced Function Integration (Functional Comprehension)
We define a helper function, `calculate_bonus_points`, which applies a complex rule (e.g., 1 point for every 10 points above 80). Use this function *inside* a list comprehension to process the raw scores list from Part 1, demonstrating how to integrate external logic into the compact comprehension structure.

***

## Code Sample

```python
from typing import List, Tuple

# --- Helper Function ---
def calculate_bonus_points(score: int) -> int:
    """
    Calculates bonus points for a score.
    Rule: If the score is above 80, earn 1 bonus point for every 10 points over 80.
    Otherwise, the bonus is 0.
    """
    if score > 80:
        bonus = (score - 80) // 10
        return bonus
    return 0

# --- Data Structures ---

# List of raw scores (integers)
raw_scores: List[int] = [65, 88, 92, 78, 55, 99, 70]

# List of student records: (name, score)
student_records: List[Tuple[str, int]] = [
    ("Alice", 88),
    ("Bob", 65),
    ("Charlie", 92),
    ("Diana", 78),
    ("Evan", 55),
    ("Fiona", 99),
    ("George", 70)
]

def analyze_scores() -> None:
    """
    Performs various data manipulations using list comprehensions.
    """
    print("--- Running List Comprehension Assignment ---")

    # ========================================================
    # PART 1: Basic Transformation (Mapping)
    # Goal: Create a list of the square of every raw score.
    # Expected: [65*65, 88*88, 92*92, ...]
    # ========================================================
    # TODO: Implement the list comprehension here.
    squared_scores: List[int] = [
        # Student must implement the comprehension here
        score * score for score in raw_scores
    ]
    print(f"\n[Part 1: Squared Scores] Original Scores: {raw_scores}")
    print(f"Result (Squared): {squared_scores}")


    # ========================================================
    # PART 2: Filtering and Transformation (Filtering + Mapping)
    # Goal: Create a list of names for students who passed (score >= 70).
    # Use tuple unpacking or indexing to extract the name.
    # ========================================================
    # TODO: Implement the list comprehension here.
    passing_students: List[str] = [
        # Student must implement the comprehension here
        name for name, score in student_records if score >= 70
    ]
    print(f"\n[Part 2: Passing Students] Records: {student_records}")
    print(f"Result (Names of those >= 70): {passing_students}")


    # ========================================================
    # PART 3: Advanced Function Integration (Functional Comprehension)
    # Goal: Calculate the bonus points for every score using the helper function.
    # This demonstrates calling a function within a comprehension.
    # ========================================================
    # TODO: Implement the list comprehension here.
    bonus_points_list: List[int] = [
        # Student must implement the comprehension here
        calculate_bonus_points(score) for score in raw_scores
    ]
    print(f"\n[Part 3: Bonus Points] Raw Scores: {raw_scores}")
    print(f"Result (Bonus Points): {bonus_points_list}")


if __name__ == "__main__":
    analyze_scores()
```