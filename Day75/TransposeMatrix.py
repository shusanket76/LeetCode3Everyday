class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        nm = [[0 for x in range(row)] for y in range(col)]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                nm[col][row]=matrix[row][col]
        return nm
        