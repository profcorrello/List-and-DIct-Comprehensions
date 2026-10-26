from typing import Dict, List, Tuple


def demonstrate_dict_comprehension(data: List[Tuple[str, int]]) -> None:
    """
    Demonstrates converting traditional dictionary population loops
    into a concise dictionary comprehension.

    Args:
        data: A list of (key, value) tuples.
    """
    print("\n" + "=" * 60)
    print("⚙️ 2. DICTIONARY COMPREHENSIONS (Creating Key-Value Maps)")
    print("=" * 60)

    # --- Traditional Loop Approach ---
    print("\n[Demo: Building a Dictionary]")
    student_scores: Dict[str, int] = {}

    # The 'Long Way': Initialize, then loop and assign
    for student, score in data:
        student_scores[student] = score

    print(f"  -> Traditional Loop Result: {student_scores}")

    # --- Comprehension Approach ---
    print("\n  -> Dictionary Comprehension (The 'Pythonic Way'):")
    # Syntax: {key_expression: value_expression for item in iterable}
    # Here, key is 'student' and value is 'score'
    student_scores_comp: Dict[str, int] = {student: score for student, score in data}

    print(f"  -> Comprehension Result: {student_scores_comp}")
    print("     *Observation: Concisely creates the map in one line.*")
