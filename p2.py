import math
# print(math.ceil(3/3))
def minEatingSpeed(piles, h: int) -> int:
        l = 1
        r = max(piles)
        while l<=r:
            mid = int(l+r)//2
            temp = 0
            for x in piles:
                temp+=math.ceil(x/mid)
            if temp>h:
                r=mid-1
            else:
                l=mid+1
        return r


a = minEatingSpeed(piles = [3,6,7,11], h = 8)

