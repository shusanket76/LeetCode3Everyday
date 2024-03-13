# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0
        while l1 and l2:
            
            total = l1.val+l2.val+carry
            
            carry = 0
            if total>=10:
                carry = total//10
                total = total%10
                
            tail.next = ListNode(total)
            tail=tail.next
            l1=l1.next
            l2=l2.next
        while l1:
            total = l1.val+carry
            carry = 0
            if total>=10:
                carry = total//10
                total = total%10
            tail.next = ListNode(total)
            l1=l1.next
            tail=tail.next
        while l2:
            total = l2.val+carry
            carry = 0
            if total>=10:
                carry = total//10
                total = total%10
            tail.next = ListNode(total)
            l2=l2.next
            tail=tail.next
        while carry!=0:

            if carry>=10:
                tail.next = ListNode(carry%10)
                carry = carry//10
            else:
                tail.next = ListNode(carry)
                carry = 0
        return dummy.next
