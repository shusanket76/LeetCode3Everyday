def jump(nums) -> int:
        l = r = 0
        res = 0
        while r<len(nums)-1:
            farthest = 0
            for x in range(l,r+1):
                farthest = max(farthest, x+nums[x])
            l=r+1
            r = farthest
            res+=1
        return res
a = jump([2,3,1,1,4])