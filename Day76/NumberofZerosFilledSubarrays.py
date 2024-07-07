class Solution:
    def zeroFilledSubarray(self, nums) -> int:
        res = 0
        temp = 0
        r = 0
        while r<len(nums):
            count = 1
            while r<len(nums) and nums[r]==0:
                temp+=count
                count+=1
                r+=1

            if temp!=0:
                res+=temp
                temp = 0
                
            else:
                r+=1
        return (res)