"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # The end of the list is the top, where new values are added.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if not self.items:
            raise IndexError("The stack has no items to remove.")

        # Removing from the top returns the last value added (LIFO).
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if not self.items:
            raise IndexError("There is no top item to inspect because the stack is empty.")

        # Read the last item (the top) without changing the stack.
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return not self.items


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Add at the back so earlier arrivals stay closer to the front.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if not self.items:
            raise IndexError("The queue has no waiting items to remove.")

        # Removing from the front returns the first value added (FIFO).
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if not self.items:
            raise IndexError("There is no front item to inspect because the queue is empty.")

        # Read the first item without removing it from the queue.
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return not self.items


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO: TICKET EDIT HISTORY ===")
    edit_history = Stack()

    edits = [
        "Changed category from General to Network",
        "Changed priority from Low to Medium",
        "Assigned ticket to the networking team",
        "Changed status from New to In Progress",
    ]

    # Record edits in the order they occurred.
    for edit in edits:
        edit_history.push(edit)
        print(f"Pushed edit: {edit}")

    print(f"\nNext edit to undo (peek): {edit_history.peek()}")
    print("Peeking at the top edit did not remove it from the stack.")

    print("\nSimulating undo in LIFO order, newest edit first:")
    while not edit_history.is_empty():
        print(f"Popped edit to undo: {edit_history.pop()}")

    print(f"Stack empty after removing all edits: {edit_history.is_empty()}")
    print("\n--- Empty stack tests ---")

    # Catch each invalid operation so the remaining demonstrations can run.
    try:
        edit_history.pop()
    except IndexError as error:
        print(f"Pop on an empty stack: {error}")

    try:
        edit_history.peek()
    except IndexError as error:
        print(f"Peek on an empty stack: {error}")

    print("\n--- Single-item stack test ---")
    single_edit_history = Stack()
    single_edit_history.push("Changed priority from Low to Medium")

    print(f"Stack empty before removal: {single_edit_history.is_empty()}")
    print(f"Popped only edit: {single_edit_history.pop()}")
    print(f"Stack empty after removal: {single_edit_history.is_empty()}")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO: INCOMING SUPPORT TICKETS ===")
    ticket_queue = Queue()

    tickets = [
        "Ticket 101: Login failure",
        "Ticket 102: Network timeout",
        "Ticket 103: Missing account permissions",
        "Ticket 104: Report generation error",
    ]

    # Record tickets in their arrival order.
    for ticket in tickets:
        ticket_queue.enqueue(ticket)
        print(f"Enqueued ticket: {ticket}")

    print(f"\nNext ticket to process (front): {ticket_queue.front()}")
    print("Viewing the front ticket did not remove it from the queue.")

    print("\nProcessing tickets in FIFO order, earliest arrival first:")
    while not ticket_queue.is_empty():
        print(f"Dequeued ticket to process: {ticket_queue.dequeue()}")

    print(f"Queue empty after processing all tickets: {ticket_queue.is_empty()}")
    print("\n--- Empty queue tests ---")

    # Catch each invalid operation so the remaining demonstrations can run.
    try:
        ticket_queue.dequeue()
    except IndexError as error:
        print(f"Dequeue on an empty queue: {error}")

    try:
        ticket_queue.front()
    except IndexError as error:
        print(f"Front on an empty queue: {error}")

    print("\n--- Single-item queue test ---")
    single_ticket_queue = Queue()
    single_ticket_queue.enqueue("Ticket 105: Password reset")

    print(f"Queue empty before removal: {single_ticket_queue.is_empty()}")
    print(f"Dequeued only ticket: {single_ticket_queue.dequeue()}")
    print(f"Queue empty after removal: {single_ticket_queue.is_empty()}")

if __name__ == "__main__":
    main()
