class Solution:
    def pivotIndex(self, nums) -> int:
        sum1 = 0
        left=0
        for x in nums:
            sum1+=x
        for x in range(len(nums)):
            if x-1<0:
                left=0
            else:
                left+=nums[x-1]
            
            right = sum1-nums[x]-left
            if left==right:
                return x
        return -1

        