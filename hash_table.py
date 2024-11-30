from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
        self.collision_type = collision_type
        self.count =0
        self.params = params
        if len(self.params)==2:
            self.capacity=self.params[1]
            self.z = self.params[0]
        else:
            self.capacity=self.params[3]
            self.z = self.params[0]
            self.z1 = self.params[1]
            self.c = self.params[2]
        self.init_array = [None]*self.capacity
        
    def p(self,k):
        if 'a' <= k <= 'z':
            return ord(k) - ord('a')
        elif 'A' <= k <= 'Z':
            return ord(k) - ord('A') + 26
        else:
            return ord(k) - ord('A')
        
    def hash_function(self, k):
        h=0
        for char in reversed(k):
            h = (h * self.z + self.p(char)) % self.capacity
        return h
        
    def second_hash_function(self, k):
        h = 0
        for char in reversed(k):
            h = (h * self.z1 + self.p(char)) % self.c
        r = self.c - h
        return r
        
    def insert(self, x):
        slot = self.hash_function(x)
        if self.collision_type == "Chain":
            if self.init_array[slot] is None:
                self.init_array[slot] = []
                self.init_array[slot].append(x)
                self.count +=1
            elif x not in self.init_array[slot]:
                self.init_array[slot].append(x)
                self.count +=1
                
        else:
            if self.count == len(self.init_array):
                raise Exception("Table is full")
            if self.init_array[slot] is None:
                self.init_array[slot] = x
                self.count+=1
            if self.init_array[slot] == x:
                        return
            elif self.init_array[slot] is not x:
                i=1
                if self.collision_type == "Linear":
                    while(i<self.capacity and self.init_array[slot]!=None):
                        slot = (slot + 1)%self.capacity
                        i+=1
                        if self.init_array[slot] is None:
                            self.init_array[slot] = x
                            self.count+=1
                            break
                        elif self.init_array[slot] == x:
                            break
                elif self.collision_type == "Double":
                    hashed_value2 = self.second_hash_function(x)
                    while(i<self.capacity and self.init_array[slot]!=None):
                        slot = (slot + hashed_value2)%self.capacity
                        i+=1
                        if self.init_array[slot] is None:
                            self.init_array[slot] = x
                            self.count+=1
                            break
                        elif self.init_array[slot] == x:
                           break

    def find(self, key):
        slot = self.hash_function(key)
        if self.collision_type == "Chain":
            if self.init_array[slot] is not None:
                for k in self.init_array[slot]:
                    if k == key:
                        return True
            return False
        else:
            i=1
            if self.init_array[slot] is None:
                return False
            elif self.init_array[slot]==key:
                return True
            elif self.collision_type == "Linear":
                    while i<=self.capacity and self.init_array[slot]!=None and self.init_array[slot]!=key:
                        slot = (slot + 1)%self.capacity
                        i+=1
                        if self.init_array[slot] is None:
                            return False
                        elif self.init_array[slot]==key:
                            return True
            elif self.collision_type == "Double":
                hashed_value2 = self.second_hash_function(key)
                if self.init_array[slot]==key:
                    return True
                elif self.init_array[slot] is None:
                    return False
                while i<=self.capacity and self.init_array[slot]!=None and self.init_array[slot]!=key:
                    slot = (slot + hashed_value2)%self.capacity
                    i+=1
                    if self.init_array[slot] is None:
                        return False
                    elif self.init_array[slot]==key:
                        return True
    
    def get_slot(self, key):
        hashed_value = self.hash_function(key)
        return hashed_value
    
    def get_load(self):
        return self.count/self.capacity
    
    def __str__(self):
        res = []
        for slot in self.init_array:
            if slot==None:
                res.append("<EMPTY>")
            elif self.collision_type=="Chain":
                res.append(" ; ".join(str(i) for i in slot))
            else:
                res.append(str(slot))
        a= " | ".join(res)
        return a

    
    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self):
        new_size = get_next_size()
        old = self.init_array
        self.init_array = [None]* new_size
        self.capacity = new_size
        self.count=0
        for slot in old:
            if slot != None:
                if self.collision_type=="Chain":
                    for y in slot:
                        self.insert(y)
                else:
                    self.insert(y)
            
                
            
    
# IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF, 
# YOU WOULD NOT NEED TO WRITE IT TWICE
    
class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
    
    def insert(self, key):
        super().insert(key)
    
    def find(self, key):
        slot = self.hash_function(key)
        if self.collision_type == "Chain":
            if self.init_array[slot] is not None:
                for k in self.init_array[slot]:
                    if k == key:
                        return True
            return False
        else:
            i=1
            if self.init_array[slot] is None:
                return False
            elif self.init_array[slot]==key:
                return True
            elif self.collision_type == "Linear":
                    while i<=self.capacity and self.init_array[slot]!=None and self.init_array[slot]!=key:
                        slot = (slot + 1)%self.capacity
                        i+=1
                        if self.init_array[slot] is None:
                            return False
                        if self.init_array[slot]==key:
                            return True
            elif self.collision_type == "Double":
                hashed_value2 = self.second_hash_function(key)
                if self.init_array[slot]==key:
                    return True
                elif self.init_array[slot] is None:
                    return False
                while i<=self.capacity and self.init_array[slot]!=None and self.init_array[slot]!=key:
                    slot = (slot + hashed_value2)%self.capacity
                    i+=1
                    if self.init_array[slot] is None:
                        return False
                    elif self.init_array[slot]==key:
                        return True
    
    def get_slot(self, key):
        super().get_slot(key)
    
    def get_load(self):
        return self.count/self.capacity
    
    def __str__(self):
        res = []
        for slot in self.init_array:
            if slot==None:
                res.append("<EMPTY>")
            elif self.collision_type=="Chain":
                res.append(" ; ".join(str(i) for i in slot))
            else:
                res.append(str(slot))
        a= " | ".join(res)
        return a


    
