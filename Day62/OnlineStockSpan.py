class StockSpanner:

    def __init__(self):
        self.pricearray = []
        self.spanarray  = []
        

    def next(self, price: int) -> int:
        span = 1
        while self.pricearray and self.pricearray[-1]<=price:
            span+=self.spanarray[-1]
            self.pricearray.pop()
            self.spanarray.pop()
        self.pricearray.append(price)
        self.spanarray.append(span)
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)