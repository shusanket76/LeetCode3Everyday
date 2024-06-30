class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        hasnums = set(nums)
        option = ["0","1"]
        def dfs(tl, curr):
            if len(curr)==tl:
                return curr[:]
            for x in option:
                curr+=x
                a = dfs(tl, curr)
                if a not in hasnums and  len(a)==tl:
                    return a
                curr = curr[0:-1]
            return curr[0:-1]
                
        
        b = dfs(len(nums[0]), "")
        return (b)
        