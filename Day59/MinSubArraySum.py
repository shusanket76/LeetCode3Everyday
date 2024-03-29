class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        r = 0
        l = 0
        reslen = float("inf")
        wehave = 0
        while r < len(nums):
            wehave += nums[r]
            while wehave >= target:
                if (r - l + 1) < reslen:
                    reslen = r - l + 1
                wehave -= nums[l]
                l += 1
            r += 1

        if reslen == float("inf"):
            return 0
        return reslen
