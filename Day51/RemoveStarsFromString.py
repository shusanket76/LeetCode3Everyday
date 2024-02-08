class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for x in s:
            if x=="*":
                if len(stack)!=0:
                    stack.pop()
            else:
                stack.append(x)
        res = ""
        for a in stack:
            res+=a
        return res