"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class SupportTicket:
    department = "Technical Support"

    def __init__(self, ticket_id, description):
        self.ticket_id = ticket_id
        self.description = description
        self.notes = []

    # Student-created extension:
    # Add troubleshooting notes while rejecting empty or whitespace-only input.
    def add_note(self, note):
        cleaned_note = note.strip()

        if not cleaned_note:
            raise ValueError("A troubleshooting note cannot be empty.")

        self.notes.append(cleaned_note)

    def __str__(self):
        return (
            f"Ticket {self.ticket_id}: {self.description} "
            f"({len(self.notes)} notes)"
        )


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class EscalatedTicket(SupportTicket):
    support_level = "Escalated Support"

    def __init__(
            self, ticket_id, description, assigned_engineer, escalation_reason
    ):
        super().__init__(ticket_id, description)
        self.assigned_engineer = assigned_engineer
        self.escalation_reason = escalation_reason

    def reassign_engineer(self, assigned_engineer):
        self.assigned_engineer = assigned_engineer

    def __str__(self):
        return (
            f"{super().__str__()} | "
            f"Engineer: {self.assigned_engineer} | "
            f"Escalation reason: {self.escalation_reason}"
        )


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    ticket1 = EscalatedTicket(
        1003,
        "Reports fail to load",
        "Alex",
        "Initial troubleshooting did not resolve the issue"
    )

    ticket2 = EscalatedTicket(
        1004,
        "Scheduled jobs are delayed",
        "Jordan",
        "Processing delays affect multiple customers"
    )

    # Access the same class variable through the class and an instance.
    print("Through the class:", EscalatedTicket.support_level)
    print("Through an instance:", ticket1.support_level)

    # Add an attribute to only this instance after its creation.
    ticket1.callback_requested = True

    print("\nTicket 1 instance namespace:")
    print(ticket1.__dict__)

    print("\nTicket 2 instance namespace:")
    print(ticket2.__dict__)

    # Inspect names defined directly in the child class.
    print("\nEscalatedTicket class namespace:")
    print(list(EscalatedTicket.__dict__.keys()))

    print("\nClass variable stored in the class namespace:")
    print(EscalatedTicket.__dict__["support_level"])


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = EscalatedTicket(
        1005,
        "Database connection fails",
        "Alex",
        "Connection failures persist after troubleshooting"
    )
    original.add_note("Reviewed the connection settings.")

    # A shallow copy creates a new ticket but shares its nested notes list.
    shallow_copy = copy(original)

    # A deep copy creates a new ticket with an independent notes list.
    deep_copy = deepcopy(original)

    # Modify the original ticket's nested mutable data after copying.
    original.add_note("Restarted the database service.")

    for label, ticket in [
        ("Original", original),
        ("Shallow copy", shallow_copy),
        ("Deep copy", deep_copy)
    ]:
        print(f"\n{label}:")
        print(ticket)
        print("Notes:", ticket.notes)

    print("\nOriginal and shallow copy are the same ticket:")
    print(original is shallow_copy)

    print("Original and shallow copy share the same notes list:")
    print(original.notes is shallow_copy.notes)

    print("Original and deep copy share the same notes list:")
    print(original.notes is deep_copy.notes)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Support Ticket ===")
    ticket = SupportTicket(1001, "Unable to sign in")
    print(ticket)
    ticket.add_note("Confirmed that the account is active.")
    print("After adding a note:")
    print(ticket)
    print("Notes:", ticket.notes)

    # Handle an invalid note without stopping the remaining demonstrations.
    try:
        ticket.add_note("   ")
    except ValueError as error:
        print("Could not add note:", error)

    print("Notes after the rejected entry:", ticket.notes)

    print("\n=== Escalated Ticket ===")
    escalated_ticket = EscalatedTicket(
        1002,
        "Platform unavailable",
        "Jim",
        "Multiple customers affected"
    )
    print(escalated_ticket)

    escalated_ticket.reassign_engineer("Jordan")
    print("After reassignment:")
    print(escalated_ticket)

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
