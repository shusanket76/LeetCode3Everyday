from collections import deque
class StockSpanner:

    def __init__(self):
        
        self.pointerarray = []
        self.pricearray = []
        self.pointer = 0
        self.res = []

    def next(self, price: int) -> int:
        if len(self.pointerarray)==0:
            self.pointerarray.append(self.pointer)
            self.pricearray.append(price)
            self.res.append(1)
            self.pointer+=1
          
        else:
            while self.pricearray[self.pointerarray[-1]]<price:
                self.pricearray.pop()
                self.pointerarray.pop()
            self.res.append(self.pointer-self.pointerarray[-1])
            self.pointerarray.append(self.pointer)
            self.pricearray.append(price)
            self.pointer+=1
        print(self.res)
        return self.res
            