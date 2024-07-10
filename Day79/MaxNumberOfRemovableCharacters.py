class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        l = 0
        r = len(removable)-1
        res = 0
        while l<=r:
            mid = int((l+r)/2)
            pl = 0
            sl = 0
            a = set(removable[:mid+1]) 
            while pl<len(p) and sl<len(s):
                
                if sl in a or s[sl]!=p[pl]:
                    sl+=1
                    continue
                
                sl+=1
                pl+=1
                
            if pl==len(p):
                res = max(res, mid+1)
                l=mid+1

            else:
                r = mid-1
        
        return (res)
        