class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        path=set()
        # finding unsurrounded region
        def dfs(x,y):
            if x>=0 and y>=0 and x<len(board) and y<len(board[0]) and (x,y) not in path and board[x][y]=="O":
                path.add((x,y))
                board[x][y]="T"
                dfs(x-1,y)
                dfs(x,y-1)
                dfs(x+1,y)
                dfs(x,y+1)
        for x in range(len(board)):
            if board[x][0]=="O":
                dfs(x,0)
            if board[x][len(board[0])-1]=="O":
                dfs(x, len(board[0])-1)
        for y in range(len(board[0])):
            if board[0][y]=="O":
                dfs(0,y)
            if board[len(board)-1][y]=="O":
                dfs(len(board)-1, y)
        for z in range(len(board)):
            for k in range(len(board[0])):
                if board[z][k]=="O":
                    board[z][k]="X"
                if board[z][k]=="T":
                    board[z][k]="O"
        