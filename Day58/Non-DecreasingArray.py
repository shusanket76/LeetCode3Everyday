class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        l = 0
        modify = 0
        while l<len(nums)-1:
            if nums[l]>nums[l+1]:
                modify+=1
                if l==0:
                    nums[l] = nums[l+1]-1
                else:
                    if nums[l-1]<=nums[l+1]:
                        nums[l] = nums[l-1]+1
                    else:
                        nums[l+1] = nums[l]+1
            if modify>=2:
                return False
            l+=1
        if nums[l-1]<=nums[l]:
            return True
        return False
        