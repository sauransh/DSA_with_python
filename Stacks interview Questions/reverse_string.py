'''Stack: Reverse String ( ** Interview Question)
The reverse_string function takes a single parameter string, which is the string you want to reverse.

Return a new string with the letters in reverse order.
'''
import Stack_implementation_with_LIST

def reverse_string(my_string):
    stack = Stack_implementation_with_LIST.Stack()
    reversed_string = ''

    for char in my_string:
        stack.push(char)
    
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reverse_string

st = 'hello'

print ( reverse_string(st) )