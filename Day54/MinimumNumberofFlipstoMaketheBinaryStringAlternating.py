class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s=s+s
        alt1, alt2 = "", ""
        for x in range(len(s)):
            alt1+= "0" if x%2 else "1"
            alt2 += "1" if x%2 else "0"
        r = 0 
        res = float("inf")
        l = 0
        diff1 = 0
        diff2 = 0
        while r<len(s):
            if s[r]!=alt1[r]:
                diff1+=1
            if s[r]!=alt2[r]:
                diff2+=1
            if (r-l+1)>n:
                if s[l]!=alt1[l]:
                    diff1-=1
                if s[l]!=alt2[l]:
                    diff2-=1
                l+=1
            if (r-l+1)==n:
                res = min(res,diff1, diff2)
            r+=1
        return res