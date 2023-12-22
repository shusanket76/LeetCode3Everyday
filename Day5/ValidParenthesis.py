from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        hasmap = {"}":"{","]":"[",")":"("}
        stack = deque()
        for x in s:
            if x not in hasmap:
                stack.append(x)
            else:
                if len(stack)==0:
                    return False
                a = stack.pop()
                if hasmap[x]!=a:
                    return False
        return len(stack)==0
                
                