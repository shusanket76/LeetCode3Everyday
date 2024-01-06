class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr, pointer):
            if pointer>=len(nums):
                res.append(curr[:])
                return
            curr.append(nums[pointer]) 
            dfs(curr, pointer+1)
            curr.pop()
            dfs(curr, pointer+1)

        curr = []
        dfs(curr, 0)
        return res