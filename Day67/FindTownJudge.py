class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hasmap = {}
        trustj={}
        if len(trust)==0 and n<=1:
            return 1
        if len(trust)==0 and n>=2:
            return -1
        for x in trust:
            hasmap[x[0]]=True
            if x[1] in trustj:
                trustj[x[1]]+=1
            else:
                trustj[x[1]]=1
        
        
        for y in range(1,n+1):
            if y not in hasmap:
                if trustj[y]<n-1:
                    return -1
                return y
        return -1
        
        