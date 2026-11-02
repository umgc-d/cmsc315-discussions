# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Implementation

I used a Python list to represent a support engineer's manually ordered
ticket worklist. Each entry contained a ticket ID, and its position
represented the planned work sequence. The demonstration placed an urgent
ticket first, a follow-up ticket in the middle, and a newly assigned ticket
at the end.

The operation functions remained separate from the demonstration data in
`main()`. They accepted a list and the necessary arguments, allowing the
same functions to work with other list contents. The program demonstrated
manual placement rather than automatic priority calculation. Removing an
entry represented removing a ticket from the worklist, rather than deleting
its record from a ticketing system.

### List Operations

I implemented `insert_at()` with `lst.insert(index, value)`. Insertion
modified the original list and shifted existing entries at and after the
insertion position one index to the right. Inserting at `len(lst)` placed
the new entry at the end without shifting existing entries.

I implemented `delete_at()` with index validation followed by
`lst.pop(index)`. The condition `0 <= index < len(lst)` restricted deletion
to existing, nonnegative positions. Valid deletions returned the removed
ticket ID and shifted later entries one index to the left. Invalid indices,
including negative indices, returned `None` without changing the list. The
same validation handled an empty list without raising an `IndexError`.

I implemented `search_value()` with a loop using `enumerate(lst)`, which
provided each entry and its index. The search compared entries sequentially
because the planned work order did not indicate where a particular ticket
ID would appear. It returned the first matching index or `-1` when no match
was found, leaving the list unchanged.

### Demonstration and Edge Cases

In `main()`, I demonstrated insertion and deletion at the beginning, middle,
and end. I displayed the list after every modification and the removed
value after every deletion. I recalculated the middle and end indices as
the list changed size.

I searched for an existing ticket and a missing ticket. Additional cases
covered deletion at `len(tickets)`, rejection of a negative deletion index,
deletion and search on an empty list, insertion into an empty list, and
removal of its only entry. I also used separate sample data with duplicate
ticket IDs to verify that search returned the first match. The functions
did not enforce ticket ID uniqueness.

### Performance Analysis

I identified beginning and middle insertion and deletion as O(n) operations
because they shifted existing entries. End insertion and deletion required
no shifting and had O(1) amortized cost, although occasional resizing could
take O(n) time.

The linear search had an O(1) best case when the first entry matched and an
O(n) worst case when the match was last or absent. In a larger support
worklist, repeated searches and changes near the beginning could therefore
require more work as the number of tickets increased.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

I needed to understand why the deletion function rejected negative indices
when Python allowed them. An index of `-1` identified the last entry, but
`delete_at()` returned `None` for that index. Tracing the function showed me
that its bounds check rejected the value before `pop()` ran.

I also questioned the use of `None` instead of an exception. Comparing the
two approaches clarified what happened after an unsuccessful deletion.
`None` was a normal return value, so execution continued even if the caller
ignored it. An uncaught `IndexError` interrupted execution. The starter
required `None`, and the calling code could check that value to decide what
to do next.

The worklist showed how the position of a change affected the amount of
work. Placing `"INC1004"` first shifted all three original entries. The end
insertion shifted none. Searching for `"INC9999"` checked every remaining
ticket before returning `-1`. In a larger worklist, the same missing-ticket
search would require more comparisons, and inserting at the front would
shift more entries.