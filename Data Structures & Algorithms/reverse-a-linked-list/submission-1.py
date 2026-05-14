# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        if head.next == None:
            return head
        prev = None
        cur = head
        next_node = cur.next
        while cur != None:
            cur.next = prev
            prev = cur
            cur = next_node
            if cur != None:
                next_node =  cur.next
        
        return prev
        