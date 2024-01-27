class Solution:
    def pacificAtlantic(self, heights):
        pacificset  = set()
        atlanticset = set()

        def dfs(a,b, haset, prev):
            if a>=0 and b>=0 and a<len(heights) and b<len(heights[0]) and (a,b) not in haset and prev<=heights[a][b]:
                haset.add((a,b))
                dfs(a+1,b,haset, heights[a][b])
                dfs(a,b+1,haset, heights[a][b])
                dfs(a-1,b,haset, heights[a][b])
                dfs(a,b-1,haset, heights[a][b])

        
        
        # for PACIFIC
        # top and bottom
        prev = -1
        for x in range(len(heights[0])):
            
            dfs(0,x, pacificset, prev)
            dfs(len(heights)-1,x,atlanticset, prev)

        # left and right
        for y in range(len(heights)):
            dfs(y,0, pacificset, prev)
            dfs(y, len(heights[0])-1,atlanticset, prev )
        
        res = []
        for d in pacificset:
            if d in atlanticset:
                res.append(d)
        return res