from typing import List


def demonstrate_list_comprehension(data: List[str]) -> None:
    """
    Demonstrates converting traditional list loops into list comprehensions.

    Args:
        data: A list of strings to process.
    """
    print("\n" + "=" * 60)
    print("✅ 1. LIST COMPREHENSIONS (Filtering and Mapping)")
    print("=" * 60)

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
