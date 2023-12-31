class Solution:
    def diagonalSum(self, mat) -> int:
        haset = set()
        x=0
        y=0
        su=0
        while x<len(mat) and y<len(mat[0]):
            if(x,y) not in haset:
                su+=mat[x][y]
                haset.add((x,y))
            x+=1
            y+=1
        x = 0
        y=len(mat[0])-1
        while x<len(mat) and y>=0:
            if(x,y) not in haset:
                su+=mat[x][y]
                haset.add((x,y))
            x+=1
            y-=1
        return su