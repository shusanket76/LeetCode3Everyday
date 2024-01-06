class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(pointer, curr):
            if pointer>len(nums):
                return 
            if pointer==len(nums):
                res.append(curr[:])
                return 
            curr.append(nums[pointer])
            dfs(pointer+1, curr)
            curr.pop()
            while pointer<len(nums)-1 and nums[pointer]==nums[pointer+1]:
                pointer+=1
            dfs(pointer+1, curr)
        dfs(pointer=0, curr=[])
        return res