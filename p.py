def minCostClimbingStairs( cost) -> int:

    
        def dfs(tc, pos, hasmap={}):
            if pos in hasmap:
                return hasmap[pos]
            if pos>=len(cost):
                return tc
     
            hasmap[pos] = min(dfs(tc+cost[pos],pos+1, hasmap), dfs(tc+cost[pos],pos+2, hasmap))
            return hasmap[pos]
            pass
        tc = 0

        return min(dfs(tc, 0,{}), dfs(tc,1,{}))
a = minCostClimbingStairs([10,15,20])
print(a)