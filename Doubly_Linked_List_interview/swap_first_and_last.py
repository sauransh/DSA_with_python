'''
DLL: Swap First and Last ( ** Interview Question)
Swap the values of the first and last node

Method name:
swap_first_last

Note that the pointers to the nodes themselves are not swapped - only their values are exchanged.
'''


def swap_first_last(self):
        # Check if the list is empty or has only one node
        if self.head is None or self.head == self.tail:
            return
        #Swap the values of the head and tail nodes
        self.head.value, self.tail.value = self.tail.value, self.head.value # tuple unpacking