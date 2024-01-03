class Solution:
    def hasTrailingZeros(self, nums) -> bool:
        a=0
        for x in nums:
            if x%2==0:
                a+=1
            if a==2:
                return True
        return False