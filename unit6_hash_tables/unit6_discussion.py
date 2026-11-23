"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    # Create an empty dictionary to track active case assignments.
    case_assignments = {}

    # Python dictionaries use a key's hash to determine an initial
    # index in the hash table, allowing for efficient lookup.
    case_assignments[29039] = "Matthew Mann"
    case_assignments[21069] = "Mark Lyon"
    case_assignments[41622] = "Luke Bullock"
    case_assignments[39403] = "John Eagleton"
    case_assignments[40018] = "Paul Swords"

    print("Active case assignments:")
    print(case_assignments)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    # Python hashes each case ID to locate its associated engineer
    # without sequentially searching the dictionary.
    print(f"Case 41622: {case_assignments[41622]}")
    print(f"Case 40018: {case_assignments[40018]}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("Before reassignment:")
    print(case_assignments)

    # Assigning a new value to an existing key replaces its
    # previous value without creating a new dictionary entry.
    case_assignments[29039] = "Mark Lyon"

    print("Case 29039 reassigned from Matthew Mann to Mark Lyon.")

    print("After reassignment:")
    print(case_assignments)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("Before deletion:")
    print(case_assignments)

    # Remove the closed case and its associated engineer assignment.
    del case_assignments[39403]

    print("Closed case 39403 removed from active case assignments.")

    print("After deletion:")
    print(case_assignments)
    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    # Look up a missing case using get() to avoid a KeyError.
    print(f"Case 39403: {case_assignments.get(39403, 'Case not found')}")

    # Check whether a case exists before attempting to delete it.
    if 39403 in case_assignments:
        del case_assignments[39403]
    else:
        print("Cannot delete case 39403 because it does not exist.")

    # Prevent reassignment from inadvertently creating a new entry.
    if 39403 in case_assignments:
        case_assignments[39403] = "Paul Swords"
    else:
        print("Cannot reassign case 39403 because it does not exist.")

    print("Final active case assignments:")
    print(case_assignments)


if __name__ == "__main__":
    main()