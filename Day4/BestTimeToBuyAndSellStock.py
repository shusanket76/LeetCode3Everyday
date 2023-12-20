class Solution:
    def maxProfit(self, prices) -> int:
        first = 0
        res = 0
        second = first+1
        while second<len(prices):
            if prices[first]<prices[second]:
                res = max(res, prices[second]-prices[first])
                second+=1
            else:
                first=second
                second=first+1
        return res