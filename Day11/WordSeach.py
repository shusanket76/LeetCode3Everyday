class Solution:
    def exist(self, board, word: str) -> bool:
        def dfs(path, x, y, counter):
            if x>=0 and y>=0 and x<len(board) and y<len(board[0]) and (x,y) not in path:
            
                if board[x][y]==word[counter]:
                    counter+=1
                else:
                    return False
                if counter>=len(word):
                    return True
              

                path.add((x,y))
                a=dfs(path, x+1, y,counter)
                b=dfs(path, x-1, y,counter)
                c=dfs(path, x, y-1,counter)
                d=dfs(path, x, y+1,counter)
                path.remove((x,y))
                return (a or b or c or d)
            else:
                return False
                

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y]==word[0]:
                    path=set()
                    if dfs(path, x, y,0) is True:
                        return True
        return False
        

        