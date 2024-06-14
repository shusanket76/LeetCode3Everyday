class Solution:
    def totalMoney(self, n: int) -> int:
        ts = 0
        prevmonday = 0
        day = 0
        temp = 0
        while day<n:
            if day%7==0:
                temp=prevmonday+1
                prevmonday+=1
                ts+=temp
            
            else:
                add = temp+1
                temp+=1
                ts+=add
       
            day+=1
        return ts


        