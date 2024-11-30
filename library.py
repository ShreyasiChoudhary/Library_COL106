import hash_table as ht
from hash_table import HashMap
from hash_table import HashSet
from hash_table import HashTable

class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    
class MuskLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, book_titles, texts):
        combo=[]
        for i in range(len(book_titles)):
            combo.append((book_titles[i],texts[i]))
        
        self.merge_sort1(combo)
        self.book_title = []
        self.text =[]
        self.books=[]
        for i in range(len(book_titles)):
            self.book_title.append(combo[i][0])
            self.text.append(combo[i][1])
        for i in range(len(self.text)):
            self.text[i]=self.merge_sort(self.text[i])
        for text in self.text:
            unique_words=[]
            for i in range(len(text)):
                if i==0:
                    unique_words.append(text[i])
                elif unique_words[-1]!=text[i]:
                    unique_words.append(text[i])
            text.clear()
            text.extend(unique_words)
        for i in range(len(book_titles)):
            self.books.append((self.book_title[i],self.text[i]))
        

    def merge_sort(self,words):
        if len(words) <= 1:
            return words
        mid = len(words) // 2
        left_half = self.merge_sort(words[:mid])
        right_half = self.merge_sort(words[mid:])
        return self.merge(left_half, right_half)

    def merge(self,left, right):
        sorted_list = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1
        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        
        return sorted_list
    def merge1(self,s1,s2,s):
        i=j=k=0
        while i<len(s1) and j<len(s2):
            if s1[i][0] < s2[j][0]:
                s[k]=s1[i]
                i+=1
            else:
                s[k]=s2[j]
                j+=1
            k+=1
        while i<len(s1):
            s[k]=s1[i]
            i+=1
            k+=1
        while j<len(s2):
            s[k]=s2[j]
            j+=1
            k+=1
    
    def merge_sort1(self,s):
        n=len(s)
        if n<2: return
        s1=s[0:n//2]
        s2=s[n//2:n]
        self.merge_sort1(s1)
        self.merge_sort1(s2)
        self.merge1(s1,s2,s)
    

        
    def binary_search(self,array,left,right,key):
        while left<= right:
            mid = (left + right)//2
            if array[mid][0]== key:
                return mid
            elif array[mid][0]<key:
                left = mid + 1
            else:
                right = mid -1
        return -1
        
    def binary_search1(self,array,left,right,key):
        while left<= right:
            mid = (left + right)//2
            if array[mid] == key:
                return mid
            elif array[mid]<key:
                left = mid + 1
            else:
                right = mid -1
        return -1
        
            
    def distinct_words(self, book_title):
        x = self.binary_search(self.books,0,len(self.books)-1, book_title)
        result =[]
        for word in self.books[x][1]:
            result.append(word)
        return result
    
    def count_distinct_words(self, book_title):
        x = self.binary_search(self.books,0,len(self.books)-1, book_title)
        return len(self.books[x][1])
    
    def search_keyword(self, keyword):
        result=[]
        for book in self.books:
            y = self.binary_search1(book[1],0, len(book[1])-1, keyword)
            if y != -1:
                result.append(book[0])
        return result
    
    def print_books(self):
        for book in self.books:
            Name = book[0] 
            words = book[1] 
            print(f"{Name}: {' | '.join(words)}")

class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
        '''
        name    : "Jobs", "Gates" or "Bezos"
        params  : Parameters needed for the Hash Table:
            z is the parameter for polynomial accumulation hash
            Use (mod table_size) for compression function
            
            Jobs    -> (z, initial_table_size)
            Gates   -> (z, initial_table_size)
            Bezos   -> (z1, z2, c2, initial_table_size)
                z1 for first hash function
                z2 for second hash function (step size)
                Compression function for second hash: mod c2
        '''

        self.name = name
        self.book=[]
        self.params = params
        if self.name=="Jobs":
            self.books = HashMap("Chain", self.params)
        elif self.name=="Gates":
            self.books = HashMap("Linear", self.params)
        else:
            self.books = HashMap("Double", self.params)
    
    def add_book(self, book_title, text):

        if (self.name == "Jobs"):
            self.Hash = HashSet("Chain", self.params)
        elif (self.name == "Gates"):
            self.Hash = HashSet("Linear", self.params)
        elif(self.name == "Bezos"):
            self.Hash = HashSet("Double", self.params)
        for word in text:
            self.Hash.insert(word)
        self.books.insert((book_title,self.Hash))
        if self.books.get_slot2(book_title) not in self.book:
            self.book.append(self.books.get_slot2(book_title))




        
    def distinct_words(self, book_title):
        result = []
        z = self.books.get_slot2(book_title)
        if self.books.collision_type == "Chain":
            for k in self.books.init_array[z]:
                if k[0] == book_title:
                    for i in k[1].init_array:
                        if i is not None:
                            for s in i:
                                result.append(s)
        else:
            x = self.books.init_array[z][0][1].init_array
            result = []
            for y in x:
                if y is not None:
                    result.append(y)
        return result
        
        
    def count_distinct_words(self, book_title):
        z = self.books.get_slot2(book_title)
        if self.books.collision_type == "Chain":
            for k in self.books.init_array[z]:
                if k[0] == book_title:
                    return k[1].count
        else:
            x = self.books.init_array[z][0][1].count
            return x
    
    def search_keyword(self, keyword):
        result = []
        for book_title in self.book:
            book_hash_list = self.books.init_array[book_title]
            if self.books.collision_type == "Chain":
                    for books in book_hash_list:
                        slot = books[1].hash_function(keyword)
                        if books[1].init_array[slot] is not None:
                            for x in books[1].init_array[slot]:
                                if x==keyword:
                                    result.append(books[0])
                    

            else:
                book_hash_set = self.books.init_array[book_title][0][1]
                slot = book_hash_set.hash_function(keyword)
                if book_hash_set.init_array[slot] == keyword:
                    result.append(self.books.init_array[book_title][0][0])
                elif book_hash_set.init_array[slot] is not None:
                    i=1
                    if book_hash_set.collision_type == "Linear":
                        while(i<book_hash_set.capacity and book_hash_set.init_array[slot]!= None):
                            slot = (slot + 1)%book_hash_set.capacity
                            i+=1
                            if book_hash_set.init_array[slot] == keyword:
                                result.append(self.books.init_array[book_title][0][0])
                                break
                    elif book_hash_set.collision_type == "Double":
                            hashed_value2 = book_hash_set.second_hash_function(keyword)
                            while(i<book_hash_set.capacity and book_hash_set.init_array[slot]!= None):
                                slot = (slot + hashed_value2)%book_hash_set.capacity
                                i+=1
                                if book_hash_set.init_array[slot]==keyword:
                                    result.append(self.books.init_array[book_title][0][0])
                                    break
        return result
    

    
    def print_books(self):
        if self.books.collision_type == "Chain":
            for book_title in self.book:
                book_hash_list = self.books.init_array[book_title]
                for books in book_hash_list:
                    Name = books[0]
                    print(f"{Name}: ", end="") 
                    res=[]
                    for j in range(len(books[1].init_array)):
                        if books[1].init_array[j] is not None:
                            res.append(" ; ".join(str(word) for word in books[1].init_array[j]))
                        else:
                            res.append("<EMPTY>")
                    print (" | ".join(res))

        else:

            for book in self.book:
                Name = self.books.init_array[book][0][0]
                print(f"{Name}: ", end="")
                res = []
                for j in range(len(self.books.init_array[book][0][1].init_array)):
                    if self.books.init_array[book][0][1].init_array[j] is not None:
                        res.append(str(self.books.init_array[book][0][1].init_array[j]))
                    else:
                        res.append("<EMPTY>")
                print (" | ".join(res))

