class Node:
    '''Node class constructor'''
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    '''Linked List constructor'''
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        '''Class Method to print linked list'''
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        
    def append(self,value):
        '''Class method to append new node to the linked list(add at end)'''
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.next = None
        self.length +=1
        return True
    
    def pop(self):
        '''Class method to pop last item from the list'''
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while(temp.next):
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length-=1
        if self.length ==0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self,value):
        '''Class method to add new node to the front of the list'''
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True
    
    def pop_first(self):
        '''Class method to remove first item from the list'''
        if self.length == 0:
            return
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1 
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self,index):
        '''Class method to get item at index'''
        if index<0 or index >=self.length:
            return None
        temp = self.head
        for _ in range(self.length):
            temp = temp.next
        return temp
    
    def set_value(self,index,value):
        '''Method to set value on a given index in the list'''
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False