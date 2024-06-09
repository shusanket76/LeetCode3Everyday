class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currmin = 1
        currmax = 1
        for x in nums:
            if x ==0:
                currmax = 1
                currmin = 1
                
            temp  = currmax
            currmax = max(currmax*x, currmin*x, x)
            currmin = min(temp*x, currmin*x, x)
            res = max(res, currmax)
        return res

        