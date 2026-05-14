# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None:
            return
        if head.next == None:
            return


        #Find middle of the list to split into head and head2
        slow_ptr = head
        fast_ptr = head
        while fast_ptr.next.next != None:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            if fast_ptr.next == None:
                break
            
            

        mid = slow_ptr
        head2 = mid.next
        mid.next = None

        print("head2", head2.val)

        #now reverse head2:
        prev = None
        cur = head2
        next_node = head2.next

        while cur !=None:
            cur.next = prev
            prev = cur
            cur = next_node
            if next_node != None:
                next_node = next_node.next
        
        head2 = prev
        head1 = head


        #now, combine head1 and head2

        cur1 = head1
        cur2 = head2
        print(head1.val, head2.val)

        while cur2 != None:
            next1= cur1.next
            next2 =cur2.next
            cur1.next =cur2
            cur2.next = next1

            cur1 = next1
            cur2 = next2
