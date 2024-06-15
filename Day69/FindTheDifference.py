class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hasmap = {}
        haset = set()
        for x in t:
            if x in hasmap:
                hasmap[x]+=1
                haset.add(x)
            else:
                hasmap[x]=1
                haset.add(x)
            
        for y in s:
            if y in hasmap:
                hasmap[y]-=1
                if hasmap[y]==0:
                    haset.remove(y)
        return haset.pop()