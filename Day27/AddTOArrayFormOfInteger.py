class Solution:
    def addToArrayForm(self, num, k: int):
        carry = 0
        num.reverse()
        r= 0
        carry = 0
        while k:
            numtoadd = k%10
            if r>=len(num):
                num.append(numtoadd)
              
                
            else:
                num[r]+=numtoadd
            
            carry = num[r]//10
            
            num[r]=num[r]%10
            k=k//10
            k+=carry
            carry=0
            r+=1
        


        return num[::-1]
