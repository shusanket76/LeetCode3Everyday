class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        hasmap = {}
        left = 0
        res = float("inf")
        for y in range(len(nums)):
            left+=nums[y]
            hasmap[left]=y
            if x-left==0:
                res  = min(res, y+1)
        right = 0
        for a in range(len(nums)-1, -1, -1):
            right+=nums[a]
            if x-right==0:
                res = min(res, len(nums)-a)
            if x-right in hasmap and hasmap[x-right]<a:
                res = min(res, len(nums)-a+hasmap[x-right]+1)
        if res == float("inf"):
            return -1
        return res
            
        