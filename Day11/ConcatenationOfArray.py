class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:   
        ans = []
        for x in range(2):
            for y in nums:
                ans.append(y)
        return ans
        