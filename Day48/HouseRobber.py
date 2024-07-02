# class Solution:
#     def rob(self, nums) -> int:
#         hasmap = {}
#         def dfs(nums, total):
#             if tuple(nums) in hasmap:
#                 return hasmap[tuple(nums)]
             
#             if len(nums)==0:
#                 return 0
            
#             hasmap[tuple(nums[:])] =  max(dfs(nums[2:], total)+nums[0], dfs(nums[1:], total))
#             return hasmap[tuple(nums)]
            
#         return dfs(nums,0)
# ================================================================================================
# I LIKE SOL
class Solution:
    def rob(self, nums: List[int]) -> int:
        hasmap = {}

        def dfs(pointer):
            if pointer>=len(nums):
                return 0
            if pointer in hasmap:
                return hasmap[pointer]
            a = dfs(pointer+2)+nums[pointer]
            b = dfs(pointer+3)+nums[pointer]
            hasmap[pointer] = max(a,b)
            return max(a,b)
            
         
            
        return max(dfs(0), dfs(1))

        