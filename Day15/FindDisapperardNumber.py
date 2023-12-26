# BRUTE FORCE
# class Solution:
#     def findDisappearedNumbers(self, nums):
#         res =[]
#         hasmap={}
#         for x in nums:
#             hasmap[x]=True
#         for y in range(1,len(nums)+1):
#             if y not in hasmap:
#                 res.append(y)
#         return res
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in nums:
            i=abs(x)-1
            nums[i]=-1*abs(nums[i])
        res = []
        for y in range(len(nums)):
            if nums[y]>0:
                res.append(y+1)
        return res