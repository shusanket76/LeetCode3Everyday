class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def dfs(dots, pointer, curr):
            
            if (pointer == len(s)) and (dots==4):
                print(curr)
                res.append(curr[:-1][:])
                return 
            if dots>4:
                return 
            for x in range(pointer, min(pointer+3, len(s))):
                print(x, pointer)
                if (int(s[pointer:x+1])<=255) and(pointer==x or s[pointer]!="0"):
                    dfs(dots+1, x+1, curr+s[pointer:x+1]+".")
            
        

        dfs(0,0,"")
        return res



        