class Solution:
    def arraySign(self, nums) -> int:
        su=0
        for x in nums:
            if x==0:
                return 0
            if x<0:
                su+=1
        return 1 if su%2==0 else -1