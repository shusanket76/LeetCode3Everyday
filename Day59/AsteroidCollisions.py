from collections import deque


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        for x in asteroids:
            add = True
            if len(stack) == 0:
                stack.append(x)
            else:
                while len(stack) != 0 and x < 0 and stack[-1] > 0:
                    if abs(x) > stack[-1]:
                        stack.pop()
                        add = True
                    elif abs(x) < stack[-1]:
                        add = False
                        break
                    else:
                        add = False
                        stack.pop()
                        break
                if add:
                    stack.append(x)
        return stack
