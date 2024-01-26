def findPeakElement(nums) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            l= mid-1
            r = mid+1

            lval = False
            rval = False
            if l>=0:
                lval = True
            if r<len(nums):
                rval = True
            if lval and rval:
                if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                    return nums[mid]
                elif nums[mid]<nums[mid-1]:
                    r=mid-1
                elif nums[mid]<nums[mid+1]:
                    l = mid+1
            elif rval:
                if nums[mid]>nums[mid+1]:
                    return nums[mid]
                else:
                    return nums[mid+1]
    
            else:
                return mid
        
a = findPeakElement([2,1])