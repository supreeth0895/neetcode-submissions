# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total_len = 0
        curr = head
        while curr:
            curr= curr.next
            total_len +=1
        idx_to_del = total_len-n
        i = 0
        curr = head
        prev = None
        print(total_len, idx_to_del)
        if idx_to_del == 0:
            return head.next
        while i!=idx_to_del:
            prev = curr
            curr = curr.next
            i+=1
        prev.next = curr.next
        return head