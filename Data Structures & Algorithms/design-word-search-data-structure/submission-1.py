class Node:
    def __init__(self, val, children=None, is_last_char=False):
        self.val = val
        self.children = children if children is not None else {}
        self.is_last_char = is_last_char

class WordDictionary:

    def __init__(self):
        self.root = Node(-1)
        

    def addWord(self, word: str) -> None:
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
        def backtrack(cur_idx, cur_node):
            if cur_idx == len(word):
                if cur_node.is_last_char :
                    return True
                else:
                    return False
            
            ch = word[cur_idx]
            if ch != '.':
                if ch not in cur_node.children:
                    return False
                else:
                    val = backtrack (cur_idx+1,cur_node.children[ch])                
                    return val
            else:
                for key in cur_node.children:
                    val = backtrack (cur_idx+1,cur_node.children[key])
                    if val:
                        return True

            return False

        return backtrack(0,self.root)



        
