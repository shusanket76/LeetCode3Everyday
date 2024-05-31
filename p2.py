def maxProduct(nums) -> int:
        hasmap = {}
        
        def dfs(nums, curr):
            if len(nums)==0:
                return 1
            res = None
            for x in nums:
                a = dfs(nums[1:], curr)
                a*=x
                if res is None or res<a:
                    res = a
            return res


        return dfs(nums, curr=1)
a = maxProduct([2,3,-1,4])