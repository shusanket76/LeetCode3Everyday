# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        
        def sameTree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            return (sameTree(p.left, q.left) and sameTree(p.right, q.right))
        

        if not root:
            return False
        if not subRoot:
            return True
        if sameTree(root,subRoot) is True:
            return True
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot))
        

