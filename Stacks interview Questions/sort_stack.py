'''Stack: Sort Stack ( ** Interview Question)
The sort_stack function takes a single argument, a Stack object.  The function should sort the elements in the stack in ascending order (the lowest value will be at the top of the stack) using only one additional stack. 

The function should use the pop, push, peek, and is_empty methods of the Stack object.

Note: This is a new function, not a method within the Stack class.'''

import Stack_implementation_with_LIST as s

def sort_stack(input_stack = s.Stack()):

    sorted_stack = s.Stack()

    while not input_stack.is_empty():
        temp = input_stack.pop()
        while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
            input_stack.push(sorted_stack.pop())
        sorted_stack.push(temp)

    while not sorted_stack.is_empty():
        input_stack.push(sorted_stack.pop())




my_stack = s.Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack_list()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack_list()
