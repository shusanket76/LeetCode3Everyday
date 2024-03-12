from collections import deque
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = deque()
        poppedpointer = 0
        for x in pushed:
            stack.append(x)
            while stack and  stack[-1] == popped[poppedpointer]:
                stack.pop()
                poppedpointer+=1
        return poppedpointer==len(popped)
