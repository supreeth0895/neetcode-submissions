# Sliding Window Maximum using Block Preprocessing
# Time Complexity:  O(n) — two linear scans to build arrays, one to compute output
# Space Complexity: O(n) — for the two precomputed arrays

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # left_to_right_max[i] = max value from the start of i's block up to index i
        left_to_right_max = [0] * n

        # right_to_left_max[i] = max value from index i to the end of i's block
        right_to_left_max = [0] * n

        # Build left_to_right_max (left to right, reset at each block boundary)
        left_to_right_max[0] = nums[0]
        for i in range(1, n):
            if i % k == 0:
                # Block boundary — restart the max from this element
                left_to_right_max[i] = nums[i]
            else:
                # Extend the max within the current block
                left_to_right_max[i] = max(left_to_right_max[i - 1], nums[i])

        # Build right_to_left_max (right to left, reset at each block boundary)
        right_to_left_max[n - 1] = nums[n - 1]
        for i in range(1, n):
            if (n - 1 - i) % k == 0:
                # Block boundary — restart the max from this element
                right_to_left_max[n - 1 - i] = nums[n - 1 - i]
            else:
                # Extend the max within the current block
                right_to_left_max[n - 1 - i] = max(right_to_left_max[n - i], nums[n - 1 - i])

        # For each window of size k:
        # - right_to_left_max[i]         covers from window start to its block end
        # - left_to_right_max[i+k-1]     covers from block start to window end
        # The true window max is the larger of the two
        output = [0] * (n - k + 1)
        for i in range(n - k + 1):
            output[i] = max(left_to_right_max[i + k - 1], right_to_left_max[i])

        return output