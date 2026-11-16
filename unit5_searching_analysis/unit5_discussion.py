"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Check ticket IDs in order. A missing ID requires checking all n
    # entries, so the worst-case time complexity is O(n).
    for index, ticket_id in enumerate(lst):
        if ticket_id == target:
            return index

    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    left = 0
    right = len(lst) - 1

    while left <= right:
        middle = (left + right) // 2
        ticket_id = lst[middle]

        if ticket_id == target:
            return middle

        # The IDs are sorted, so the midpoint comparison lets us
        # discard the midpoint and one side of the remaining range.
        if ticket_id < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    small_export = [17748, 17773, 17829]
    print(f"Ticket IDs in the sorted export: {small_export}")

    # Both searches find 17829 at index 2 and return -1 for the missing ID.
    for target in (17829, 17801):
        linear_index = linear_search(small_export, target)
        binary_index = binary_search(small_export, target)

        print(f"\nSearching for ticket ID {target}")
        print(f"Linear search returned {linear_index}")
        print(f"Binary search returned {binary_index}")

    print("\nLinear search checks IDs in order.")
    print("Binary search starts at 17773 and checks to its right for both IDs.")
    print("A return value of -1 means the ticket ID was not found.")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    large_export = list(range(18000, 28000))
    target = large_export[-1]

    # Linear search checks every entry to reach the last ID.
    # Binary search keeps the upper half after each midpoint below the target.
    linear_index = linear_search(large_export, target)
    binary_index = binary_search(large_export, target)

    print(f"Searching for ticket ID {target} in {len(large_export):,} sorted IDs")
    print(f"Linear search returned index {linear_index}")
    print(f"Binary search returned index {binary_index}")
    print("For this target, linear search checks 10,000 IDs.")
    print("Binary search checks 14 IDs by narrowing the range at each step.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    edge_cases = [
        ("Empty export", [], 17773),
        ("One ID, target present", [17773], 17773),
        ("One ID, target missing", [17773], 17748),
    ]

    for description, export, target in edge_cases:
        print(f"\n{description} (searching for {target} in {export})")
        print(f"Linear search returned {linear_search(export, target)}")
        print(f"Binary search returned {binary_search(export, target)}")

    print("\nAn empty export has no IDs to check.")
    print("In a one-item export, the only possible match is at index 0.")
    print("Both searches return -1 if the only ID differs from the target.")


if __name__ == "__main__":
    main()