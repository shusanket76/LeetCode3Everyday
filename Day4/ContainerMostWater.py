class Solution:
    def maxArea(self, height) -> int:
        left = 0
        res = 0
        right = len(height)-1
        while left<=right:
            h = min(height[left], height[right])
            area = h*(right-left)
            res = max(res, area)
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return res


        