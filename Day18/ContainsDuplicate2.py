from collections import deque
class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        queue = deque()
        l = 0
        r = 0
        while r<len(nums):
            while (r-l)>k:
                queue.popleft()
                l+=1
            if nums[r] in queue:
                return True
            queue.append(nums[r])
            r+=1
        return False
            

        