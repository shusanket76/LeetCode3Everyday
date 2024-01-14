class Solution:
    def sortArray(self, nums):
        

        def dfs(nums):
            if len(nums)==1:
                return nums[:]
            start = 0
            end = len(nums)
            mid = start+end//2
            left = dfs(nums[start:mid])
            right = dfs(nums[mid:end])
            leftpointer = 0
            rightpointer=0
            numspointer = 0
            while leftpointer<len(left) and rightpointer<len(right):
                if left[leftpointer] < right[rightpointer]:
                    nums[numspointer] = left[leftpointer]
                    leftpointer+=1
                else:
                    nums[numspointer] = right[rightpointer]
                    rightpointer+=1
                numspointer+=1
            while leftpointer<len(left):
                nums[numspointer] = left[leftpointer]
                numspointer+=1
                leftpointer+=1
            while rightpointer<len(right):
                nums[numspointer]=right[rightpointer]
                rightpointer+=1
                numspointer+=1
            return nums
        return dfs(nums)