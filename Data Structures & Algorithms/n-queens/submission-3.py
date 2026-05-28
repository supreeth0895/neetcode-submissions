"""
N-Queens Solver: places N queens on an N×N board so none share a row, column, or diagonal.
Recurses row-by-row (one queen per row), so no duplicate solutions are possible.
Time: O(N!), Space: O(N²)
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []

        def helper(row, blocked_locations, queen_locations):
            # Base case: one queen placed in each row — valid solution found
            if row == n:
                answer.append(queen_locations)
                return
            for col in range(n):
                # Skip cells attacked by previously placed queens
                if (row, col) in blocked_locations:
                    continue
                blocked_copy = blocked_locations.copy()
                for idx in range(n):
                    # Block this queen's entire row and column
                    blocked_copy.add((row, idx))
                    blocked_copy.add((idx, col))
                    # Block all four diagonal directions
                    if row + idx < n and col + idx < n:
                        blocked_copy.add((row + idx, col + idx))  # down-right
                    if row + idx < n and col - idx >= 0:
                        blocked_copy.add((row + idx, col - idx))  # down-left
                    if row - idx >= 0 and col + idx < n:
                        blocked_copy.add((row - idx, col + idx))  # up-right
                    if row - idx >= 0 and col - idx >= 0:
                        blocked_copy.add((row - idx, col - idx))  # up-left
                # Place queen at (row, col) and recurse to next row
                helper(row + 1, blocked_copy, queen_locations + [(row, col)])

        # Start at row 0 with no blocked cells and no queens placed
        helper(0, set(), [])

        # Convert (row, col) pairs to board strings
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