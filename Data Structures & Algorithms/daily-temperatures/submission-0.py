class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0]*len(temperatures)
        for idx, elem in enumerate(temperatures):
            if not stack :
                stack.append((elem, idx))
            else:
                while stack and stack[-1][0] < elem:
                    pop_temp, pop_idx = stack.pop()
                    results[pop_idx] = idx-pop_idx
                else:
                    stack.append((elem, idx))
        return results