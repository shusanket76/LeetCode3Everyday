class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        slist = s.split(" ")
        if len(slist)!=len(pattern):
            return False
        hasmap1 = {}
        hasmap2 = {}
        for x in range(len(pattern)):
            if pattern[x] in hasmap1:
                if hasmap1[pattern[x]]!=slist[x]:
                    return False
            else:
                hasmap1[pattern[x]] = slist[x]
            
            if slist[x] in hasmap2:
                if hasmap2[slist[x]]!=pattern[x]:
                    return False
            else:
                hasmap2[slist[x]] = pattern[x]
        return True