class Solution:
    def canJump(self, nums) -> bool:
        r = len(nums)-1
        l = len(nums)-1
        while r>=0:
            dis = (l-r)
            if nums[r]>=dis:
                dis = 0
                l=r
            r-=1
        return dis==0



        