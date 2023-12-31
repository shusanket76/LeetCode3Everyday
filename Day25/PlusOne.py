class Solution:
    def plusOne(self, digits):
        x=len(digits)-1
        carry=0
        while x>=0:
            num = digits[x]
            if x==len(digits)-1:
                num+=1+carry
            else:
                num+=carry
            if num>=10:
                carry = num//10
                digits[x]=num%10
                x-=1
                
            else:
                digits[x]=num
                return digits
        if carry!=0:
            digits.insert(0, carry)
        return digits
        