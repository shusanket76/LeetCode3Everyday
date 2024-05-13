def leastBricks(wall) -> int:
        hasmap={}
        for x in wall:
            totalcount = 0
            for y in x:
                totalcount+=y
                if totalcount in hasmap:
                    hasmap[totalcount]+=1
                else:
                    hasmap[totalcount]=1
             
        print(hasmap)
        hasmap.pop(totalcount)
        return totalcount - max(hasmap.values())


a = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
leastBricks(a)
print(leastBricks(a))