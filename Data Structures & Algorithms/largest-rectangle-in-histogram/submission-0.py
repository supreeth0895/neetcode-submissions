class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        idx = 0
        for idx, height in enumerate(heights):
            if not stack:
                stack.append((height, idx))
            else:
                prev_idx = idx
                while stack and stack[-1][0] >= height:
                    prev_height, prev_idx = stack.pop()
                    area = max(area, prev_height*(idx-prev_idx))
                stack.append((height, prev_idx))
        idx+=1
        while stack:
            prev_height, prev_idx = stack.pop()
            area = max(area, prev_height*(idx-prev_idx))
        return (area)