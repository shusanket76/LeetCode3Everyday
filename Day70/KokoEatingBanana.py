import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l<=r:
            mid = int(l+r)//2
            temp = 0
            for x in piles:
                temp+=math.ceil(x/mid)
            if temp>h:
                l=mid+1
            elif temp<=h:
                res = min(res, mid)
                r=mid-1
        return res