"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Insert before the specified index. Existing elements at that position
    # and later positions shift one index to the right.
    # Beginning and middle insertions take O(n) time because of shifting.
    # End insertion takes O(1) amortized time, although resizing can take O(n).
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Accept only nonnegative indices within the list's current bounds.
    # This also rejects every index when the list is empty.
    if 0 <= index < len(lst):
        # pop() removes and returns the item. Later elements shift left.
        return lst.pop(index)

    # Leave the list unchanged and avoid an IndexError for invalid indices.
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Check each item sequentially because the list is ordered by planned
    # work sequence, which does not tell us where a particular value is.
    for index, item in enumerate(lst):
        if item == value:
            # Stop at the first match and return its position.
            return index

    # No match was found. An empty list also reaches this return directly.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # Store ticket IDs in the engineer's planned work order.
    tickets = ["INC1001", "INC1002", "INC1003"]
    print(f"Original worklist: {tickets}")

    # Place an urgent ticket first, shifting all existing entries right.
    insert_at(tickets, 0, "INC1004")
    print(f"Inserted urgent ticket INC1004 at index 0: {tickets}")

    # Place a follow-up ticket in the middle of the current worklist.
    middle_index = len(tickets) // 2
    insert_at(tickets, middle_index, "INC1005")
    print(f"Inserted follow-up ticket INC1005 at index {middle_index}: "
          f"{tickets}")

    # Place a newly assigned ticket at the end without shifting entries.
    end_index = len(tickets)
    insert_at(tickets, end_index, "INC1006")
    print(f"Inserted new ticket INC1006 at index {end_index}: {tickets}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Remove the first ticket after its work has been completed.
    removed = delete_at(tickets, 0)
    print(f"Removed first ticket at index 0: {removed}")
    print(f"Updated worklist: {tickets}")

    # Remove a ticket from the middle after transferring responsibility.
    middle_index = len(tickets) // 2
    removed = delete_at(tickets, middle_index)
    print(f"Removed middle ticket at index {middle_index}: {removed}")
    print(f"Updated worklist: {tickets}")

    # Remove the last ticket after it no longer requires attention.
    end_index = len(tickets) - 1
    removed = delete_at(tickets, end_index)
    print(f"Removed last ticket at index {end_index}: {removed}")
    print(f"Updated worklist: {tickets}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print(f"Current worklist: {tickets}")

    # Locate a ticket that remains in the worklist.
    target = "INC1005"
    found_index = search_value(tickets, target)
    print(f"Search for existing ticket {target}: index {found_index}")

    # Search for a ticket that is absent. The function returns -1.
    target = "INC9999"
    found_index = search_value(tickets, target)
    print(f"Search for missing ticket {target}: index {found_index} "
          "(not found)")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Reject an index just beyond the last item and a negative index.
    # Neither attempt should change the worklist.
    print(f"Worklist before invalid deletions: {tickets}")
    for invalid_index in [len(tickets), -1]:
        removed = delete_at(tickets, invalid_index)
        print(f"Delete at invalid index {invalid_index}: {removed}")
        print(f"Worklist after attempt: {tickets}")

    # Deleting from an empty list should return None without an error.
    empty_tickets = []
    removed = delete_at(empty_tickets, 0)
    print(f"Delete from empty worklist: {removed}")
    print(f"Worklist after attempt: {empty_tickets}")

    # Searching an empty list should return -1 without entering the loop.
    found_index = search_value(empty_tickets, "INC1001")
    print(f"Search empty worklist for INC1001: {found_index} (not found)")

    # Inserting at index 0 should work even when the list is empty.
    insert_at(empty_tickets, 0, "INC1007")
    print(f"Inserted INC1007 into empty worklist: {empty_tickets}")

    # Removing the only ticket should leave an empty list again.
    removed = delete_at(empty_tickets, 0)
    print(f"Removed only ticket: {removed}")
    print(f"Worklist after single-item deletion: {empty_tickets}")

    # Use separate sample data to verify that duplicate values return
    # the first matching index. These functions do not enforce uniqueness.
    duplicate_tickets = ["INC1001", "INC1002", "INC1001"]
    found_index = search_value(duplicate_tickets, "INC1001")
    print(f"Duplicate-value sample: {duplicate_tickets}")
    print(f"Search for INC1001 returned first matching index: {found_index}")


if __name__ == "__main__":
    main()