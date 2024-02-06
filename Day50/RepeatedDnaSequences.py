class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l = 0
        r = 0
        res = []
        hasmap = {}

        while r<=len(s)-1:
            while ((r-l+1)==10):
                hasmap[s[l:r+1]]=hasmap.get(s[l:r+1], 0)+1
                l+=1
            r+=1
        for a,b in hasmap.items():
            if b>=2:
                res.append(a)
        return res
