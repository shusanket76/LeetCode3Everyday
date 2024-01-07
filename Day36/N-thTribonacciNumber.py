class Solution:
    
    def tribonacci(self, n: int, hasmap = {}) -> int:
        if n in hasmap:
            return hasmap[n]
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        hasmap[n] = self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
        return hasmap[n]