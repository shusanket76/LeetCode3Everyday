from collections import deque
class Solution:
    def shortestBridge(self, grid) -> int:
        set1 = set()
        set2 = set()
        def dfs1(x,y, sit):
            if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and (x,y) not in sit and grid[x][y]==1:
                sit.add((x,y))
                a = dfs1(x-1,y,sit) 
                b = dfs1(x+1,y,sit) 
                c = dfs1(x,y+1,sit) 
                d = dfs1(x,y-1,sit) 
        visit = set()
        res = [0]
        def shortestpath(queue, src, target):
            while queue:
                q = len(queue)
                for x in range(q):
                    (x,y) = queue.popleft()
                    
                    dir = [(1,0), (-1,0), (0,1), (0,-1)]
                    for d in dir:
                        r = x+d[0]
                        c = y+d[1]
                        if r>=0 and c>=0 and r<len(grid) and c<len(grid[0]) and (r,c) not in visit and (r,c) not in src:
                            visit.add((r,c))
                            if (r,c) in target:
                                # res[0]+=1
                                return res[0]
                            queue.append((r,c))
                res[0]+=1
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==1:
                    if len(set1)==0:
                        dfs1(x,y, set1)
                    else:
                        dfs1(x,y, set2)
 
        queue = deque()
        if len(set1)<=len(set2):
            queue.extend(set1)
            a = shortestpath(queue, set1, set2)
            return res[0]
        else:
            queue.extend(set2)
            a = shortestpath(queue, set2, set1)
            return res[0]