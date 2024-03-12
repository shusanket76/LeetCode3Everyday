class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = [0 for x in nums]
        mid = len(nums)//2
        l = 0
        i = 0
        while i<len(nums) and l<=mid:
            res[i]=nums[l]
            l+=1
            i+=2
        i = 1
        r = len(nums)-1
        while i<len(nums) and r>=mid:
            res[i]=nums[r]
            r-=1
            i+=2
        return res
        