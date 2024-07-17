class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        start = 1
        end = position[-1]
        res = float("-inf")
        while start<=end:
            dis = int((start+end)/2)
            curr = position[0]
            target = 1
            for x in range(1,len(position)):
                if abs(curr-position[x])>=dis:
                    target+=1
                    curr=position[x]
                if target==m:
                    res = max(res, dis)
                    start=dis+1
                    break
            if target<m:
                end = dis-1

        return res

        