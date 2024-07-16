from collections import deque
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        haset = []
        closehaset = []
        stack = deque()
        newstr = ""
        for x in range(len(s)):
            if s[x]=="(":
                haset.append(x)
            elif s[x]==")":
                if len(haset)!=0:
                    haset.pop()
                else:
                    closehaset.append(x)
        haset = set(haset)
        closehaset = set(closehaset)
        for x in range(len(s)):
            if x in haset or x in closehaset:
                continue
            newstr+=s[x]

        return (newstr)

        