class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [x for x in range(len(nums)+1)]
        res = 0
        for y in nums:
            res^=y
        for z in arr:
            res^=z
        return res