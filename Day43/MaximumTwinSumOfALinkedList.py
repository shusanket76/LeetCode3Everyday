# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head) -> int:
        res = []
        prev,curr = None, head
        while curr:
            res.append(curr.val)
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        x = 0 
        while prev:
            res[x]+=prev.val
            x+=1
            prev = prev.next
        finalans = 0
        for a in res:
            finalans = max(finalans, a)
        return finalans