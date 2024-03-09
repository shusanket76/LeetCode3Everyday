class Solution:
    def minSwaps(self, s: str) -> int:
        res = 0
        leftpointer = 0
        rightpointer = len(s)-1
        hasmap = {"]":"["}
        closed = 0
        openbrack =0
        while leftpointer<rightpointer:
            if s[leftpointer] in hasmap:
                closed+=1
            else:
                openbrack+=1
            if closed>openbrack:
                while rightpointer>leftpointer and  s[rightpointer]  in hasmap:
                    rightpointer-=1
                openbrack+=1
                closed-=1
                res+=1
                rightpointer-=1
            leftpointer+=1
 
                    
        return res
                
            
        