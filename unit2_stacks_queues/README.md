# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Implementation Documentation

### Design Approach

I implemented a technical support workflow with two data structures. A
stack stored descriptions of ticket edits and retrieved them in reverse
order to simulate undo. A queue stored incoming ticket descriptions and
retrieved them in arrival order for processing.

The undo demonstration showed the order in which edits would be reversed.
It did not restore actual ticket fields.

### Stack Implementation

I used a Python list to store stack values and treated its end as the top.
The `push()` method appended a value, and `pop()` removed and returned the
last value added. Using the same end for both operations produced
last-in-first-out (LIFO) behavior.

The `peek()` method used index `-1` to return the top value without removing
it. The `is_empty()` method returned whether the list contained no values.

The demonstration pushed four edits: a category change, a priority change,
a team assignment, and a status change. It then popped them in reverse
order, beginning with the status change. The peek result matched the first
popped edit, showing that peeking had left the stack unchanged.

### Queue Implementation

I used `collections.deque` to store queue values. The `enqueue()` method
appended tickets at the back, and `dequeue()` used `popleft()` to remove and
return the front ticket. Adding and removing at opposite ends produced
first-in-first-out (FIFO) behavior.

The `front()` method used index `0` to return the next ticket without
removing it. The `is_empty()` method returned whether the deque contained
no values.

The demonstration enqueued Tickets 101 through 104 and dequeued them in
that same order. Ticket 101 appeared in both the front result and the first
dequeue result, showing that viewing it had not removed it.

### Edge Case Handling

I checked for an empty structure before each removal or viewing operation.
Empty calls to `pop()`, `peek()`, `dequeue()`, and `front()` raised
`IndexError` with descriptive messages. The demonstrations caught these
exceptions and printed the messages so execution continued.

I also created separate single-item structures. Each reported `False` for
`is_empty()` before removal and `True` afterward.

### Memory Usage

Both structures required additional storage as more items were added.
Their theoretical container space was O(n), where n represented the number
of stored items. Memory for the ticket and edit descriptions also depended
on the lengths of their strings.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

### Reflection

This assignment helped me connect stack and queue behavior to a technical
support workflow. I implemented a stack with a Python list and a queue with
a deque. Although both structures stored sequences of values, their
removal rules served different purposes. The stack retrieved recent ticket
edits first, while the queue retrieved incoming tickets in arrival order.

One point I needed to clarify was whether `self.items.pop()` called the
stack's own `pop()` method recursively. Reviewing the object before the
method call helped me understand that `self.items` referred to a list, so
the call used Python's existing list method. This clarified how my stack
implementation built on operations provided by its underlying container.

The demonstrations also showed why predictable ordering and empty-case
handling mattered. LIFO (last in, first out) suited undo because the latest edit was retrieved
first. FIFO (first in, first out) suited a first-come-first-served ticket
workflow because earlier arrivals were retrieved first. Raising and catching `IndexError` made
invalid operations explicit while allowing the demonstrations to continue.
The stack simulated undo order; actually restoring ticket fields would
have required additional reversal logic.
