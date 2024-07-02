import math
class Solution:
    def minimizeArrayValue(self, nums) -> int:
        ts = 0 
        r = 0
        res = [nums[0]]
        while r<len(nums):
            ts+=nums[r]
            avg = math.ceil(ts/(r+1))
            if avg>res[0]:
                res[0]=avg
            r+=1
        return res[0]
        