# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Implementation Documentation

### Application Scenario

I modeled a technical support ticket system using `SupportTicket` and
`EscalatedTicket`. The scenario represented a support workflow in which a ticket
recorded an issue and troubleshooting notes, while an escalated ticket also
identified an assigned engineer and the reason for escalation.

### Parent Class

I created `SupportTicket` with the class variable `department` and the instance
variables `ticket_id`, `description`, and `notes`. The constructor initialized
each ticket with its own empty notes list. The `__str__()` method returned a
readable summary containing the ticket ID, description, and number of notes.

### Child Class and Inheritance

I created `EscalatedTicket` as a subclass of `SupportTicket`. Its constructor
called `super().__init__()` to reuse the parent initialization, then added
`assigned_engineer` and `escalation_reason`. I also added the class variable
`support_level` and the method `reassign_engineer()`. The child class overrode
`__str__()` and extended the parent summary with the escalation details.

### Encapsulation and Student-Created Extension

I added `add_note()` to keep note validation with the ticket's data. The method
removed surrounding whitespace and raised `ValueError` when the resulting
string was empty. Valid notes were appended to the notes list. The child class
inherited this method without duplicating its implementation. The attributes
remained public, so the method provided a consistent way to add notes without
preventing direct access to the list.

### Namespace Demonstration

I created two escalated tickets and accessed `support_level` through both the
class and an instance. Both accesses returned the class value. I then added
`callback_requested` to only the first ticket. Printing each object's
`__dict__` showed its instance attributes and confirmed that the additional
attribute belonged only to the first ticket. I also displayed the names in
`EscalatedTicket.__dict__` and its stored `support_level` value.

### Shallow and Deep Copying

I created an escalated ticket containing one troubleshooting note, then used
`copy()` and `deepcopy()` to create two copies. After I added a second note to
the original, the original and shallow copy displayed both notes. The deep
copy displayed only the first note. Identity checks showed that the shallow
copy was a separate ticket object but shared the original notes list, while
the deep copy had an independent notes list.

### Memory Behavior and Growth

Each separately constructed ticket received its own instance attributes and
notes list. Adding notes increased the list's contents and memory needs. The
class variables were stored on their respective classes and were accessible
through instances. The shallow copy reused the existing notes list, while the
deep copy required additional storage for an independent list.

### Execution and Edge Case

The program was executed with Python 3 from the unit folder:

```bash
python unit1_discussion.py
```

The `main()` function created both ticket types, demonstrated engineer
reassignment, and called the namespace and copying demonstrations. It also
attempted to add a whitespace-only note inside a `try`/`except` block. The
exception handler displayed an explanatory message, the existing notes
remained intact, and the remaining demonstrations continued. Labeled output
made the results of each operation visible.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

### Reflection

I learned how Python classes grouped related data and behavior, how
inheritance reused existing functionality, and how special methods such as
`__str__()` controlled an object's readable representation. Creating support
tickets also helped me distinguish class attributes from instance attributes.

The main challenge was understanding why a shallow copy reflected changes made
to the original ticket's notes. I worked through this by displaying each list
and comparing object identities with `is`. These checks showed that separate
ticket objects could reference the same mutable list.

A procedural implementation could have used functions operating on ticket
dictionaries. The object-oriented approach kept ticket information and related
operations together. Inheritance improved reusability because escalated
tickets reused initialization and note validation. Keeping validation in
`add_note()` also supported maintainability by placing that logic in one
method.

I also considered the overhead involved. Classes added structure to a small
program, and deep copying required additional memory for an independent notes
list. For larger support applications, this organization offered a practical
foundation for additional ticket types. In future projects, I could apply the
same principles while choosing copying behavior carefully to prevent
unintended changes to shared data.

Additionally, although `add_note()` validated notes, the public `notes`
attribute still allowed that validation to be bypassed through
`ticket.notes.append("")`. In a future iteration, I could improve encapsulation
by providing read-only access to notes and routing additions through
`add_note()`.
