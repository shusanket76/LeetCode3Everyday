class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # insertion-sort
        for x in range(1, len(nums)):
            pivot = nums[x]
            j = x-1
            while j>=0 and nums[j]>pivot:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1] = pivot
        

