class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        hasmap={}
        
        for x in wall:
            totalcount = 0
            for y in x:
                totalcount+=y
                if totalcount in hasmap:
                    hasmap[totalcount]+=1
                else:
                    hasmap[totalcount]=1
             
        
        hasmap.pop(totalcount)

        if len(hasmap)==0:
            return len(wall)
        else:
            return len(wall) - max(hasmap.values())
        
        