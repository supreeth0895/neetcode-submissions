class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        max_area = 0
        heights.append(0)
        for cur_idx in range(0, len(heights)):
            idx = cur_idx
            val  = heights[cur_idx]
            if st and st[-1][1] > val: 
                while st and st[-1][1] > val:
                    idx, popped_elem = st.pop()
                    max_area = max(max_area, popped_elem * (cur_idx - idx))
                st.append((idx, val))
            else:
                st.append((cur_idx, val))
        return max_area

        