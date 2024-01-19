class Solution:
    def singleNonDuplicate(self, nums) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if (mid+1>=len(nums) or nums[mid]!=nums[mid+1]) and (mid-1<0 or nums[mid]!=nums[mid-1]):
                return nums[mid]
            else:
                if nums[mid]==nums[mid-1]:
                    first = mid-1-l
                    if first%2==0:
                        l =mid+1
                    else:
                        r=mid-2
                elif nums[mid]==nums[mid+1]:
                    first = mid-l
                    if first%2==0:
                        l = mid+2
                    else:
                        r = mid-1




        