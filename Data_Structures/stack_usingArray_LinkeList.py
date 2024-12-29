'''
Implement Stack using Array/ Linked List
'''


class Node:
    def __init__(self,val,next= None):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        poped = self.top.val
        self.top = self.top.next
        return poped
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.top.val
    
    def is_empty(self):
        return self.top is None
    
    def print_stack(self):
        if self.is_empty():
            return "stack is empty"
        temp = self.top
        while temp:
            print(temp.val)
            temp = temp.next

        
        

mystack = Stack()
print(mystack.print_stack())
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.print_stack()
print("pop")
print("popped:", mystack.pop())
mystack.print_stack()