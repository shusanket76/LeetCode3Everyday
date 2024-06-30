class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        res = [0]


        def dfs(x,y, visit, count):
            if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and (x,y) not in visit and grid[x][y]>0:
                count+=grid[x][y]
                visit.add((x,y))
                res[0]=max(res[0], count)
                a = dfs(x+1,y, visit, count)
                b = dfs(x-1,y, visit, count)
                c = dfs(x,y+1, visit, count)
                d = dfs(x,y-1, visit, count)
                visit.remove((x,y))

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]>0:
                    dfs(x,y,set(), 0)
        return res[0]
        