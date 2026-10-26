from dict_comprehensions import demonstrate_dict_comprehension
from list_comprehensions import demonstrate_list_comprehension
from sample_data import SCORE_DATA, WORD_LIST


def main() -> None:
    """
    Main function to generate the demonstration.
    """
    print("#################################################################")
    print("# PYTHONIC CODE DEMO: LOOPS VS. COMPREHENSIONS (CIS 186) #")
    print("#################################################################")

    # Run Demonstrations
    demonstrate_list_comprehension(WORD_LIST)
    demonstrate_dict_comprehension(SCORE_DATA)

    print("\n" + "=" * 60)
    print("✨ CONCLUSION: Comprehensions are generally faster, cleaner, and more readable.")
    print("=" * 60)


if __name__ == "__main__":
    main()
