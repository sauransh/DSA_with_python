'''
LL: Binary to Decimal ( ** Interview Question)
Your task is to implement the binary_to_decimal method for the LinkedList class. This method should convert a binary number, represented as a linked list, to its decimal equivalent.

In this context, a binary number is a sequence of 0s and 1s. The LinkedList class represents this binary number such that each node in the linked list contains a single digit (0 or 1) of the binary number, and the whole number is formed by traversing the linked list from the head to the end.

The binary_to_decimal method should start from the head of the linked list and use each node's value to calculate the corresponding decimal number. The formula to convert a binary number to decimal is as follows:

To put it in simple terms, each digit of the binary number is multiplied by 2 raised to the power equivalent to the position of the digit, counting from right to left starting from 0, and all the results are summed together to get the decimal number.

The binary_to_decimal method should return this calculated decimal number.



Examples

Consider the binary number 101. If this number is represented as a linked list, the head of the linked list will contain the digit 1, the next node will contain 0, and the last node will contain 1. When we apply the binary_to_decimal method on this linked list, the method should return the number 5, which is the decimal equivalent of binary 101.

Similarly, for a linked list representing the binary number 1101, the binary_to_decimal method should return the number 13.
'''


def binary_to_decimal(self):
    temp = self.head
    res = 0
    while temp:
        res = res*2 + temp.value
        temp= temp.next
    return res

'''
DRY RUN:

LL : 1 1 0 1

o/p : 13 -> 2^3 + 2^2 + 0 + 2^0

res
2*0 + 1 = 1
2*1 + 1 = 3
2*3 + 0 = 6
2*6 + 1 = 13
'''