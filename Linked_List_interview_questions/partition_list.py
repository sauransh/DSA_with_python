'''LL: Partition List ( ** Interview Question)
You are given a singly linked list implementation in Python that does not have a tail pointer (which will make this method simpler to implement).

You are tasked with implementing a method partition_list(self, x) that will take an integer x and partition the linked list such that all nodes with values less than x come before nodes with values greater than or equal to x. You should preserve the original relative order of the nodes in each of the two partitions.

You need to implement this method as a method of the LinkedList class. The method should take an integer x as input. If the linked list is empty, the method should return None.

To implement this method, you should create two new linked lists. These two linked lists will be made up of the original nodes from the linked list that is being partitioned, one for nodes less than x and one for nodes greater than or equal to x.  None of the nodes from the linked list should be duplicated.

The creation of a limited number of new nodes is allowed (e.g., dummy nodes to facilitate the partitioning process).

You should then traverse the original linked list and append each node to the appropriate new linked list.

Finally, you should connect the two new linked lists together.



Let's consider the list 2 -> 8 -> 1 -> 4 -> 3 -> 7, and we'll partition around the value 4.



Before

2 -> 8 -> 1 -> 4 -> 3 -> 7


After

After calling the partition_list(4), we have:

2 -> 1 -> 3 -> 8 -> 4 -> 7


Explanation:

The partition_list method separates the nodes into two lists, one for nodes with values less than x and the other for nodes with values equal to or greater than x. The function then concatenates these two lists.

In the above example, the nodes with values less than 4 (i.e., 2, 1, and 3) come before the nodes with values equal to or greater than 4 (i.e., 8, 4, and 7).  The relative order of the nodes is preserved.'''


def partition_list(self,x):
    
    if self.head == None:
        return
    
    dummy1 = Node(0)
    dummy2 = Node(0)
    prev1 = dummy1
    prev2 = dummy2
    current = self.head

    while current:
        if current.value >x:
            prev1.next = current
            prev1 = current
        else:
            prev2.next = current
            prev2 = current
        current = current.next
    
    prev1.next = dummy2.next
    self.head = dummy1.next



'''DRY RUN

X = 4
dummy1
prev1
(0)    -> 2 -> 8 -> 1 -> 4 -> 3 -> 7
dummy2
prev2


P1|P2 
0|0
2|0
2|8
1|8
1|4
3|4
3|7

o/p : 2 1 3 8 4 7

'''