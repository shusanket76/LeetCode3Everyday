class Solution:
    def shuffle(self, nums, n: int):
        res =[]
        slow = 0
        fast =0
        while fast<len(nums):
            fast+=2
            slow+=1
        first = 0
        second = slow
        print(second)
        while second<len(nums):
            res.append(nums[first])
            res.append(nums[second])
            first+=1
            second+=1
        return res
        