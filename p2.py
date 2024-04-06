from collections import deque


def dailyTemperatures(temperatures):
    res = [0 for x in temperatures]
    stack = deque()
    for x in range(len(temperatures)):
        if len(stack) == 0:
            stack.append(x)
        else:
            while len(stack) != 0 and temperatures[stack[-1]] < temperatures[x]:
                res[stack[-1]] = x-stack[-1]
                stack.pop()
            stack.append(x)
    return res

a = dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
print(a)
