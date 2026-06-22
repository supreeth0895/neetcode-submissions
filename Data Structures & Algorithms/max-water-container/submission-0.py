class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = -math.inf
        i, j = 0, len(heights)-1
        while i < j:
            max_area = max(max_area, min(heights[i], heights[j])*(j-i))
            if heights[i]> heights[j]:
                j-=1
            else:
                i+=1
        return max_area