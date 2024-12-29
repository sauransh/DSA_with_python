class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next
    
    def enqueue(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length +=1
        return True

    def dequeue(self):
        if self.length == 0:
            return
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -=1
        return temp


q = Queue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.print_queue()
print('Dequeue',q.dequeue())
q.print_queue()