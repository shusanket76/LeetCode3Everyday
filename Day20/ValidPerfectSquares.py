
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = int(num/2)+1
        while l<=r:
            mid = int((l+r)/2)
            if mid*mid==num:
                return True
            elif mid*mid>=num:
                r=mid-1
            else:
                l=mid+1
        return False

        