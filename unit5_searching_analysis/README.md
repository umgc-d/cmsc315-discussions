# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.

## Implementation

I used fictional ticket IDs to represent a support case export. I ran both
searches on the same sorted lists so I could compare the indexes they returned
and how many IDs they examined. Both functions returned the zero-based index
of a match or `-1` when the target was missing.

I used `enumerate()` in `linear_search()` to check each ticket ID in order
and keep track of its index. A missing ID required checking all `n` entries,
so the worst-case time complexity was `O(n)`.

In `binary_search()`, I used two indexes to mark the remaining search range.
I checked the middle ID and used the sorted order to decide which half to
keep. Each unsuccessful check removed the midpoint and about half of the
remaining entries, giving the search a worst-case time complexity of
`O(log n)`.

In the three-ID export, both searches found `17829` at index `2` and returned
`-1` for `17801`. In the 10,000-ID export, both found `27999` at index `9999`.
To reach that last index, linear search examined all 10,000 IDs, while binary
search examined 14.

I also tested an empty export and a one-ID export. Both searches returned `-1`
for the empty export. In the one-ID export, both returned `0` for a match and
`-1` for a miss.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

Understanding how binary search narrowed the range took the most thought
for me. The Unit 5 zyBooks exercises helped me see how checking the middle
value let me discard about half of the remaining entries. Working through
those examples first made it easier to decide when to move the left or
right index in my code.

I also appreciated how zyBooks connected the number of entries examined to
Big O runtime. Linear search can check all `n` entries, so its worst-case
runtime is `O(n)`. Binary search is `O(log n)` because it roughly halves
the remaining range at each step. For a nonempty sorted list, my binary
search checked at most `floor(log2(n)) + 1` entries. For 10,000 IDs, I
rounded `log2(10000)` down to 13 and added 1. The search for the last ID
took those 14 checks, while linear search checked all 10,000 IDs.

If I needed to find one ticket in an unsorted support case export, I would
use linear search and save the time it would take to sort the export. For
repeated lookups in an export already sorted by ticket ID, I would use
binary search.