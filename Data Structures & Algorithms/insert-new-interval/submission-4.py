#SUPREETH
#MergeIntervals.
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        if len(newInterval) == 0:
            return intervals

        new_intervals = []
        #Add new interval into 1 array which is sorted
        for interval in intervals:
            if newInterval[0] < interval[0]:
                new_intervals.append(newInterval)
            new_intervals.append(interval)
        
        if len(intervals) == len(new_intervals):
            #To be appended at the end
            new_intervals.append(newInterval)

        ##MergeIntervals
        answer = []
        cur_interval = new_intervals[0]
        cur_idx = 1
        while cur_idx < len(new_intervals):
            if new_intervals[cur_idx][0] <= cur_interval[1]:
                print(new_intervals[cur_idx][1], cur_interval[1])
                cur_interval[1] = max(new_intervals[cur_idx][1], cur_interval[1])
            else:
                answer.append(cur_interval)
                cur_interval = new_intervals[cur_idx]
            cur_idx = cur_idx+1
        
        answer.append(cur_interval)
        return answer







        
        