class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        l=0
        while l<len(flowerbed):
            if n==0:
                return True
            if flowerbed[l]==1:
                l+=1
                continue
            before = l-1
            if before>=0:
                if flowerbed[before]==1:
                    l+=1
                    continue
            after = l+1
            if after<len(flowerbed):
                if flowerbed[after]==1:
                    l+=1
                    continue
            flowerbed[l]=1
            l+=1
            n-=1
            if n==0:
                return True
        return False
