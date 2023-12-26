class Solution:
    def numIslands(self, grid) -> int:
        path=set()
        count = 0
        def dfs(x,y):
            if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and (x,y) not in path and grid[x][y]=="1":
                path.add((x,y))
                dfs(x-1,y)
                dfs(x+1,y)
                dfs(x,y-1)
                dfs(x,y+1)
                return True

                
            else:
                return False
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]=="1":
                    if dfs(x,y) is True:
                        count+=1
        return count
        