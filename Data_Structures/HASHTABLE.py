class HashTable:
    def __init__(self,size=7):
        self.data_map = [None]*size
    
    def _hash(self,key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i,":",val)
            
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
        all_keys=[]
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

my_hashtable = HashTable()
my_hashtable.set_item('nails',1000)
my_hashtable.set_item('bolts',1200)
my_hashtable.set_item('bolt',100)
my_hashtable.set_item('mail',500)
my_hashtable.print_table()
print("hash " + str(my_hashtable._hash('mail')))

print(my_hashtable.get('bolt'))

print(my_hashtable.keys())