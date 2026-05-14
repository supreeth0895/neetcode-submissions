# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    #This is optimal solution using min heap - We use Node wrapper to compare nodes.
    #TC - O(nlogk), SC - O(k)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        cur = [None] * len(lists)
        answer = None
        cur= answer

        #Add all heads in min heap
        for head in lists:
            if head != None:
                heapq.heappush(q, NodeWrapper(head))
        
        #Keep Popping the minimum node, and add next of that node into min heap until min heap is empty
        while q:
            node_wrapper = heapq.heappop(q)
            node = node_wrapper.node
            if node.next:
                heapq.heappush(q, NodeWrapper(node.next))
            if not answer:
                node.next = None
                answer = node
                cur = answer
            else:
                node.next = None
                cur.next = node
                cur = cur.next
        
        return answer

        
            
    # #This was my first attempt. I did not know how to write wrapper class. This is not optimal. TC is O(nk) and SC is O(n) . Above is more optimal TC O(n logk) SC - O(k)
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     #Use a min heap to get minvalue of sorted keys. OR just take all keys in an array and sort it. Min heap is actually optional
    #     q = []

    #     #Use a Map to store  key(int)-> val(Nodes)
    #     my_map = {}
        
    #     for head in lists:
    #         cur = head
    #         while cur != None:
    #             key = cur.val
    #             heapq.heappush(q, key)
    #             if key not in my_map:
    #                 my_map[key] = [cur]
    #             else:
    #                 my_map[key].append(cur)
    #             cur = cur.next
        
    #     head = None
    #     cur= head
        
    #     while q:
    #         key = heapq.heappop(q)
    #         nodes = my_map[key]
    #         len_of_nodes= len(nodes)
    #         node = nodes[len_of_nodes-1]
    #         if len_of_nodes > 1:
    #             nodes = nodes[:len_of_nodes -1]
    #             my_map[key] = nodes
    #         else:
    #             my_map.pop(key)


    #         node.next = None
    #         #append to list
    #         if head == None:
    #             head = node
    #             cur = head                
    #         else:
    #             cur.next = node
    #             cur = cur.next
        
    #     return head

   