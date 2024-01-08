class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        res = 0
        finalres = float("-inf")
        while r<=len(nums)-1:
            res+=nums[r]
            finalres = max(finalres, res)
            while res<0:
              
                res-=nums[l]
                l+=1
            r+=1
        return finalres
# ================================================
# 2nd Solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r = 0
        res = 0
        finalres = nums[-1]
        while r<len(nums):
            res = max(res+nums[r], nums[r])
            finalres = max(finalres, res)
            r+=1
        return finalres
        