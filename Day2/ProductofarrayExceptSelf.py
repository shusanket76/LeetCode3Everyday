class Solution:
    def productExceptSelf(self, nums):
        leftarr = []
        leftmul = 1
        res = []
        for x in range(len(nums)):
            if x==0:
                leftarr.append(leftmul)
            else:
                leftmul *= nums[x-1]
                leftarr.append(leftmul)
        
        rightarr = []
        rightmul = 1
   
        for y in range(len(nums)-1,-1,-1):
            if y==len(nums)-1:
                rightarr.append(rightmul)
            else:
                rightmul *= nums[y+1]
                rightarr.append(rightmul)
        for a in range(len(rightarr)):
            res.append(leftarr[a]*rightarr[len(rightarr)-1-a])
        return res