class Solution:
    def shipWithinDays(self, weights, days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r
        while l<=r:
            mid = int((l+r)/2)
            r1 = 0
            tempsum = 0
            tempship = 1
            while r1<len(weights):
                if (tempsum+weights[r1])>mid:
                    tempship+=1
                    tempsum=0
                    if (tempship>days):
                        break
                    else:
                        tempsum+=weights[r1]
                else:
                    tempsum+=weights[r1]
                r1+=1
            if r1==len(weights):
                res = min(res, mid)
                r = mid-1
            else:
                l=mid+1
        return res
            
