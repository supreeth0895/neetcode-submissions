#SUPREETH
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr2 = head
        for i in range(0,n):
            ptr2 = ptr2.next


        ptr1 = head
        prev = None
        while ptr2 != None:
            ptr2 = ptr2.next
            prev = ptr1
            ptr1 = ptr1.next
        
        if prev:
            prev.next = ptr1.next
        else:
            head = head.next

        return head






        