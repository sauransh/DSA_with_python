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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
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
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self,index,value):
        '''Method to set value on a given index in the list'''
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        '''Class method to insert item at a prticular index;
            Moving of node required
        '''
        if index<0 or index>self.length:
            return False
        
        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
        return True
    
    def remove(self,index):
        '''Method to  remove item from a give index'''

        if index <0 or index>self.length:
            return
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length-=1
        return temp
    
    def reverse(self):
        '''Method to reverse a list'''

        if self.length == 0:
            return
        
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before #flip signs
            before =temp
            temp = after


# ll - linkedlist object 'constructor call'
ll = LinkedList(1)
print('Append:')
# append method
ll.append(2)
ll.append(3)
ll.append(4)

ll.print_list()

# Pop
ll.pop()
print('POP:')
ll.print_list()

#PREPRND
print('PREPEND:')
ll.prepend(9)
ll.print_list()

#pop first
print('POP_FIRST:')
ll.pop_first()
ll.print_list()

#get
print('GET:',ll.get(1))

#set value

print('set_value',ll.set_value(2,7))
ll.print_list()

#insert
print('insert:',ll.insert(1,77))
ll.print_list()

#remove
print('remove:',ll.remove(2))
ll.print_list()

#reverse
print('reverse',ll.reverse())
ll.print_list()