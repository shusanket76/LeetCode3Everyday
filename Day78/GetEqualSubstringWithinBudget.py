class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = []
        for x in range(len(s)):
            val = abs(ord(s[x])-ord(t[x]))
            res.append(val)

        l = 0
        r = 0
        a = 0
        temp = 0
        while r<len(res):
            a+=res[r]
            while l<=r and a>maxCost:
                a-=res[l]
                l+=1
            temp = max(temp, r-l+1)
            r+=1
        return (temp)
        
