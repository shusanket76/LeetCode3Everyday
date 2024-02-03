# class Solution:
#     def findMin(self, nums) -> int:
#         l=0
#         r=len(nums)-1
#         ans = nums[0]
#         while l<=r:
#             mid = int((l+r)/2)
#             ans = min(nums[mid], ans)
#             # first group
#             if nums[mid]>=nums[l]:
#                 if nums[r]<nums[l]:
#                     l=mid+1
#                 else:
#                     r=mid-1
#             # second group
#             else:
#                 if r-mid>1:
#                     r=mid-1
#                 else:
#                     l=mid+1
#         return ans

        


# ======================================================================
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = nums[l]
        while l<=r:
            if nums[l]<=nums[r]:
                res = min(res, nums[l])
                return res
            mid = (l+r)//2
            res = min(res, nums[mid])
  
            if nums[l]<=nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return res
        