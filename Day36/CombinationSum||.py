class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        res = []
        candidates.sort()

        def dfs(curr, pointer, target):
            if target==0:
                res.append(curr[:])
                return
            if target<0 or pointer>=len(candidates):
                return False
            curr.append(candidates[pointer])
            dfs(curr, pointer+1, target-candidates[pointer])
            curr.pop()
            while pointer<len(candidates)-1 and candidates[pointer]==candidates[pointer+1]:
                pointer+=1
            dfs(curr, pointer+1, target)
            
        dfs(curr=[], pointer=0, target=target)
        return res