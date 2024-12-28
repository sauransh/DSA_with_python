'''
DLL: Reverse ( ** Interview Question)
Create a new method called reverse that reverses the order of the nodes in the list, i.e., the first node becomes the last node, the second node becomes the second-to-last node, and so on.

To do this, you'll need to traverse the list and change the direction of the pointers between the nodes so that they point in the opposite direction.

Do not change the value of any of the nodes.

Once you've done this for all nodes, you'll also need to update the head and tail pointers to reflect the new order of the nodes.

'''

'''
Pseudo code for the reverse method:

1. Set current_node to head

2. While current_node is not None:

    Set a temporary variable, temp_next, to current_node.next

    Set current_node.next to current_node.prev

    Set current_node.prev to temp_next

    Set current_node to temp_next (which is actually the previous node after swapping)

3. Swap head and tail pointers of the DoublyLinkedList
'''

def reverse(self):
    current = self.head
    while current:
        temp = current.next
        current.next = current.prev
        current.prev = temp
        current = temp
    self.head,self.tail = self.tail,self.head   # Tuple unpacking to swap head and tail position 
    

    