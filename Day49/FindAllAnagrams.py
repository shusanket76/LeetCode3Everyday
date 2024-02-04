class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        hasmap1 = {}
        hasmap2 = {}
        tempres=0
        for x in p:
            hasmap1[x] = hasmap1.get(x,0)+1
            hasmap2[x] = hasmap2.get(x,0)+0
        l = 0
        r = 0
        while r<len(s):
            while (r-l+1>len(p)):
                if s[l] in hasmap1:
                    hasmap2[s[l]]-=1
                    if hasmap2[s[l]]<hasmap1[s[l]]:
                        tempres-=1
                    l+=1
                else:
                    l+=1
            if s[r] in hasmap1:
                hasmap2[s[r]]+=1
                if  hasmap2[s[r]]<=hasmap1[s[r]]:
                    tempres+=1
                    if tempres==len(p):
                        res.append(l)
                r+=1
            else:
                r+=1
        return res
            
        