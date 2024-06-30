class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        hasmap = {}
        hasmap2 = {}
        res = []
        for x in range(len(graph)):
            hasmap[x] = graph[x]
        def dfs(start, visit):
            if start in hasmap2:
                return hasmap2[start]
            hasmap2[start]=False
            for x in hasmap[start]:
                a = dfs(x, visit)
                if a is False:
                    
                    return False
            hasmap2[start] = True
            return True
        

        for x in hasmap:
                if dfs(x, visit= set()) is True:
                    res.append(x)
        return res
        