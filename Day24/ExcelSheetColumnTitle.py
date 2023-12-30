class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber>0:
            mod =(columnNumber-1)%26
            dig = 65+mod
            res+=chr(dig)
            columnNumber=(columnNumber-1)//26
        print(res)
        return res[::-1]
        
        
        