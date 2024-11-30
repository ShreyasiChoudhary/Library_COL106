from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        new_size = get_next_size()
        old = self.init_array
        self.init_array = [None]* new_size
        self.capacity = new_size
        self.count=0
        if(self.collision_type=="Chain" or self.collision_type=="Linear"):
            self.params = (self.params[0], new_size)
        else:
            self.params = (self.params[0], self.params[1], self.params[2], new_size)
        for slot in old:
            if slot != None:
                if self.collision_type=="Chain":
                    for y in slot:
                        self.insert(y)
                else:
                    self.insert(slot)
        
    def insert(self, x):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(x)
        
        if self.get_load() >= 0.5:
            self.rehash()
            
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        new_size = get_next_size()
        old = self.init_array
        self.init_array = [None]* new_size
        self.capacity = new_size
        self.count=0
        if(self.collision_type=="Chain" or self.collision_type=="Linear"):
            self.params = (self.params[0], new_size)
        else:
            self.params = (self.params[0], self.params[1], self.params[2], new_size)
        for slot in old:
            if slot != None:
                if self.collision_type=="Chain":
                    for y in slot:
                        self.insert(y)
                else:
                    self.insert(slot[0])
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()