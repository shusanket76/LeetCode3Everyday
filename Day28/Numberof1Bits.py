class Solution:
    def hammingWeight(self, n: int) -> int:
        res=1
        ans = 0
        while n!=0:
            ans+=res&n
            n=n>>1
        return ans
        