class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0 
        r = len(nums)-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]==target:
                return True
            
            elif nums[l]<nums[mid]:
                if nums[l]>target and nums[mid]<=target:
                    l=mid+1
                else:
                    r=mid-1
                #first array
            elif nums[l]>nums[mid]:
                if nums[r]<target and nums[mid]>=target:
                    r=mid-1
                else:
                    l=mid+1
                #second array
            else:
                l+=1
        return False
    




# ======================================================
    # ANOTHER SOLUTION (REVISI)
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0 
        r = len(nums)-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]==target:
                return True
            
            if nums[l]<nums[mid]:
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            elif nums[l]>nums[mid]:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                l+=1
        return False