class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0 
        r= n
        while l<=r:
            mid = int((l+r)/2)
            requiredcoins = (1/2)*mid*(mid+1)
            if requiredcoins<=n:
                l=mid+1
            else:
                r=mid-1
       
        return r

        