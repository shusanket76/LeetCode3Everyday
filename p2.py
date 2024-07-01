def lengthOfLIS(nums) -> int:
        hasmap = {}
        res = [0]
        def dfs(start, prev):
            
            if start==len(nums) or prev>=nums[start]:
                return 0
            if start in hasmap:
                 return hasmap[start]+1
            maxval = None
            for x in range(start, len(nums)):
                a = dfs(x+1,nums[start] )
                if a is not None:
                    if maxval is None or maxval<a:
                        a+=1
                        maxval=a
            hasmap[start] = maxval
            return maxval


            
        res = [0]
        for x in range(len(nums)):
            b = dfs(x,float("-inf") )
            res[0] = max(res[0],b)
        return res[0]

a = lengthOfLIS([10,9,2,5,3,4])
print(a)