class Solution:
    def rob(self, nums) -> int:
        hasmap = {}
        def dfs(nums, total):
            if tuple(nums) in hasmap:
                return hasmap[tuple(nums)]
             
            if len(nums)==0:
                return 0
            
            hasmap[tuple(nums[:])] =  max(dfs(nums[2:], total)+nums[0], dfs(nums[1:], total))
            return hasmap[tuple(nums)]
            
        return dfs(nums,0)