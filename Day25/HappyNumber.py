class Solution:
    def isHappy(self, n: int) -> bool:
        hasmap = {}
        while n!=1:
            if n in hasmap:
                return False
            hasmap[n]= True
            x = str(n)
            newn = 0
            for a in x:
                newn+=(int)(a)**2
            n=newn
        return True

        