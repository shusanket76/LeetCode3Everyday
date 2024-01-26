from collections import deque
class Solution:
    def evalRPN(self, tokens) -> int:
        stack = deque()
        l = 0
        haset = set()
        haset.add("*")
        haset.add("/")
        haset.add("-")
        haset.add("+")
        
        while l<len(tokens):
            if tokens[l] in haset:
                num2=  int(stack.pop())
                num1 = int(stack.pop())
                if tokens[l]=="+":
                    stack.append(num1+num2)
                elif tokens[l]=="-":
                    stack.append(num1-num2)
                elif tokens[l]=="/":
                    stack.append(num1/num2)
                elif tokens[l]=="*":
                    stack.append(num1*num2)
            else:
                stack.append(tokens[l])
            l+=1
        print(stack)
        return int(stack[-1])

