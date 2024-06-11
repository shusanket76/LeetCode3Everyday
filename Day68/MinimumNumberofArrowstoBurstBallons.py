class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda i:i[1])
        print(points)
        shoot = points[0][1]
        r = 1
        res = 1
        while r<len(points):
                if points[r][0]<=shoot<=points[r][1]:
                        pass
                else:
                    shoot = points[r][1]
                    res+=1
                r+=1
        return res
     