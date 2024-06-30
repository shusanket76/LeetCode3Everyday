from collections import deque
def shortestBridge(grid) -> int:
        set1 = set()
        set2 = set()

        def dfs1(x,y):
            if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and (x,y) not in set1 and grid[x][y]==1:
                set1.add((x,y))
                a = dfs1(x+1, y)
                b = dfs1(x-1, y)
                c = dfs1(x, y+1)
                d = dfs1(x, y-1)
        def bfs(x,y, coun):
            queue = deque()
            queue.append((x,y, coun))
            while queue:
                q = len(queue)
                for x in range(q):
                    (a,b, coun) = queue.popleft()
                    if (a,b) in set1:
                        return coun
                    dir = [(1,0), (0,1), (-1,0), (0,-1)]
                    for d in dir:
                        r = a+d[0]
                        c = b+d[1]
                        if r>=0 and c>=0 and r<len(grid) and c<len(grid[0]) and (r,c) not in set2:
                            queue.append((r,c, coun+1))

                        


        # def dfs2(x,y):
        #     if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and (x,y) not in set2:
        #         if (x,y) in set1:
        #             return 0
        #         set2.add((x,y))
        #         shortestpath = None
        #         dir = [(1,0), (0,1), (-1,0), (0,-1)]
        #         for d in dir:
        #             r = x+d[0]
        #             c = y+d[1]
        #             count = dfs2(r,c)
        #             if count is not None:
        #                 if shortestpath==None or shortestpath>count:
        #                     shortestpath = count
        #                     if grid[x][y]!=1:
        #                         shortestpath+=1
        #         set2.remove((x,y))
        #         return shortestpath
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==1:
                    if (x,y) not in set1:
                        if len(set1)==0:
                        # first
                            dfs1(x,y)
                    
                        else:
                            print("ds")
                            return (bfs(x,y,coun=0))-1


a = shortestBridge(grid = [[1,0,1,1,1,0],[0,1,1,1,0,0],[1,1,1,0,0,0],[0,1,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
print(a)