'''
Queue Implementation using Array/ LinkedList
'''

class Node:
    def __init__(self,value):
        self.val = value
        self.next = None
    
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        dequeued = self.front.val
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued
    
    def front_value(self):
        if self.is_empty():
            return "Queue is empty"
        return self.front.val

    def is_empty(self):
        return self.front is None
    
    def print_queue(self):
        if self.is_empty():
            return "Queue is empty"
        temp = self.front
        while temp:
            print(temp.val)
            temp = temp.next

q = Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
q.print_queue()
print('DeQueued:',q.dequeue())

q.print_queue()


