class HashTable:
    def __init__(self,size = 7):
        self.data_map = [None]* size
    
    def _hash(self,key):
        my_hash = 0
        for s in key:
            my_hash = (my_hash+ ord(s)*23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i,':',val)
    
    def set_item(self,key,value):
        index = self._hash(key)

        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])
    
    def get(self,key):
        index = self._hash(key)

        if self.data_map[index]:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []

        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys



myHT = HashTable()

myHT.set_item('well',2)
myHT.set_item('swell',3)
myHT.set_item('hell',4)
myHT.set_item('bell',5)

myHT.print_table()

print(myHT.get('bell'))

print(myHT.keys())