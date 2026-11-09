# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Implementation Documentation

### Support Ticket ID Application

I used the BST to organize support ticket IDs, check whether an ID was
present, and list the stored IDs in numerical order. Each node stored one
ID rather than a complete ticket record.

I inserted nine IDs in the order
`[6000, 5963, 6078, 5914, 5987, 6031, 6096, 5972, 5991]`.
This made `6000` the root and placed values in both subtrees.

### Recursive Insertion

I initialized each node with a value and two child references set to
`None`. The BST initially had no root.

I implemented `insert()` by assigning the recursive helper's result to
`self.root`. The helper created a node when it reached an empty position.
It followed the left subtree for a smaller ID and the right subtree for
a larger ID. Returning the current node preserved the connections as the
recursive calls finished.

I ignored duplicate IDs. When an ID matched an existing node, the helper
returned that node without adding another entry.

### Recursive Search

I started each search at the root. A matching ID returned `True`, while
an empty position returned `False`. Otherwise, the helper searched only
the subtree that could contain the requested ID.

I demonstrated searches for existing IDs `6000` and `5972`, followed by
missing IDs `5902` and `6053`. The missing examples covered an ID below
the stored range and an ID between stored values.

### In-Order Traversal

I collected IDs by visiting the left subtree, the current node, and then
the right subtree. This produced sorted output because smaller IDs were
visited before each node and larger IDs afterward.

Each call to `inorder()` created a new result list. The recursive helper
appended IDs to that shared list without rearranging the tree.

### Edge Cases and Insertion Order

I demonstrated that an empty tree returned `[]` from traversal and
`False` from search. I also inserted `5987` again and compared traversal
results before and afterward to confirm that the stored IDs were
unchanged.

I built a separate tree using the same IDs in ascending order. Every
new ID became a right child, creating a chain. Searching for `6096`
required nine node visits in that tree, compared with three in the
original tree.

A reasonably balanced tree supported O(log n) search and insertion.
The sequential example demonstrated their O(n) worst case. In-order
traversal took O(n) time because it visited every node. My implementation
did not automatically balance the tree.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

### My Reflection

This assignment gave me practice applying BST concepts to support ticket
IDs. No single method was especially difficult, but connecting the node
structure, recursive operations, and ordering rules required thought and
attention throughout the implementation. I worked through the methods
one section at a time and followed specific IDs through the comparisons
to understand how the operations fit together.

For insertion, smaller IDs went left and larger IDs went right until an
empty position was reached. Search used the same ordering to follow only
the subtree that could contain the requested ID. In-order traversal
visited smaller IDs, the current ID, and then larger IDs, producing a
sorted list without changing the tree.

I used two insertion orders to compare search performance. Finding
`6096` required three node visits in the original tree and nine after
ascending insertion created a chain. A reasonably balanced BST supported
O(log n) searches, compared with O(n) linear searches through an unsorted
list. However, the sequential example demonstrated that BST searches
could also take O(n). For ticket IDs generated in ascending order,
automatic balancing would be a useful improvement beyond my
implementation.