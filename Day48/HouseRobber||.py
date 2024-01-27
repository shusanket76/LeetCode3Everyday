class Solution:
    def rob(self, nums) -> int:
      
        def dfs(nums, total, hasmap):
            if tuple(nums) in hasmap:
                return hasmap[tuple(nums)]
             
            if len(nums)==0:
                return 0
            
            hasmap[tuple(nums[:])] =  max(dfs(nums[2:], total, hasmap)+nums[0], dfs(nums[1:], total, hasmap))
            return hasmap[tuple(nums)]
        if len(nums)==1:
            return nums[0]
        return max(dfs(nums[:len(nums)-1],0, hasmap = {}), dfs(nums[1:],0, hasmap = {}))
        