def gridGame(grid) -> int:

        # find total sum

        # find total sum
        totalsum = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                totalsum +=grid[x][y]
        
        def redrobot(x, y, visit, total=totalsum):
            if x==2 and y==len(grid[0]):
                val = bluerobot(0,0,visit, 0)
                return val
            if x>=0 and y>=0 and x<2 and y<len(grid[0]):
                visit.add((x,y))
                right = redrobot(x,y+1, visit) 
                down = redrobot(x+1,y, visit)
                visit.remove((x,y))
                return min(right, down)
            else:
                return total
        def bluerobot(x,y, visit, curr):
            if x==2 and y==len(grid[0]):
                return 0
            if x>=0 and y>=0 and x<2 and y<len(grid[0]):
                right = bluerobot(x,y+1, visit, curr)
                if (x,y) not in visit:
                    right+=grid[x][y]
                down = bluerobot(x+1, y, visit, curr)
                if (x,y) not in visit:
                    down+=grid[x][y]
                return max(right, down)
            else:
                return 0
                    
        c = redrobot(0,0, set(), totalsum)
        print(c)
grid = [[2,5,4],[1,5,1]]
b = gridGame(grid)