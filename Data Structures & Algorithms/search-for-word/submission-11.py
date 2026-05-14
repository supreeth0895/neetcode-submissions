class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(cur_row, cur_col, cur_index, visited):
            nonlocal answer
            if answer:
                return
            if cur_row >= len(board) or cur_row < 0 or cur_col >= len(board[0]) or cur_col < 0:
                return
            if (cur_row, cur_col) in visited:
                return
            
            if board[cur_row][cur_col] == word[cur_index]:
                visited.add((cur_row, cur_col))
                if cur_index + 1 == len(word):
                    answer = True
                    return
                
                backtrack(cur_row+1, cur_col, cur_index+1, visited)
                backtrack(cur_row, cur_col+1, cur_index+1, visited)
                backtrack(cur_row-1, cur_col, cur_index+1, visited)
                backtrack(cur_row, cur_col-1, cur_index+1, visited)
                visited.remove((cur_row, cur_col))
        
        answer = False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if not answer:
                    backtrack(r, c, 0, set())
        return answer