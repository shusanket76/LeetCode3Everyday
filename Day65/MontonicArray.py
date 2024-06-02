class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        l = 0
        r = 1
        while r<len(nums):
            if nums[l]==nums[r]:
                l+=1
                r+=1
            elif nums[l]<nums[r]:
                while r<len(nums) and nums[l]<=nums[r]:
                    l+=1
                    r+=1
                if r==len(nums):
                    return True
                return False
            
            elif nums[l]>nums[r]:
                while r<len(nums) and nums[l]>=nums[r]:
                    l+=1
                    r+=1
                if r==len(nums):
                    return True
                return False
        return True
        