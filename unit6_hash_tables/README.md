# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Implementation

I created a dictionary called `case_assignments` to track the engineers
assigned to active technical support cases. Each case ID served as an integer
key, and the assigned engineer's name served as a string value.

I populated the dictionary with five case assignments and retrieved the
engineers assigned to two existing cases. I then reassigned case `29039`
from Matthew Mann to Mark Lyon and removed case `39403` to simulate its
closure.

I tested three edge cases involving the closed case. I used `get()` with a
default message when looking up the missing key. For deletion and
reassignment, I checked whether the key existed before proceeding. These
checks prevented a `KeyError` during deletion and an unintended insertion
during reassignment.

The dictionary used hashing to facilitate key-based retrieval without
requiring the case IDs to be sorted.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

### Reflection

Apart from using the `__dict__` attribute in Assignment 1, I had little
experience with dictionaries in Python. I was impressed by their capabilities.
I initially expected to have to implement a hashing mechanism for this
assignment, but Python's built-in `dict` type already handled that.

The zyBooks material gave me a good understanding of hashing and collision
resolution before beginning the assignment. One consideration was handling
missing keys. I was surprised to learn that attempting to delete a nonexistent
key with `del` raises a `KeyError`. I used a conditional statement to prevent
this exception from occurring.

Hash tables use a hash function to help determine where a key-value pair
should be stored. A collision occurs when different keys map to the same
initial table index. Python dictionaries handle collisions by probing other
positions in the hash table, whereas separate chaining is an alternative
approach that stores multiple entries in the same bucket.

Frequent collisions can reduce lookup efficiency because additional entries
must be examined. Although dictionary lookup has a worst-case time complexity
of O(n), its average time complexity of O(1) makes it particularly useful
for applications requiring frequent retrieval by key.