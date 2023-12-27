
class Solution:
    def calPoints(self, operations) -> int:
        stack = []
        for x in operations:
            if x=="C":
                stack.pop()
            elif x=="D":
                num = stack[-1]
                num = num*2
                stack.append(num)
            elif x=="+":
                nu1 = stack[-1]
                nu2=stack[-2]
                ad = nu1+nu2
                stack.append(ad)

            else:
                nu = int(x)
                stack.append(nu)
        su=0
        for y in stack: 
            su+=y
        return su