class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x<0:
            return False
        stack = []
        oldnum = x
        while x!=0:
            stack.append(x%10)
            x=x//10
        a=0
        newnum=0
        while len(stack)!=0:
            stacknum = stack.pop()
            newnum+=10**a*stacknum
            a+=1
        return newnum==oldnum
      
