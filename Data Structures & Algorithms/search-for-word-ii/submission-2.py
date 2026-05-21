class Node:
    def __init__(self, val, children=None, is_last_char=False):
        self.val = val
        self.children = children if children is not None else {}
        self.is_last_char = is_last_char

class Solution:
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

    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        for word in words:
            self.insert(word)
        answer = set()
        def dfs(row, col, cur_node, cur_string, visited):
            if cur_node.is_last_char:
                answer.add(cur_string)
            if row < 0 or col <0 or row >= len(board) or col >= len(board[0]):
                return
            if (row, col) in visited:
                return
            visited.add((row,col))

            

            ch = board[row][col]
            if ch in cur_node.children:
                new_node = cur_node.children[ch]
                new_string = cur_string + ch
                dfs(row+1, col, new_node, new_string,  visited.copy())
                dfs(row-1, col, new_node, new_string, visited.copy())
                dfs(row, col+1, new_node, new_string, visited.copy())
                dfs(row, col-1, new_node, new_string, visited.copy())
 
        
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                dfs(i,j, self.root, "",set())
        return list(answer)
        

        
        
        