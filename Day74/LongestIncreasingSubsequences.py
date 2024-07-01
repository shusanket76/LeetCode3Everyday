class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        hasmap = {}
        res = [0]
        def dfs(start, prev):
            
            if start==len(nums) or prev>=nums[start]:
                return 0
            if start in hasmap:
                 return hasmap[start]
            maxval = None
            for x in range(start, len(nums)):
                a = dfs(x+1,nums[start] )
                if a is not None:
                    a+=1
                    if maxval is None or maxval<a:
                        maxval=a
            hasmap[start] = maxval
            return maxval


            
        res = [0]
        for x in range(len(nums)):
            b = dfs(x,float("-inf") )
            res[0] = max(res[0],b)
        return res[0]

            

        b = dfs(0,float("-inf") )
        print(b)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        hasmap = {}
        res = [0]
        def dfs(start, prev):
            
            if start==len(nums) or prev>=nums[start]:
                return 0
            if start in hasmap:
                 return hasmap[start]
            maxval = None
            for x in range(start, len(nums)):
                a = dfs(x+1,nums[start] )
                if a is not None:
                    a+=1
                    if maxval is None or maxval<a:
                        maxval=a
            hasmap[start] = maxval
            return maxval


            
        res = [0]
        for x in range(len(nums)):
            b = dfs(x,float("-inf") )
            res[0] = max(res[0],b)
        return res[0]

            

