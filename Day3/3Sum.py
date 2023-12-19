class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for x in range(len(nums)):
            if x>0 and nums[x]==nums[x-1]:
                continue
            left = x+1
            right=len(nums)-1
            while left<right:
                wehave = nums[x]+nums[left]+nums[right]
                if wehave>0:
                    right-=1
                elif wehave<0:
                    left+=1
                else:
                    res.append([nums[x], nums[left], nums[right]])
                    left+=1
                    while left<=right and nums[left]==nums[left-1]:
                        left+=1
        return res

        