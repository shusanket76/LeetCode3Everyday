from collections import deque
class MyStack:

    def __init__(self):
        self.queue1 = deque()
        
        

    def push(self, x: int) -> None:
        self.queue1.append(x)

        

    def pop(self) -> int:
        qlen = len(self.queue1)
        for x in range(qlen):
            top = self.queue1.popleft()
            if x!=qlen-1:
                self.queue1.append(top)
        return top
        

    def top(self) -> int:
        for x in self.queue1:
            top = x
        return top
        

    def empty(self) -> bool:
        return len(self.queue1)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()