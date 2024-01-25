class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        inset = set()
        hasmap = {}
        for x in range(len(s)):
            if s[x] in hasmap:
                hasmap[s[x]][1] = x
            else:
                hasmap[s[x]] =[x, float("-inf")]
        for y in hasmap.values():
            if y[1]!=float("-inf"):
                for z in range(y[0]+1, y[1]):
                    if s[z] in inset:
                        continue
                    inset.add(s[z])
                    res+=1
                inset = set()
    

        return res
        