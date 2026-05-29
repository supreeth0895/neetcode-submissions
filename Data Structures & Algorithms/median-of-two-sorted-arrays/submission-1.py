#SUPREETH

# Finds the median of two sorted arrays in O(log(min(m, n))) time using binary search.

# The core idea: instead of merging both arrays, we binary search for the correct
# "split point" in the smaller array (A) that partitions both arrays into equal
# left/right halves. Once found, the median is derived from the boundary values.

# Args:
#     nums1: First sorted array
#     nums2: Second sorted array

# Returns:
#     The median of the two combined sorted arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Always binary search on the smaller array to minimize iterations
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A

        # Binary search bounds for the split index in A
        left_idx = 0
        right_idx = len(A) - 1

        total_len = len(A) + len(B)
        half_len = total_len // 2  # Number of elements that should be on the left side

        while True:
            # midA: last index of A's left partition (elements going to the left half)
            midA = (left_idx + right_idx) // 2

            # midB: last index of B's left partition, derived so that
            # len(left_A) + len(left_B) == half_len
            # left_A has (midA + 1) elements, so left_B needs (half_len - (midA + 1))
            midB = (half_len - 1) - (midA + 1)

            # --- Boundary values at the edges of each partition ---

            # Largest value in A's left partition (or -inf if A contributes nothing to left)
            left_val_A  = A[midA]      if midA >= 0        else float("-inf")

            # Smallest value in A's right partition (or +inf if A is fully in the left)
            right_val_A = A[midA + 1]  if midA + 1 < len(A) else float("inf")

            # Largest value in B's left partition (or -inf if B contributes nothing to left)
            left_val_B  = B[midB]      if midB >= 0        else float("-inf")

            # Smallest value in B's right partition (or +inf if B is fully in the left)
            right_val_B = B[midB + 1]  if midB + 1 < len(B) else float("inf")

            # --- Check if the partition is valid ---
            # A valid partition requires that every element on the left ≤ every element on
            # the right across both arrays, i.e. the two cross-conditions hold:
            if left_val_A <= right_val_B and left_val_B <= right_val_A:

                # Odd total length: median is the smallest element in the right half
                if total_len % 2 != 0:
                    return min(right_val_A, right_val_B)

                # Even total length: median is the average of the inner two elements
                else:
                    return (max(left_val_A, left_val_B) + min(right_val_A, right_val_B)) / 2

            # A's left partition is too large — move the split point left in A
            elif left_val_A > right_val_B:
                right_idx = midA - 1

            # A's left partition is too small — move the split point right in A
            else:
                left_idx = midA + 1