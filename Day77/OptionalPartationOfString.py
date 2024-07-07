class Solution:
    def partitionString(self, s: str) -> int:
        res = 1
        haset = set()
        r = 0
        while r<len(s):
            if s[r] in haset:
                res+=1
                haset = set()
                haset.add(s[r])
                r+=1
            else:
                haset.add(s[r])
                r+=1
        return (res)
        