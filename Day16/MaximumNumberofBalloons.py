class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hasmap={"b":0,"a":0,"l":-1,"o":0,"n":0}
        for x in text:
            if x in hasmap:
                hasmap[x] = hasmap[x]+1
        if hasmap["l"]==0:
            return 0
        return min(hasmap.values())
        