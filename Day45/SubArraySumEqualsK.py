class Solution:
    def subarraySum(self, nums, k: int) -> int:
        hasmap = {0:1}
        temp=0
        res =0
        for x in nums:
            temp+=x
            wehave = temp-k
            if wehave in hasmap:
                res+=hasmap[wehave]
            hasmap[temp]=hasmap.get(temp,0)+1
        return res