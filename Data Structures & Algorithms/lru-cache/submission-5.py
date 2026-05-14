class Node:
    def __init__(self, key, val=0, next=None, prev= None):
        self.key = key
        self.val = val
        self.next=next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1,-1)
        self.last = self.head
        self.my_map = {}
        self.capacity = capacity
        self.cur_size = 0
        

    def get(self, key: int) -> int:
        if key in self.my_map:
            # Move that Node to the Rear of list
            node_to_be_moved = self.my_map[key]
            if node_to_be_moved != self.last:
                #delete that node from linked list
                node_to_be_moved.prev.next = node_to_be_moved.next
                node_to_be_moved.next.prev = node_to_be_moved.prev

                #insert rear
                self.last.next = node_to_be_moved
                node_to_be_moved.prev = self.last
                self.last = node_to_be_moved
                node_to_be_moved.next = None
            return self.my_map[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.my_map:
            if self.cur_size == self.capacity:
                #delete front
                node_to_be_removed = self.head.next
                self.head.next = self.head.next.next
                if self.head.next:
                    self.head.next.prev = self.head
                key_to_be_removed  = node_to_be_removed.key
                self.my_map.pop(key_to_be_removed)
                self.cur_size = self.cur_size -1
            #insert rear
            new_node = Node(key, value)
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node
            self.my_map[key] = new_node
            self.cur_size = self.cur_size + 1
        else:
            self.my_map[key].val = value
            # Move that Node to the Rear of list
            self.get(key)