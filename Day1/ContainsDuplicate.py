class Solution:
    def containsDuplicate(self, nums) -> bool:
        hasmap = {}
        for x in nums:
            if x in hasmap:
                return True
            else:
                hasmap[x] = True
        return False
        