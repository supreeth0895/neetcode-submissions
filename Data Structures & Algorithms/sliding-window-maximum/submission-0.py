class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        left_idx = 0
        right_idx = 0
        while right_idx < len(nums):
            while q and nums[q[len(q)-1]] < nums[right_idx]:
                q.pop()
            q.append(right_idx)

            #remove left value from windoe

            if left_idx > q[0]:
                q.popleft()
            
            if (right_idx+1) >= k:
                output.append(nums[q[0]])
                left_idx = left_idx+1
            right_idx = right_idx+1
        return output

        