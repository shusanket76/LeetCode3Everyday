class Solution:
    def countSubIslands(self, grid1, grid2) -> int:
        res = 0
        path=set()
        def dfs(x,y,path):
            if x>=0 and y>=0 and x<len(grid2) and y<len(grid2[0]) and (x,y) not in path and grid2[x][y]==1:
                if grid1[x][y]!=1:
                    return False
                path.add((x,y))
                a = dfs(x-1,y,path)
                b = dfs(x+1,y,path)
                c = dfs(x,y-1,path)
                d = dfs(x,y+1,path)
                return (a and b and c and d)
            return True
            

        for x in range(len(grid2)):
            for y in range(len(grid2[0])):
                if grid2[x][y]==1 and (x,y) not in path:
                    if dfs(x,y,path) is True:
                        res+=1
        return res


        