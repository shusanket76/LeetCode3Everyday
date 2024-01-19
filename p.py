def singleNonDuplicate(nums) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            else:
                if nums[mid]==nums[mid-1]:
                    first = mid-1-l
                    if first%2==0:
                         l=mid+1
                    else:
                         r = mid-2
                        

                elif nums[mid]==nums[mid+1]:
                    first = mid-l
                    if first%2==0:
                        l = mid+2
                    else:
                        r = mid-1



a = singleNonDuplicate([1,1,2,3,3,4,4,8,8])
        