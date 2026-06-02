#Use this approach. Solution in video is confusing.
class Solution:
    """
    Largest Rectangle in Histogram

    Approach:
    - For each bar, find:
        1. The nearest smaller bar on the left.
        2. The nearest smaller bar on the right.
    - These boundaries determine the widest rectangle for which the
      current bar is the minimum height.
    - The width of the rectangle is:
          right_boundary - left_boundary + 1
    - Compute the area for every bar and return the maximum.

    Time Complexity: O(n)
        Each index is pushed to and popped from the stack at most once.

    Space Complexity: O(n)
        For the stacks and boundary arrays.
    """

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        # leftMost[i] stores the index of the nearest bar
        # strictly smaller than heights[i] on the left.
        # If none exists, it remains -1.
        leftMost = [-1] * n

        for i in range(n):
            # Remove bars that are greater than or equal to the current bar
            # since they cannot be the nearest smaller element.
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            # Top of stack is now the nearest smaller bar on the left.
            if stack:
                leftMost[i] = stack[-1]

            # Add current index to the monotonic increasing stack.
            stack.append(i)

        stack = []

        # rightMost[i] stores the index of the nearest bar
        # strictly smaller than heights[i] on the right.
        # If none exists, it remains n.
        rightMost = [n] * n

        for i in range(n - 1, -1, -1):
            # Remove bars that are greater than or equal to the current bar
            # since they cannot be the nearest smaller element.
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            # Top of stack is now the nearest smaller bar on the right.
            if stack:
                rightMost[i] = stack[-1]

            # Add current index to the monotonic increasing stack.
            stack.append(i)

        maxArea = 0

        for i in range(n):
            # Convert nearest-smaller indices into actual rectangle boundaries.
            leftMost[i] += 1
            rightMost[i] -= 1

            # Width of the largest rectangle where heights[i]
            # is the limiting (minimum) height.
            width = rightMost[i] - leftMost[i] + 1

            # Compute area and update answer.
            maxArea = max(maxArea, heights[i] * width)

        return maxArea