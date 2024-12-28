'''
LL: Find Kth Node From End ( ** Interview Question)
Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.

Given this LinkedList:

1 -> 2 -> 3 -> 4

If k=1 then return the first node from the end (the last node) which contains the value of 4.

If k=2 then return the second node from the end which contains the value of 3, etc.

If the linked list has fewer than k items, the program should return None.

The find_kth_from_end function should follow these requirements:

The function should utilize two pointers, slow and fast, initialized to the head of the linked list.

The fast pointer should move k nodes ahead in the list.

If the fast pointer becomes None before moving k nodes, the function should return None, as the list is shorter than k nodes.

The slow and fast pointers should then move forward in the list at the same time until the fast pointer reaches the end of the list.

The function should return the slow pointer, which will be at the k-th position from the end of the list.



This is a separate function that is not a method within the LinkedList class. This means you need to indent the function all the way to the left. 

'''

def find_kth_node_from_end(llist,k):
    slow = llist.head
    fast = llist.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next
    return slow





'''DRY RUN:
if k = 2 o/p: 3

1->2->3->4              s|f|k: 1|1|0,1|2|1,1|3|2,2|4|2,3|none|2
^
s
f
'''
