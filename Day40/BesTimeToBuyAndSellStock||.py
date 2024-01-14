class Solution:
    def maxProfit(self, prices) -> int:
        l = 0
        r = 1
        res = 0
        while r<len(prices):
            if prices[l]>prices[r]:
                r+=1
                l+=1
            else:
                buy = prices[l]
                temp=0
                while r<len(prices) and prices[r-1]<prices[r]:
                    temp = max(temp, prices[r]-buy)
                    r+=1
                res+=temp
                l=r
                r+=1
        return res


        