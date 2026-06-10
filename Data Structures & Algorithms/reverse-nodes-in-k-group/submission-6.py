#SUPREETH
# Walk the list in groups of k. For each group, reverse the nodes in place.
# Connect the reversed group to the next group's start.
# If a group has fewer than k nodes, leave it as-is.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head
        prev_node = None
        next_group_end = head

        group_start = start

        while start != None:
            group_start = start

            # Find the end of the current group (k-1 steps from start)
            # If group has fewer than k nodes, return as-is
            end = start
            for i in range(0, k-1):
                end = end.next
                if end == None:
                    return head

            # Find the start of the next group (one step past end)
            next_group_end = end
            for i in range(0, k):
                if next_group_end.next:
                    next_group_end = next_group_end.next
                else:
                    next_group_end = end.next
                    break

            # Reverse nodes in current group [start, end]
            next_start = end.next
            cur_node = start
            while cur_node != next_start:
                temp = cur_node.next
                cur_node.next = prev_node
                prev_node = cur_node
                cur_node = temp

            # If this is the first group, update head to the new front (end)
            if group_start == head:
                head = end

            # Connect tail of reversed group to start of next group
            group_start.next = next_group_end
            start = next_start

        return head