from collections import deque
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        stack = deque()
        res = 0
        for x in range(len(colors)):
            if len(stack)==0:
                stack.append(x)
            else:
                if colors[stack[-1]]==colors[x]:
                    if neededTime[stack[-1]]<neededTime[x]:
                        res+=neededTime[stack[-1]]
                        stack.pop()
                        stack.append(x)
                        
                        
                    else:
                        res+=neededTime[x]
                else:
                    stack.append(x)
      
        return (res)
        
