def findMinArrowShots(points) -> int:
        points.sort(key = lambda i:i[0])
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
a = findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])
print(a)