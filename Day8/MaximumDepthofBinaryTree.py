class Solution:
    def maxDepth(self, root) -> int:
        count=0
        res = [0]
        def dfs(root,count):
            if not root:
                return 0
            count+=1
            res[0]=max(res[0], count)
            dfs(root.left,count)
            dfs(root.right,count)
            return res
        dfs(root,0)
        return res[0]