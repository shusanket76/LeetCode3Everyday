class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        res = []
        r = 0
        while r<len(nums):
            if nums[r]>0:
                pos.append(nums[r])
            else:
                neg.append(nums[r])
            r+=1
        r = 0
        while r<len(pos):
            res.append(pos[r])
            res.append(neg[r])
            r+=1
        return (res)
