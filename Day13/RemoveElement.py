class Solution:
    def removeElement(self, nums, val: int) -> int:
        a=0
        l=0
        r=len(nums)-1
        while l<=r:
            if nums[l]==val:
                nums.pop(l)
                r-=1
            else:
                l+=1
   