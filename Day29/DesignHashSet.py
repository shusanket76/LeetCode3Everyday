class Node:
    def __init__(self,val, next=None):
        self.value=val
        self.next=None
    

class MyHashSet:

    def __init__(self):
        self.max = 10**6
        self.array=[[] for x in range(self.max)]

        

    def add(self, key: int) -> None:

        index = key%self.max
        addin = self.array[index]
        contains= False
        if len(addin)==0:
            a = Node(key)
            addin.append(a)
            return
     
            
        else:
            b = addin[0]
            if b.value ==key:
                return 
            while b and b.next:
                if b.value==key:
                    contains = True
                    break
                    
                b=b.next
            if not contains and b.value!=key:
                b.next = Node(key)
          
    
        
        

    def remove(self, key: int) -> None:
        
        index = key%self.max
        addin = self.array[index]
        if len(addin)!=0:
            a = addin[0]
            
            dummy= Node(0)
            tail=dummy
            tail.next=a
    
        
            while a :
                
                if a.value==key:
                    tail.next=tail.next.next
                    
                    break
                else:
                    a=a.next
                    tail=tail.next
            self.array[index] = []  if dummy.next is None else [dummy.next]
        

    def contains(self, key: int) -> bool:
    
        index = key%self.max
        addin = self.array[index]
        if len(addin)!=0:
            a=addin[0]
            while a:
                if a.value==key:
                    return True
                a=a.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)