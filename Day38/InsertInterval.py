class Solution:
    def insert(self, intervals, newInterval):
        res = []
        l = 0
        r= len(intervals)
        while l<r:
            if newInterval[1]<intervals[l][0]:
                res.append(newInterval)
                return res+intervals[l:]
            elif newInterval[0]>intervals[l][1]:
                res.append(intervals[l])
            else:
                newInterval = [min(newInterval[0], intervals[l][0]), max(newInterval[1], intervals[l][1])]
            l+=1
        res.append(newInterval)
        return res
        
            
                         

        