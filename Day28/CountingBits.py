class Solution:
    def countBits(self, n: int):
        res = []
        for x in range(n+1):
            one =1
            temp=0
            while x!=0:
                temp+=one&x
                x=x>>1
            res.append(temp)
        return res