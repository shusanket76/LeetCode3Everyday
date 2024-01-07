class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

    
        def dfs(tc, pos, hasmap={}):
            if pos in hasmap:
                return hasmap[pos]

            if pos>=len(cost):
                return 0
            
            hasmap[pos] = min(dfs(tc,pos+1, hasmap), dfs(tc,pos+2, hasmap))+cost[pos]
            return hasmap[pos]
            pass
        tc = 0
        return min(dfs(tc, 0), dfs(tc,1))
        