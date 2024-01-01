class Node:
    
    def __init__(self, key=None,value=None, next=None):
        self.key=key
        self.value = value
        self.next = next


class MyHashMap:

    def __init__(self):
        self.max = 1000
        self.array = [Node() for x in range(1000)]
        

    def put(self, key: int, value: int) -> None:
        
        index = key%self.max
        curr = self.array[index]
        
        while curr.next:
            if curr.next.key==key:
                    curr.next.value = value
                    return
            curr=curr.next
                
                
                
                
        curr.next = Node(key,value)
        

        

    def get(self, key: int) -> int:
      
        index = key%self.max
        curr = self.array[index]

        while curr.next:
            if curr.next.key==key:
                    return curr.next.value
            curr=curr.next
        
        return -1
            


        

    def remove(self, key: int) -> None:
    
        index = key%self.max
        curr = self.array[index]
            
        while curr.next:
            if curr.next.key==key:
                    curr.next=curr.next.next
                    break
            curr=curr.next
            
  
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)