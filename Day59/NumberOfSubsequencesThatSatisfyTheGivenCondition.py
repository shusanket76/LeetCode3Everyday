class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        r = len(nums) - 1
        mod = 10**9 + 7
        res = 0
        for i, leftval in enumerate(nums):
            while (leftval + nums[r]) > target and i <= r:
                r -= 1

            if i <= r:
                res += 2 ** (r - i)
                res %= mod
        return res
