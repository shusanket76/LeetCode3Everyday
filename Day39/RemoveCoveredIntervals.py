class Solution:
    def removeCoveredIntervals(self, intervals) -> int:
        intervals.sort(key = lambda i:i[0])
        print(intervals)
        prea = intervals[0][0]
        preb = intervals[0][1]
        res = 0
        r = 1
        while r<=len(intervals)-1:
            if preb >=intervals[r][0] and preb>=intervals[r][1]:
                res+=1
            elif prea == intervals[r][0] and preb<=intervals[r][1]:
                res+=1
                preb = max(preb, intervals[r][1])

            else:
                prea = intervals[r][0]
                preb = intervals[r][1]
            r+=1
        return len(intervals)-res
        