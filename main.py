from typing import List, Dict, Tuple

def demonstrate_list_comprehension(data: List[str]) -> None:
    """
    Demonstrates converting traditional list loops into list comprehensions.
    
    Args:
        data: A list of strings to process.
    """
    print("\n" + "="*60)
    print("✅ 1. LIST COMPREHENSIONS (Filtering and Mapping)")
    print("="*60)
    
    # --- Example 1: Filtering ---
    print("\n[Demo 1: Filtering Elements (Length > 5)]")
    
    # Traditional Loop Approach (The 'Long Way')
    print("  -> Traditional Loop:")
    filtered_loop: List[str] = []
    for item in data:
        if len(item) > 5:
            filtered_loop.append(item)
    print(f"     Result (Loop): {filtered_loop}")

    # Comprehension Approach (The 'Pythonic Way')
    print("\n  -> List Comprehension:")
    # Syntax: [expression for item in iterable if condition]
    filtered_comp: List[str] = [item for item in data if len(item) > 5]
    print(f"     Result (Comp): {filtered_comp}")
    print("     *Observation: Much shorter, same result!*")

    # --- Example 2: Mapping/Transformation ---
    print("\n[Demo 2: Mapping (Converting to Uppercase)]")
    
    # Traditional Loop Approach
    print("  -> Traditional Loop:")
    upper_loop: List[str] = []
    for item in data:
        upper_loop.append(item.upper())
    print(f"     Result (Loop): {upper_loop}")

    # Comprehension Approach
    print("\n  -> List Comprehension:")
    # Syntax: [expression for item in iterable]
    upper_comp: List[str] = [item.upper() for item in data]
    print(f"     Result (Comp): {upper_comp}")
    print("     *Observation: Perfect for simple transformations.*")


def demonstrate_dict_comprehension(data: List[Tuple[str, int]]) -> None:
    """
    Demonstrates converting traditional dictionary population loops 
    into a concise dictionary comprehension.
    
    Args:
        data: A list of (key, value) tuples.
    """
    print("\n" + "="*60)
    print("⚙️ 2. DICTIONARY COMPREHENSIONS (Creating Key-Value Maps)")
    print("="*60)
    
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


def main() -> None:
    """
    Main function to generate the demonstration.
    """
    print("#################################################################")
    print("# PYTHONIC CODE DEMO: LOOPS VS. COMPREHENSIONS (CIS 186) #")
    print("#################################################################")
    
    # Sample Data for List Comprehension
    word_list: List[str] = ["apple", "banana", "kiwi", "grapefruit", "fig", "mango"]
    
    # Sample Data for Dictionary Comprehension (Student, Score)
    score_data: List[Tuple[str, int]] = [
        ("Alice", 95), 
        ("Bob", 88), 
        ("Charlie", 92)
    ]

    # Run Demonstrations
    demonstrate_list_comprehension(word_list)
    demonstrate_dict_comprehension(score_data)
    
    print("\n" + "="*60)
    print("✨ CONCLUSION: Comprehensions are generally faster, cleaner, and more readable.")
    print("="*60)


if __name__ == "__main__":
    main()
