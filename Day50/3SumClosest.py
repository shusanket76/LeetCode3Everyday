class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        res = [float("inf")]
        nums.sort()
        for x in range(len(nums)):
            if x>0 and nums[x]==nums[x-1]:
                continue
            l = x+1
            r = len(nums)-1
            while l<r:
                wehave = nums[x]+nums[l]+nums[r]
                if abs(res[0]-target)>abs(wehave-target):
                    res[0] = wehave
                if wehave>target:
                    r-=1
                elif wehave<target:
                    l+=1
                else:
                    return target
                        
        return res[0]