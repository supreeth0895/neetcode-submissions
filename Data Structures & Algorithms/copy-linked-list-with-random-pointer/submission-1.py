#SUPREETH

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head

        #step1 insert node next to each other
        cur = head
        while cur != None:
            new_node = Node(cur.val,None, None)
            temp = cur.next
            cur.next = new_node
            new_node.next = temp
            new_node.random = cur.random
            cur=temp
        
        #step2: fix random pointer values:
        cur = head.next
        while cur != None:
            if cur.random:
                cur.random = cur.random.next
            if cur.next == None:
                break
            cur = cur.next.next
        
        #Step3: seperate the two lists
        ptr1 = head
        ptr2 = head.next
        head2 = ptr2

        while ptr1 != None:
            ptr1.next = ptr1.next.next
            if ptr2.next != None:
                ptr2.next = ptr2.next.next
            else:
                ptr2.next = None
            
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return head2