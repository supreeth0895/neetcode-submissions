# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len1 = self.getlength(l1)
        len2 = self.getlength(l2)

        ans = None
        if len1 >= len2:
            ptr1 = l1
            ptr2 = l2
            ans = l1
        else:
            ptr1 = l2
            ptr2 = l1
            ans = l2
    
        carry = 0
        while ptr1 != None:
            if ptr2 != None:
                total = ptr1.val + ptr2.val + carry
                ptr2 = ptr2.next
            else:
                total = ptr1.val + carry
            sum_val = total % 10
            carry = math.floor(total/10)
            ptr1.val = sum_val

            if ptr1.next == None and carry != 0:
                print(carry)
                ptr1.next = ListNode(carry, None)
                break
            ptr1 = ptr1.next
        
        return ans

    def getlength(self, l1: Optional[ListNode]):
        cur = l1
        size = 0

        while cur != None:
            cur = cur.next
            size = size+1
        return size


        g


        