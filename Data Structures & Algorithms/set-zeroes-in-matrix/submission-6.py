# SUPREETH

# Set Matrix Zeroes (In-Place, O(1) Space)

# Uses the first row and first column as markers to track which rows/columns
# need to be zeroed. Two boolean flags handle the first row and column themselves,
# since they double as the marker space.

# Approach:
#   1. Check if the first row/column originally contain any zeros (save as flags).
#   2. Scan the rest of the matrix; for any zero found, mark its row and column
#      via the first column and first row respectively.
#   3. Use those markers to zero out the interior (rows/cols 1+).
#   4. Apply the flags to zero the first row and/or column if needed.

# Time:  O(m * n)
# Space: O(1)


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        # --- Step 1: Record whether the first row/column need to be zeroed ---
        # We check these upfront because we're about to overwrite them with markers.

        first_col_has_zero = False
        first_row_has_zero = False

        for i in range(0, len(matrix)):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        for i in range(0, len(matrix[0])):
            if matrix[0][i] == 0:
                first_row_has_zero = True
                break

        # --- Step 2: Use first row/column as markers ---
        # For every zero found, mark its row via matrix[i][0]
        # and its column via matrix[0][j].

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0   # mark this row
                    matrix[0][j] = 0   # mark this column

        # --- Step 3: Zero out interior cells using the markers ---
        # A cell (i, j) should be zero if its row or column is marked.

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # --- Step 4: Apply the saved flags to the first row and column ---
        # These couldn't use the marker system since they ARE the marker system.

        if first_col_has_zero:
            for i in range(0, len(matrix)):
                matrix[i][0] = 0

        if first_row_has_zero:
            for i in range(0, len(matrix[0])):
                matrix[0][i] = 0