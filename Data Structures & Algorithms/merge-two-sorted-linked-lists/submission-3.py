# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = head1
        temp2 = head2

        ans = ListNode()
        cur_ans_ptr = ans

        while temp1 != None and temp2 != None:
            if temp1.val <= temp2.val:
                cur_ans_ptr.next = temp1
                temp1 = temp1.next
                cur_ans_ptr = cur_ans_ptr.next
                cur_ans_ptr.next = None
            else:
                cur_ans_ptr.next = temp2
                temp2 = temp2.next
                cur_ans_ptr = cur_ans_ptr.next
                cur_ans_ptr.next = None
        
        if temp1 != None:
            cur_ans_ptr.next = temp1
        elif temp2 != None:
            cur_ans_ptr.next = temp2
        return ans.next









# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         return_ptr = None
#         if list1 == None:
#             return list2
#         if list2 == None:
#             return list1

#         if list1.val < list2.val :
#             ptr1  = list1
#             ptr2 = list2
#         else:
#             ptr1 = list2
#             ptr2 = list1
#         return_ptr = ptr1
        
#         prev = None
#         while ptr1 != None and ptr2 != None:
#             if ptr1.next:
#                 if ptr1.next.val >= ptr2.val:
#                     temp = ptr1.next
#                     ptr1.next = ptr2
#                     ptr2 = ptr2.next
#                     ptr1.next.next = temp
            
#             prev = ptr1
#             ptr1 = ptr1.next
        
#         if ptr2 != None and ptr1 == None:
#             prev.next = ptr2
#         return return_ptr

        