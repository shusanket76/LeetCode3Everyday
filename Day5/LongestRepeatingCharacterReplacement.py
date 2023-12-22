class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hasmap = {}
        result = 0
        a = 0
        b = 0
        while b<=len(s)-1:
            hasmap[s[b]]=hasmap.get(s[b],0)+1
            while len(hasmap)!=0 and ((b-a+1-max(hasmap.values())>k)):
                hasmap[s[a]] = hasmap.get(s[a],0)-1
                a+=1
            result = max(result, b-a+1)
            b+=1
        return result
        