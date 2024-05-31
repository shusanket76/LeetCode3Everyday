class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        hasmap = {}
        def dfs(amount):
            if amount in hasmap:
                if hasmap[amount] is None:
                    return None
                return hasmap[amount][:]
            if amount==0:
                return []
            if amount<0:
                return None
            fewest = None
            for x in coins:
                a = dfs(amount-x)
                if a is not None:
                    a.append(x)
                    if fewest is None or len(fewest)>len(a):
                        fewest = a[:]
            hasmap[amount] =  fewest
            if fewest is None:
                return None
            return hasmap[amount][:]
        a = dfs(amount)
        if a is None:
            return -1
        return len(a)