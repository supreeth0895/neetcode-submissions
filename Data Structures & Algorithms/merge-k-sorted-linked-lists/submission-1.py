# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Use a min heap to get minvalue of sorted keys. OR just take all keys in an array and sort it. Min heap is actually optional
        q = []

        #Use a Map to store  key(int)-> val(Nodes)
        my_map = {}
        
        for head in lists:
            cur = head
            while cur != None:
                key = cur.val
                heapq.heappush(q, key)
                if key not in my_map:
                    my_map[key] = [cur]
                else:
                    my_map[key].append(cur)
                cur = cur.next
        
        head = None
        cur= head
        
        while q:
            key = heapq.heappop(q)
            nodes = my_map[key]
            len_of_nodes= len(nodes)
            node = nodes[len_of_nodes-1]
            if len_of_nodes > 1:
                nodes = nodes[:len_of_nodes -1]
                my_map[key] = nodes
            else:
                my_map.pop(key)


            node.next = None
            #append to list
            if head == None:
                head = node
                cur = head                
            else:
                cur.next = node
                cur = cur.next
        
        return head


                




        