class Solution:
    def combinationSum(self, candidates, target):
        res=[]
        def dfs(curr, target, counter):
            if target ==0:
                res.append(curr[:])
                return 
            if target<0 or counter==len(candidates):
                return 
            curr.append(candidates[counter])
            dfs(curr,target-candidates[counter], counter)
            curr.pop()
            dfs(curr, target, counter+1)

        dfs([],target, 0)
        return res