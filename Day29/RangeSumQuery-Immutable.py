class NumArray:

    def __init__(self, nums):
        self.totalsum= 0
        for x in nums:
            self.totalsum+=x
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        l=0
        r=len(self.nums)-1
        tempsum = self.totalsum
        while l!=left:
            tempsum-=self.nums[l]
            l+=1
        while r!=right:
            tempsum-=self.nums[r]
            r-=1
        return tempsum


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)