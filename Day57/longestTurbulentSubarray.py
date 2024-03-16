class Solution:
    def maxTurbulenceSize(self, nums: List[int]) -> int:
        curr = 0
        r = 0
        finalres = 0
        greaterthan = True
        lessthan = True
        while r<len(nums)-1:
            if nums[r]>nums[r+1]:
                if  lessthan:
                    curr+=1
                    finalres = max(finalres, curr)
                else:
                    curr = 1

                greaterthan = True
                lessthan = False
            elif nums[r]<nums[r+1]:
                if  greaterthan:
                    curr+=1
                    finalres = max(finalres, curr)
                else:
                    curr = 1


                lessthan = True
                greaterthan = False
                
            else:
                curr = 0
                lessthan = True
                greaterthan = True
            r+=1
        return(finalres+1)

        