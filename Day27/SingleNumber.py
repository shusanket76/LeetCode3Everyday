class Solution:
    def singleNumber(self, nums) -> int:
        res = 0
        for a in nums:
            res^=a
        return res
        