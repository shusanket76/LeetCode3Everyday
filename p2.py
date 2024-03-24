def spiralOrder(matrix):
        
        top = 0
        bottom = len(matrix)-1
        res =[]
        while top<=bottom:
            l = top
            r = bottom
            for x in range(l, r):
                res.append(matrix[top][x])
            for x in range(top, bottom):
                res.append(matrix[x][len(matrix[0])-1])
            for x in range(r, l, -1):
                res.append(matrix[bottom][x])
            for x in range(r,l,-1):
                res.append(matrix[x][0])
            top+=1
            bottom-=1
        
a = spiralOrder([[1,2,3],[4,5,6],[7,8,9]])