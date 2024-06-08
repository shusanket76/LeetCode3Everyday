class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        ts = 0
        for x in matchsticks:
            ts+=x
        target = 0
        if ts%4==0:
            target = ts/4
        else:
            return False   
        sides = [0 for x in range(4)]
        matchsticks.sort(reverse = True)
        def dfs(i):
            if i==len(matchsticks):
                return True
            for j in range(4):
                if sides[j]+matchsticks[i]<=target:
                    sides[j]+=matchsticks[i]
                    if dfs(i+1) is True:
                        return True
                    sides[j]-=matchsticks[i]
            return False
        return dfs(0)
           
        