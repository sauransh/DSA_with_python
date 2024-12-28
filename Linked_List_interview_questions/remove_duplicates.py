'''LL: Remove Duplicates ( ** Interview Question)
You are given a singly linked list that contains integer values, where some of these values may be duplicated.

Note: this linked list class does not have a tail which will make this method easier to implement.

Your task is to implement a method called remove_duplicates() within the LinkedList class that removes all duplicate values from the list.

Your method should not create a new list, but rather modify the existing list in-place, preserving the relative order of the nodes.

You can implement the remove_duplicates() method in two different ways:



Using a Set - This approach will have a time complexity of O(n), where n is the number of nodes in the linked list. You are allowed to use the provided Set data structure in your implementation.

Without using a Set - This approach will have a time complexity of O(n^2), where n is the number of nodes in the linked list. You are not allowed to use any additional data structures for this implementation.



Here is the method signature you need to implement:

def remove_duplicates(self):


Example:

Input:

LinkedList: 1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5

Output:

LinkedList: 1 -> 2 -> 3 -> 4 -> 5

'''


'''
Approach 1 : using set 
time complexity: O(n)

'''
def remove_duplicates(self):
    values = set()
    pre = None
    current = self.head

    while current:
        if current.value in values:
            pre.next = current.next
            self.length-=1
        else:
            values.add(current.value)
            pre =current
        current = current.next
'''
Approach 2 : without set
time complexity : O(n^2)
'''

def remove_duplicates(self):
    current = self.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
                self.length -=1
            else:
                runner = runner.next
            current = current.next

'''DRY RUN

1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5
^
c

C : 1|2|3| |4| |5
'''








