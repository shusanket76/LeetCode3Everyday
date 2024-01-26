class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        temp = 0
        hasmap = {0:-1}
        for x in range(len(nums)):
            temp+=nums[x]
            wehave = temp%k
            if wehave not in hasmap:
                hasmap[wehave]=x
            
            elif (x-hasmap[wehave])>1:
                return True



        return False
        