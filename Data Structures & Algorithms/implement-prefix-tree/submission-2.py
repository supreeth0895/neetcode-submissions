class Node:
    def __init__(self, val, children=None, is_last_char=False):
        self.val = val
        self.children = children if children is not None else {}
        self.is_last_char = is_last_char
class PrefixTree:
    def __init__(self):
        self.root = Node(-1)
        

    def insert(self, word: str) -> None:
        cur_idx = 0
        cur_node = self.root
        
        while cur_idx < len(word):
            ch = word[cur_idx]
            if ch in cur_node.children:
                cur_node = cur_node.children[ch]
            else:
                new_node = Node(ch)
                cur_node.children[ch] = new_node
                cur_node = new_node
            if cur_idx == len(word)-1:
                cur_node.is_last_char = True
            cur_idx = cur_idx+1

            


    def search(self, word: str) -> bool:
        cur_idx = 0
        cur_node = self.root
        while cur_idx < len(word):
            ch = word[cur_idx]
            if ch in cur_node.children:
                cur_node = cur_node.children[ch]
            else:
                return False
            if cur_idx == len(word) -1:
                if cur_node.is_last_char != True:
                    return False
            cur_idx = cur_idx +1
        return True

        

    def startsWith(self, prefix: str) -> bool:
        cur_idx = 0
        cur_node = self.root
        while cur_idx < len(prefix):
            ch = prefix[cur_idx]
            if ch in cur_node.children:
                cur_node = cur_node.children[ch]
            else:
                return False
            cur_idx = cur_idx +1
        return True