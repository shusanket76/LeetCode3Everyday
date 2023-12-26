class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hasmap ={}
        hasmap2 = {}
        i = 0
        while i<len(s):
           
            if s[i] in hasmap and hasmap[s[i]]!=t[i]:
                return False
            if t[i] in hasmap2 and hasmap2[t[i]]!=s[i]:
                return False
            else:
              
                hasmap[s[i]]=t[i]
                hasmap2[t[i]]=s[i]
                i+=1
        return True

        