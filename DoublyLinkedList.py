class Node:
    '''Node class with contructor'''
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp= temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next
        self.length +=1
        return True
    
    def pop(self):
        if self.length == 0:
            return
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -=1
        return temp
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -=1
        return temp
    
    def get(self,index):
        if index <0 or index >=self.length:
            return
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1,index,-1):
                temp = temp.prev
        return temp
    
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False


dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.append(6)
""" dll.print_list()
print('pop:',dll.pop())
#print('pop:',dll.pop())
#print('pop:',dll.pop())
#print('pop:',dll.pop())
print('Prepend:')
dll.prepend(7)
print('popfirst:')
dll.pop_first() """
dll.print_list()

print('get',dll.get(4))
dll.set_value(4,77)
dll.print_list()