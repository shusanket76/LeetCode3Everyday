def removeCoveredIntervals(intervals) -> int:
        intervals.sort(key = lambda i :i[0])
        previous = intervals[0]
        r = 1
        res = 0
        while r<len(intervals):
            if previous[0]<=intervals[r][0] and previous[1]>=intervals[r][1]:
                res+=1
                r+=1
            elif previous[0]==intervals[r][0] and previous[1]<=intervals[r][1]:
                res+=1
                previous = [intervals[r][0], intervals[r][1]]
                r+=1
            else:
                previous = intervals[r]
                r+=1
        return len(intervals)-res

a = removeCoveredIntervals([[1,2],[1,4],[3,4]])
        