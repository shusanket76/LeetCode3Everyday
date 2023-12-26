class Solution:
    def generate(self, numRows: int):
        row1 = [1]
        row2 =[1,1]
        res =[]
        res.append(row1)
        if numRows==1:
            return res
        res.append(row2)
        if numRows==2:
            return res
        for x in range(2, numRows):
            temp = [1]
            l=0
            r=1

            while r<len(res[x-1]):
                summ = res[x-1][l]+res[x-1][r]
                temp.append(summ)
                l+=1
                r+=1
            temp.append(1)
            res.append(temp)
        return res 

        