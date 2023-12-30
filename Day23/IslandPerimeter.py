class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter=[0]
        def dfs(x,y,path):
            if (x,y) not in path:
                if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and grid[x][y]==1:
                    path.add((x,y))
                    a = dfs(x-1,y,path)
                    b = dfs(x+1,y,path)
                    c = dfs(x,y-1,path)
                    d = dfs(x,y+1,path)
                    alls = a+b+c+d
                    perimeter[0]+=alls
                    return 0
                else:
                    return 1

            else:
                return 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==1:
                    path=set()
                    dfs(x,y, path)
                    return perimeter[0]
        