#SUPREETH
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Monotonic increasing stack approach.
        # We maintain a stack of (start_index, height) pairs in increasing height order.
        # When we encounter a bar shorter than the stack top, we pop all taller bars
        # and compute their rectangle areas (height × width, where width stretches from
        # the bar's stored start index to the current position). The popped bar's start
        # index is inherited by the current shorter bar, since it could have begun there.
        # A sentinel 0 is appended to heights to flush all remaining bars at the end.
        # Time: O(n) — each bar is pushed and popped at most once.
        # Space: O(n) — stack holds at most n bars.

        st = []        # monotonic increasing stack of (start_index, height)
        max_area = 0
        heights.append(0)  # sentinel: forces all remaining bars to be popped at the end

        for cur_idx in range(0, len(heights)):
            idx = cur_idx
            val = heights[cur_idx]

            if st and st[-1][1] > val:
                # Current bar is shorter than the top of the stack,
                # so pop all taller bars — their rectangles can't extend further right
                while st and st[-1][1] > val:
                    idx, popped_elem = st.pop()
                    # Width = distance from this bar's original start to current position
                    max_area = max(max_area, popped_elem * (cur_idx - idx))

                # Push current bar, but extend it left to where we started popping —
                # since this shorter bar could have started there
                st.append((idx, val))
            else:
                # Current bar is >= top of stack, so the stack stays increasing.
                # Push normally with its own index as the start
                st.append((cur_idx, val))

        return max_area