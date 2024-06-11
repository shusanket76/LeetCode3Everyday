from collections import deque
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = deque()
        far = 0
        queue.append(0)
        while queue:
            node = queue.popleft()
            start = max(node+minJump, far+1)
            for j in range(start, min(maxJump+node+1, len(s))):
                if j==len(s)-1 and s[j]=="0":
                    return True
                if s[j]=="0":
                    queue.append(j)
            far = maxJump+node
        return False