class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hasmap = {}
        for x in s:
            hasmap[x] = hasmap.get(x,0)+1
        for y in t:
            hasmap[y] = hasmap.get(y,0)-1
        return min(hasmap.values())==max(hasmap.values())==0

