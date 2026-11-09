"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # The helper follows smaller values left and larger values right.
        # Assign its result so the first inserted node becomes the root.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # An empty position is where the new ticket ID belongs.
        if node is None:
            return Node(value)

        # Smaller IDs belong in the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger IDs belong in the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Equal IDs leave the tree unchanged, preventing duplicates.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # Each comparison lets the search skip the opposite subtree.
        # A balanced tree needs fewer comparisons than a linear scan.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # An empty position means the ticket ID was not found.
        if node is None:
            return False

        if value == node.value:
            return True

        # Search only the subtree that could contain the ticket ID.
        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        # Collect this traversal's results in a new list.
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # An empty subtree has no values to add.
        if node is None:
            return

        # Visit smaller IDs before adding the current ID.
        self._inorder_recursive(node.left, values)
        values.append(node.value)

        # Visit larger IDs after adding the current ID.
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    tickets = BST()
    ticket_ids = [1050, 1025, 1075, 1010, 1035, 1060, 1090, 1030, 1040]

    # This insertion order places ticket IDs on both sides of the root.
    for ticket_id in ticket_ids:
        tickets.insert(ticket_id)

    # Searching for an ID below 1050 skips the root's entire right subtree.
    # Further comparisons narrow the search to one branch at each node.
    print("Support ticket IDs in insertion order:", ticket_ids)
    print("Root ticket ID:", tickets.root.value)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    # Visiting left, current, then right lists IDs from smallest to largest.
    sorted_ids = tickets.inorder()
    print("Support ticket IDs in sorted order:", sorted_ids)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # Both IDs were inserted, so each search should return True.
    for ticket_id in [1050, 1030]:
        print(
            f"Search for existing ticket {ticket_id}: "
            f"{tickets.search(ticket_id)} (expected True)"
        )

    # 1000 is below the smallest ID; 1065 falls between stored IDs.
    # Both searches reach an empty position and return False.
    for ticket_id in [1000, 1065]:
        print(
            f"Search for missing ticket {ticket_id}: "
            f"{tickets.search(ticket_id)} (expected False)"
        )

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    empty_tickets = BST()

    # An empty tree has no IDs to collect and no matching node to find.
    print("Empty tree traversal:", empty_tickets.inorder(), "(expected [])")
    print("Search empty tree for 1050:", empty_tickets.search(1050),
          "(expected False)")

    # Reinserting an existing ID should leave the stored IDs unchanged.
    before_duplicate = tickets.inorder()
    tickets.insert(1035)
    after_duplicate = tickets.inorder()

    print("Ticket IDs after inserting duplicate 1035:", after_duplicate)
    print("Stored IDs unchanged:", before_duplicate == after_duplicate,
          "(expected True)")

    print("\nSequential insertion demonstration")

    sequential_tickets = BST()

    # Ascending IDs create a chain because each new ID is larger.
    for ticket_id in sorted_ids:
        sequential_tickets.insert(ticket_id)

    # Follow the right-child references to display the resulting chain.
    right_chain = []
    current = sequential_tickets.root

    while current is not None:
        right_chain.append(current.value)
        current = current.right

    print("IDs along right-child links:", right_chain)
    print("Search for 1090:", sequential_tickets.search(1090),
          "(expected True)")

if __name__ == "__main__":
    main()