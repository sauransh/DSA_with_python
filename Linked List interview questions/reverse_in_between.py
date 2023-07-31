'''
LL: Reverse Between ( ** Interview Question)
You are given a singly linked list and two integers m and n. Your task is to write a method reverse_between within the LinkedList class that reverses the nodes of the linked list from index m to index n (inclusive) in one pass and in-place.

Note: the Linked List does not have a tail which will make the implementation easier.

Input

The method reverse_between takes two integer inputs m and n.

The method will only be passed valid indexes (you do not need to test whether the indexes are out of bounds)



Output

The method should modify the linked list in-place by reversing the nodes from index m to index n.

If the linked list is empty or has only one node, the method should return None.



Example

Suppose the linked list is 1 -> 2 -> 3 -> 4 -> 5, and m = 2 and n = 4. Then, the method should modify the linked list to 1 -> 2 -> 5 -> 4 -> 3 .



Constraints

The algorithm should run in one pass and in-place, with a time complexity of O(n) and a space complexity of O(1).
'''

def reverse_between(self,m,n):
    if self.length <=1:
        return


    dummy = Node(0)
    dummy.next = self.head
    prev = dummy

    for _ in range(m):
        prev = prev.next

    current = prev.next

    for _ in range(n-m):
        temp = current.next
        current.next = temp.next
        temp.next = prev.next
        prev.next = temp

    self.head = dummy.next


'''DRY RUN

                    p    m    t    n   
dummy(0)-->    1 -> 2 -> 3 -> 4 -> 5, and m = 2 and n = 4
prev

prev|current|temp

2|3|4
c.n->t.n


'''