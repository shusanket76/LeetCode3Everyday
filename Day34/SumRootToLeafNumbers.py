# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(root, valstr):
            if not root:
                return 0
            if  (not root.left and not root.right):
                return int(valstr)
            left = dfs(root.left, valstr+str(root.left.val) if root.left else valstr)
            right = dfs(root.right,valstr+str(root.right.val) if root.right else valstr)
            print(left, right)
            return int(left)+int(right)
        return dfs(root, str(root.val))