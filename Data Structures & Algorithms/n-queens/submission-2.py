class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []

        def helper(row, blocked_locations, queen_locations):
            if row == n:
                answer.append(queen_locations)
                return
            for col in range(n):
                if (row, col) in blocked_locations:
                    continue
                blocked_copy = blocked_locations.copy()
                for idx in range(n):
                    blocked_copy.add((row, idx))
                    blocked_copy.add((idx, col))
                    if row + idx < n and col + idx < n:
                        blocked_copy.add((row + idx, col + idx))
                    if row + idx < n and col - idx >= 0:
                        blocked_copy.add((row + idx, col - idx))
                    if row - idx >= 0 and col + idx < n:
                        blocked_copy.add((row - idx, col + idx))
                    if row - idx >= 0 and col - idx >= 0:
                        blocked_copy.add((row - idx, col - idx))
                helper(row + 1, blocked_copy, queen_locations + [(row, col)])

        helper(0, set(), [])

        ret_val = []
        for queens in answer:
            board = []
            for i in range(n):
                row = ""
                for j in range(n):
                    row += "Q" if (i, j) in queens else "."
                board.append(row)
            ret_val.append(board)
        return ret_val