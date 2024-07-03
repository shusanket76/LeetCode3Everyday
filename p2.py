def rotate(matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        top = 0
        bottom = len(matrix)-1
        
        while top<=bottom:
            l = top
            r = bottom
            val1=val2=0
            for x in range(r-l):
                # top left
                val = matrix[top][x]

                # top left
                matrix[top][x] = matrix[bottom-x][l]

                # bottom left
                matrix[bottom-x][l]  = matrix[bottom][r-x]

                # bottom right
                matrix[bottom][r-x] = matrix[x][r]

                # top right

                matrix[x][r] = val


            top+=1
            bottom-=1
        return matrix
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
a = rotate(matrix)