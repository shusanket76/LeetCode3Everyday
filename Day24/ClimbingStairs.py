class Solution:
    
    def climbStairs(self, n: int, hasmap={}) -> int:
        if n in hasmap:
            return hasmap[n]
        if n<=1:
            return 1
        hasmap[n]= self.climbStairs(n-1, hasmap)+self.climbStairs(n-2, hasmap)
        return hasmap[n]