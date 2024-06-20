# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res= [""]
        def dfs(root):
            if not root:
                return 
            res[0]+="("
            res[0]+=str(root.val)
            if not root.left and root.right:
                res[0]+="()"
            else:
                dfs(root.left)
            dfs(root.right)
            res[0]+=")"

        dfs(root)
        return (res[0][1:len(res[0])-1])