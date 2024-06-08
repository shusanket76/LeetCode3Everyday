# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        mya = 0
        
        firstpart = ListNode(0)
        tail = firstpart
        while list1 and mya<=a-1:
            tail.next = ListNode(list1.val)
            tail = tail.next
            list1=list1.next
            mya+=1
        firstsecondpart = list1.next
        tail.next = list2
        while list2 and list2.next:
            list2 = list2.next
        while firstsecondpart and mya<b:
            firstsecondpart = firstsecondpart.next
            mya+=1
        list2.next = firstsecondpart
        return firstpart.next


        