class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)

    
    def insert(self, x):
        key,value = x
        slot = self.hash_function(key)
        
    
        if self.collision_type == "Chain":
            if self.init_array[slot] is None:
                self.init_array[slot] = [(key, value)]
                self.count += 1
            else:
                for x in self.init_array[slot]:
                    if key == x[0]:
                        return
                self.init_array[slot].append((key,value))
                self.count+=1
        else:
                if self.count == len(self.init_array):
                    raise Exception("Table is full")
                i=1
                if self.collision_type == "Linear":
                    if self.init_array[slot] is None:
                        self.init_array[slot] = [(key,value)]
                        self.count+=1
                    elif self.init_array[slot][0][0] is not key:
                        i=1
                        while i < self.capacity:
                            slot=(slot + 1)%self.capacity
                            i+=1
                            if self.init_array[slot] is None:
                                self.init_array[slot] = [(key,value)]
                                self.count+=1
                                break
                            elif self.init_array[slot][0][0] is key:
                                break
                elif self.collision_type == "Double":
                    hashed_value2 = self.second_hash_function(key)
                    if self.init_array[slot] is None:
                        self.init_array[slot] = [(key,value)]
                        self.count+=1
                    elif self.init_array[slot][0][0] is not key:
                        i=1
                        while i<self.capacity:
                            slot = (slot + hashed_value2)%self.capacity
                            i+=1
                            if self.init_array[slot] is None:
                                self.init_array[slot] = [(key,value)]
                                self.count+=1
                                break
                            elif self.init_array[slot][0][0] is key:
                                break
        


        
    def find(self, key):
        slot = self.hash_function(key)
        if self.collision_type == "Chain":
            if self.init_array[slot] is not None:
                for k in self.init_array[slot]:
                    if k[0]==key:
                        return k[1]
            return None
        else:
                i=1
                if self.collision_type == "Linear":
                    if self.init_array[slot] is not None:
                        if self.init_array[slot][0][0] == key:
                            return self.init_array[slot][0][1]
                        elif self.init_array[slot][0][0] != key:
                            i=1
                            while i < self.capacity and self.init_array[slot] is not None:
                                slot=(slot + 1)%self.capacity
                                i+=1
                                if self.init_array[slot] is not None:
                                    if self.init_array[slot][0][0] == key:
                                        return self.init_array[slot][0][1]
                                    
                            return None
                elif self.collision_type == "Double":
                    hashed_value2 = self.second_hash_function(key)
                    if self.init_array[slot] is not None:
                        if self.init_array[slot][0][0] == key:
                            return self.init_array[slot][0][1]
                        elif self.init_array[slot][0][0] != key: 
                            i=1
                            while i<self.capacity and self.init_array[slot] is not None:
                                slot = (slot + hashed_value2)%self.capacity
                                i+=1
                                if self.init_array[slot] is not None:
                                    if self.init_array[slot][0][0] == key:
                                        return self.init_array[slot][0][1]
                            return None
        return None

    def get_slot2(self, key):
        slot = self.hash_function(key)
        if self.collision_type == "Chain":
                return slot
        else:
            i=1
            if self.init_array[slot] is None:
                return slot
            elif self.collision_type == "Linear":
                    if self.init_array[slot][0][0]==key:
                        return slot
                    while i<self.capacity and self.init_array[slot]!=None and self.init_array[slot][0][0]!=key:
                        slot = (slot + 1)%self.capacity
                        i+=1
                        if self.init_array[slot] is None:
                            return slot
                        if self.init_array[slot][0][0]==key:
                            return slot
            elif self.collision_type == "Double":
                hashed_value2 = self.second_hash_function(key)
                if self.init_array[slot][0][0]==key:
                        return slot
                while i<self.capacity and self.init_array[slot]!=None and self.init_array[slot][0][0]!=key:
                        slot = (slot + hashed_value2)%self.capacity
                        i+=1
                        if self.init_array[slot] is None:
                            return slot
                        elif self.init_array[slot][0][0]==key:
                            return slot
    def get_slot(self, key):
        super().get_slot(key)
    
    def get_load(self):
        return self.count/self.capacity
    
    def __str__(self):
        res = []
        for slot in self.init_array:
            if slot==None:
                res.append("<EMPTY>")
            elif self.collision_type=="Chain":
                res.append(" ; ".join(f"({i[0]}, {i[1]})" for i in slot))
            else:
                res.append(f"({slot[0][0]},{slot[0][1]})")
        return " | ".join(res)
    
