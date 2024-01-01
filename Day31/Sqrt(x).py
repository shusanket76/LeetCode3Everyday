import math
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = math.ceil(x/2)
        while l<=r:
            mid = math.ceil((l+r)/2)
            if mid*mid == x:
                return mid
            elif mid*mid<x:
                l=mid+1
            else:
                r=mid-1
        return r
        