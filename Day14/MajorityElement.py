class Solution:
    def majorityElement(self, nums) -> int:
        res = []
        count=0
        for x in range(len(nums)):
            if x==0:
                res = nums[x]
                count+=1
            else:
                if nums[x]==res:
                    count+=1
                else:
                    count-=1
                    if count<0:
                        res=nums[x]
                        count=0
        return res