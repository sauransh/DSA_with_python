'''DLL: Swap Nodes in Pairs ( ** Interview Question)
You are given a doubly linked list.

Implement a method called swap_pairs within the class that swaps the values of adjacent nodes in the linked list. The method should not take any input parameters.

Note: This DoublyLinkedList does not have a tail pointer which will make the implementation easier.

Example:

1-->2-->3-->4--> should become 2-->1-->4-->3-->

Your implementation should handle edge cases such as an empty linked list or a linked list with only one node.

Note: You must solve the problem WITHOUT MODIFYING THE VALUES in the list's nodes (i.e., only the nodes' prev and next pointers may be changed.)'''




def swap_pairs(self):
    # Create a dummy node to simplify swapping logic
    dummy = Node(0)
    # Connect the dummy node to the head of the list
    dummy.next = self.head
    # Set 'prev' to the dummy node for the first iteration
    prev = dummy
 
    # Iterate while there are at least two nodes left
    while self.head and self.head.next:
        # Identify the first node of the pair to swap
        first_node = self.head
        # Identify the second node of the pair to swap
        second_node = self.head.next
 
        # Update 'next' pointers to swap the node pair
        prev.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node
 
        # Update 'prev' pointers for the swapped nodes
        second_node.prev = prev
        first_node.prev = second_node
        # Set the 'prev' of the node after the pair
        if first_node.next:
            first_node.next.prev = first_node
 
        # Move 'head' to the next pair of nodes
        self.head = first_node.next
        # Update 'prev' to the last node in the pair
        prev = first_node
 
    # Set the new head of the list after swapping
    self.head = dummy.next
    # Ensure the new head's 'prev' does not point to dummy
    if self.head:
        self.head.prev = None