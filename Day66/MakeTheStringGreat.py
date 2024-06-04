from collections import deque
class Solution:
    def makeGood(self, s: str) -> str:
        stack = deque()
        for x in s:
            if len(stack)==0:
                stack.append(x)
            else:
                if stack[-1]!=x and (stack[-1]==x.lower() or stack[-1].lower()==x):
                    stack.pop()
                else:
                    stack.append(x)
        strr = ""
        for a in stack:
            strr+=a
        return strr