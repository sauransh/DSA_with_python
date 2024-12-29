class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        
        cur = self.head
        prev = self.head
        while cur.next:
            prev = cur
            cur = cur.next
        prev.next = None
        self.tail = prev
        self.length -=1
        if self.length == 0:
            self.head = self.tail = None
        return cur

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1

    def pop_first(self):
        if self.length==0:
            return None
        
        temp = self.head
        self.head = self.head.next
        self.length-=1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.val = value
            return True
        return False
    
    def insert(self,index,value):
        if index<0 or index>=self.length:
            return False
        if index ==0:
            self.prepend(value)
        if index == self.length -1:
            self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length+=1


    

    def remove(self,index):
        if index<0 or index>=self.length:
            return
        if index ==0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()

        temp = self.get(index-1)
        temp.next = temp.next.next

        self.length-=1
    
    def reverse(self):
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




myll = LinkedList(1)
myll.append(2)
myll.append(3)
myll.append(4)

myll.print_list()
print('---------------')
print('pop',myll.pop().val)

myll.prepend(99)
myll.print_list()
print('pop_first',myll.pop_first().val)
myll.print_list()

print('get index',myll.get(1).val)
myll.insert(1,55)
myll.print_list()
myll.remove(1)
myll.print_list()
print('---------------')
print(myll.reverse())
myll.print_list()