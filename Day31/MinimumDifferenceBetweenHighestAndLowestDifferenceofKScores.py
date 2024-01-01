from collections import deque
class Solution:
    def minimumDifference(self, nums, k: int) -> int:
        # minqueue = deque()
        # maxqueue = deque()
        nums.sort()
        l=0
        r=k-1
        res = float("inf")
        while r<len(nums):
            res = min(res, nums[r]-nums[l])
            l+=1
            r+=1
        return res
            

        