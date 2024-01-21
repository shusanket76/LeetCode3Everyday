class Solution:
    def permute(self, nums):

        def dfs(curr):
            res = []
            if len(curr)==1:
                return [curr[:]]
            
            for x in range(len(curr)):
                element = curr.pop(0)
                perms = dfs(curr)
                for y in perms:
                    y.append(element)
                    res.append(y[:])
                curr.append(element)
            return res[:]  
        return dfs(nums)          
        