class Solution:
    def interchangeableRectangles(self, rectangles) -> int:
        hasmap= {}
        haset = set()
        for x in rectangles:
            val = x[0]/x[1]
            if val in hasmap:
                hasmap[val]+=1
                
            else:
                hasmap[val]=1
                haset.add((x[0],x[1]))
        res = 0
        for d in hasmap.values():
            if d>1:
                while d>1:
                    res+=d-1
                    d=d-1
        
        return res