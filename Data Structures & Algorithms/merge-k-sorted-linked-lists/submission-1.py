# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mainHead = ListNode(0, None)
        curr = mainHead
        while any(lists):
            minNode = None
            indx = None
            for i in range(len(lists)):
                if lists[i]:
                    if not minNode:
                        minNode = lists[i]
                        indx = i
                    else:
                        if lists[i].val <minNode.val:
                            minNode = lists[i]
                            indx = i
            lists[indx] = lists[indx].next
            curr.next = minNode
            curr = minNode
        return mainHead.next
        