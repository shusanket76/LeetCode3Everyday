class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        hasmap = {}
        def dfs(row, col):
            # row+1=> col or col+1
            if (row, col) in hasmap:
                return hasmap[(row,col)]
            if row>=0 and col>=0 and row<len(triangle) and col<len(triangle[row]):
                a = dfs(row+1, col)
                b = dfs(row+1, col+1)
                val = min(a,b)+triangle[row][col]
                hasmap[(row, col)] = val
                return hasmap[(row, col)] 
            else:
                return 0
        
        return (dfs(0,0))
        