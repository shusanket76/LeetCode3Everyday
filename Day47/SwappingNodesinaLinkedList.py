# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head, k: int):
            dummy = ListNode(0, head)
            first = second=third  =dummy
            
            while k!=0:
                second = second.next
                third = third.next
                k-=1
            

            while second:
                second = second.next
                first = first.next
            third.val,first.val=first.val,third.val
            return dummy.next
            
                
        