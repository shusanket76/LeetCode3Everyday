class Solution:
    def findDuplicates(self, nums):
        res = []
        for x in range(len(nums)):
            if nums[abs(nums[x])-1]<0:
                res.append(abs(nums[x]))
            else:
                a = nums[abs(nums[x])-1]
                nums[abs(nums[x])-1] = -a
        return res