class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]]
        l = 0
        r = 1
        while r<len(intervals):
            lastend = res[-1][1]
            if intervals[r][0]<=lastend:
                res[-1][1] = max(lastend, intervals[r][1])
            else:
                res.append(intervals[r])
            r+=1
        return res
        