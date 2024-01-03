# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        curra=headA
        currb=headB
        headalen = 1
        headblen=1
        while curra.next:
            headalen+=1
            curra = curra.next
        while currb.next:
            headblen+=1
            currb=currb.next
        if curra!=currb:
            return None
        curra=headA
        currb=headB
        if headalen<=headblen:
            while headalen!=headblen:
                currb=currb.next
                headblen-=1
        else:
            while headalen!=headblen:
                curra=curra.next
                headalen-=1
        while curra:
            if curra==currb:
                return curra
            curra=curra.next
            
            currb=currb.next
      
        return 