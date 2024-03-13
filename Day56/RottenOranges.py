from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        time, fresh =0,0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==1:
                    fresh+=1
                if grid[x][y]==2:
                    queue.append((x,y))
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while queue and fresh>0:
            qlen = len(queue)
            for a in range(qlen):
                node = queue.popleft()
                for b in directions:
                    row = node[0]+b[0]
                    col = node[1]+b[1]
                    if (row>=0 and col>=0 and row<len(grid) and col<len(grid[0]) and grid[row][col]==1):
                        grid[row][col]=2
                        fresh-=1
                        queue.append((row,col))
            time+=1
        if fresh!=0:
            return -1
        return time


        