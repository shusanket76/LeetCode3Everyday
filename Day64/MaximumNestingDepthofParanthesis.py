
class Solution:
    def maxDepth(self, s: str) -> int:
        hasmap = {"(":"open", ")":"close"}
        maxp = 0
        finalres = 0
        for x in s:
            if x in s:
                if x in hasmap:
                    if hasmap[x]=="open":
                        maxp+=1
                        finalres = max(finalres, maxp)
                    else:
                        maxp-=1
        return finalres
        