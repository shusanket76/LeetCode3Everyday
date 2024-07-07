from collections import deque
def minCost(colors: str, neededTime) -> int:
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
      
        print(res)
        return 1
a = minCost("abaac",[1,2,3,4,5])