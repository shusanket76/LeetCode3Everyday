from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for x in temperatures]
        stack = deque()
        for x in range(len(temperatures)):
            if len(stack) == 0:
                stack.append(x)
            else:
                while len(stack) != 0 and temperatures[stack[-1]] < temperatures[x]:
                    res[stack[-1]] = x - stack[-1]
                    stack.pop()
                stack.append(x)
        return res
