from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root) -> int:
        queue = deque()
        res = 0
        queue.append([root, 1, 0])
        prevnum, prevlevel = 1, 0
        while queue:
            node, num, level = queue.popleft()

            if level > prevlevel:
                prevnum = num
                prevlevel = level
            res = max(res, num - prevnum + 1)
            if node.left:
                queue.append([node.left, 2 * num, level + 1])
            if node.right:
                queue.append([node.right, (2 * num) + 1, level + 1])

        return res
