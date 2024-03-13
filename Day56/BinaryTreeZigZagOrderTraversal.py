from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lefttoright = True
        qs = deque()
        qs.append(root)
        res = []
        while qs:
            qslength = len(qs)
            
            temp =[]
            print("fits")
            for x in range(qslength):
                print("second")
                if  lefttoright:
                    # queue
                    node = qs.popleft()
                    if node:
                        if node.left:
                            qs.append(node.left)
                        if node.right:
                            qs.append(node.right)
                        temp.append(node.val)
                    
                    
                else:
                    # stack
                    node = qs.pop()
                    if node:
                        if node.right:
                            qs.appendleft(node.right)
                        if node.left:
                            qs.appendleft(node.left)
                        temp.append(node.val)
            if len(temp)!=0:
                res.append(temp)
                lefttoright = not lefttoright
        return res

        