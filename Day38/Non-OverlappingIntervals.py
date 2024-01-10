class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort(key = lambda i:i[0])
        prevend = intervals[0][1]
        r = 1
        fr = 0 
        while r<len(intervals):
           
            if prevend>intervals[r][0]:
                prevend = min(intervals[r][1], prevend)
                fr+=1
            else:
                prevend = intervals[r][1]
            r+=1
        return fr
        