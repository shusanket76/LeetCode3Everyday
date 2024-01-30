class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for y in range(len(nums)):
            for x in range(len(nums)-1-y):
                a = str(nums[x])+str(nums[x+1])
                b = str(nums[x+1])+str(nums[x])
                if int(a)<int(b):
                    nums[x],nums[x+1]=nums[x+1], nums[x]
        res = ""
        for a in nums:
            res+=str(a)
        if int(res)==0:
            return "0"
        return res

        