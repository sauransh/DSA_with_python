from collections import OrderedDict

class LRUCache(OrderedDict):
    def __init__(self, capacity:int):
        self.capacity = capacity
    
    def get(self,key: int)->int:
        if key in self:
            self.move_to_end(key)
            return self[key]
        else:
            return -1
        
    def put(self,key:int,value:int)->None:
        self[key] = value

        if len(self)> self.capacity:
            self.popitem(last=False)
        self.move_to_end(key)

od = OrderedDict()
od[1] = 1
od[2] = 2
od[3] = 3
od[4] = 4
lc = LRUCache(4)
lc.put(1,1)
lc.put(2,2)
lc.put(3,3)
lc.put(4,4)
print(lc)
lc.get(2)
lc.put(7,7)
print(lc)