class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        currmin = nums[0]
        for x in nums[1:]:
            while stack and x>=stack[-1][0]:
                stack.pop()
            if stack and x<stack[-1][0] and x>stack[-1][1]:
                return True
            stack.append([x, currmin])
            currmin = min(currmin, x)
        return False
