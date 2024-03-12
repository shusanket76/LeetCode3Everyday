class Solution:
    def generateParenthesis(self, n: int):
        res = []

        def dfs(curr,open,close):
            if open==close==n:
                res.append(curr[:])
                return 
            if open>n:
                return 
            if close>n:
                return 
            curr+="("
            dfs(curr, open+1, close)
            if open>close:
                curr= curr[0:len(curr)-1]
                curr+=")"
                dfs(curr, open, close+1)

        curr = ""
        dfs(curr,open=0,close=0)
        return res
        