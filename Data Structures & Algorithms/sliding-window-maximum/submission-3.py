#SUPREETH
#
# Sliding Window Maximum using a Monotonic Deque.

# Maintains a deque of indices whose corresponding values are in
# decreasing order. The front of the deque always holds the index
# of the maximum element in the current window.

# Time Complexity:  O(n) — each element is added/removed from the deque at most once
# Space Complexity: O(k) — deque holds at most k indices at any time

# Args:
#     nums: List of integers to slide the window over
#     k:    Size of the sliding window

# Returns:
#     List of maximums for each window position
#
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        output = []
        q = deque()      # Monotonic decreasing deque storing indices (not values)
        left_idx = 0     # Left boundary of the current window
        right_idx = 0    # Right boundary of the current window (expanding)

        while right_idx < len(nums):

            # Maintain the monotonic decreasing property:
            # Pop from the back any indices whose values are smaller than
            # the incoming element — they can never be the window maximum
            while q and nums[q[-1]] < nums[right_idx]:
                q.pop()

            # Add the current index to the back of the deque
            q.append(right_idx)

            # Remove left value from window:
            # If the front index is now outside the window, discard it
            if left_idx > q[0]:
                q.popleft()

            # Once we have a full window (right_idx has reached index k-1),
            # record the maximum — it's always at the front of the deque
            if (right_idx + 1) >= k:
                output.append(nums[q[0]])
                left_idx += 1   # Slide the window forward

            right_idx += 1   # Expand the window to the right

        return output