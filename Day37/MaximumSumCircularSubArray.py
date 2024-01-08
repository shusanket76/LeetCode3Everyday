class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        globalmax, globalmin = nums[0], nums[0]
        currmax,currmin = 0,0
        r = 0
        total = 0
        while r<len(nums):
            total+=nums[r]
            currmin = min(currmin+nums[r], nums[r])
            currmax = max(currmax+nums[r], nums[r])
            globalmax = max(globalmax, currmax)
            globalmin = min(globalmin, currmin)
            r+=1
        print(total,globalmax,globalmin)
        return max(globalmax, total-globalmin) if globalmax>0 else globalmax
        