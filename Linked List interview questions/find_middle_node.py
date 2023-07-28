''''Implement the find_middle_node method for the LinkedList class.

The find_middle_node method should return the middle node in the linked list WITHOUT using the length attribute.

If the linked list has an even number of nodes, return the first node of the second half of the list.

Keep in mind the following requirements:

The method should use a two-pointer approach, where one pointer (slow) moves one node at a time and the other pointer (fast) moves two nodes at a time.

When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.

The method should return the middle node or the first node of the second half of the list if the list has an even number of nodes.

The method should only traverse the linked list once.  In other words, you can only use one loop'''


def middle_node(self):
    '''2 pointer approach solution
    slow pointer moves 1 step and fast jumps 2 steps until fast reaches none or fast.next 
    '''
    slow = self.head
    fast = self.head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


"""  
DRY RUN:
i/p : 1 2 3 4 5 6 7
o/p: 4

f                       f->fast|1|3|5|7|failed condition
^                       s->slow|1|2|3|4
1 2 3 4 5 6 7
^
s
"""


