class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = [0]
        path=set()
        def dfs(x,y, path):
            if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and (x,y) not in path and grid[x][y]==1:
                path.add((x,y))
     
              
                a=dfs(x-1,y,path)
                b=dfs(x+1,y,path)
                c = dfs(x,y-1,path)
                d= dfs(x,y+1,path)
                return 1+a+b+c+d
            return 0
                
                
            
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==1 and (x,y) not in path:
                    
                    res[0] = max(res[0],dfs(x,y, path))
        return res[0]
        
