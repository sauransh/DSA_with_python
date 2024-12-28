'''
DLL: Palindrome Checker ( ** Interview Question)
Write a method to determine whether a given doubly linked list reads the same forwards and backwards.

For example, if the list contains the values [1, 2, 3, 2, 1], then the method should return True, since the list is a palindrome.

If the list contains the values [1, 2, 3, 4, 5], then the method should return False, since the list is not a palindrome.

Method name:
is_palindrome
'''

def is_palindrome(self):
    if self.length <=1:
        return True
    start = self.head
    end = self.tail
    for i in range(self.length//2):
        if start.value != end.value:
            return False
        start = start.next
        end=end.prev
    return True
