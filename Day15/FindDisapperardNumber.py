class Solution:
    def findDisappearedNumbers(self, nums):
        res =[]
        hasmap={}
        for x in nums:
            hasmap[x]=True
        for y in range(1,len(nums)+1):
            if y not in hasmap:
                res.append(y)
        return res
        