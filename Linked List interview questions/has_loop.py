'''Write a method called has_loop that is part of the linked list class.

The method should be able to detect if there is a cycle or loop present in the linked list.

The method should utilize Floyd's cycle-finding algorithm, also known as the "tortoise and hare" algorithm, to determine the presence of a loop efficiently.

The method should follow these guidelines:

Create two pointers, slow and fast, both initially pointing to the head of the linked list.

Traverse the list with the slow pointer moving one step at a time, while the fast pointer moves two steps at a time.

If there is a loop in the list, the fast pointer will eventually meet the slow pointer. If this occurs, the method should return True.

If the fast pointer reaches the end of the list or encounters a None value, it means there is no loop in the list. In this case, the method should return False.'''


def has_loop(self):
    slow = self.head
    fast = self.head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
        else:
            return False
        
'''DRY RUN:
 loop: 1->2->3->4->1            slow,fast -> head
       ^                        s|f: 1|1,2|3,3|1,4|3,1|1
       s
       f
'''
