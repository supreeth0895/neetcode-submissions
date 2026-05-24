class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        intervals.sort()
        cur_interval = intervals[0]
        cur_idx = 1
        while cur_idx < len(intervals):
            if intervals[cur_idx][0] <= cur_interval[1]:
                print(intervals[cur_idx][1], cur_interval[1])
                cur_interval[1] = max(intervals[cur_idx][1], cur_interval[1])
            else:
                answer.append(cur_interval)
                cur_interval = intervals[cur_idx]
            cur_idx = cur_idx+1
        
        answer.append(cur_interval)
        return answer
        