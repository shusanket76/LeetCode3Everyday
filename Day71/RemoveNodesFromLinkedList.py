# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        dummy = ListNode(0, prev)
        tail = dummy
        maxres = 0
        while tail and tail.next:
            if maxres>tail.next.val:
                tail.next = tail.next.next
            else:
                maxres = tail.next.val
                tail = tail.next
        prev2, curr2 = None, dummy.next
        while curr2:
            nxt2 = curr2.next
            curr2.next = prev2
            prev2= curr2
            curr2= nxt2
        return prev2
        