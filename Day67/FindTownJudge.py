class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adjacencylist = {n:[] for n in range(1,n+1)}
        trustnumbers = {n:0 for n in range(1,n+1)}
        for x in trust:
            adjacencylist[x[0]].append(x[1])
            trustnumbers[x[1]]+=1
        for y in adjacencylist:
            if len(adjacencylist[y])==0:
                if trustnumbers[y]==n-1:
                    return y
        return -1

        
        