def maxDistance(position, m: int) -> int:
        position.sort()

        start = position[0]
        end = position[-1]
        while start<=end:
            dis = int((start+end)/2)
            curr = position[0]
            target = 0
            for x in range(1,len(position)):
                if abs(curr-position[x])>=dis:
                    target+=1
                    curr=position[x]
                if target==m:
                    start=dis+1
                    break
            if target<m:
                end = dis-1
        return dis
a = maxDistance(position = [5,4,3,2,1,1000000000], m = 3)