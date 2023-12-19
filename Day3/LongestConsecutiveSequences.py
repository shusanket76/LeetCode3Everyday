def longestConsecutive(nums) -> int:
        numset = set(nums)
        res = 0
        for x in numset:
            if x-1 not in numset:
                a = 0
                while x in numset:
                    x+=1
                    a+=1
                    res=max(res,a)
        return res

a = longestConsecutive([100,4,200,1,3,2])