# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return 0
            if (not root.left and not root.right):
                return 1
            leftcount = dfs(root.left)
            rightcount = dfs(root.right)
            res[0] = max(res[0], leftcount+rightcount)
            return max(leftcount+1, rightcount+1)
        dfs(root)
        return res[0]
            
            
        