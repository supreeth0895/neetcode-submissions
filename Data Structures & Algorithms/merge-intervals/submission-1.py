class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        intervals.sort()
        cur_interval = intervals[0]
        cur_idx = 1
        while cur_idx < len(intervals):
            if intervals[cur_idx][0] <= cur_interval[1]:
                cur_interval[1] = max(intervals[cur_idx][1], cur_interval[1])
            else:
                answer.append(cur_interval)
                cur_interval = intervals[cur_idx]
            cur_idx = cur_idx+1
        
        answer.append(cur_interval)
        return answer

#Note the above is nlogn. We can do this with O(n) but will nuse up signingficant memeoy, but SC is still O(n)
#So you go over the intervals. have the start_value's min and max values.
#Create an array of size max_start_value min_start_value.
# For every start_value, you would update that index in the array.
# Scan the the array. If val is not 0, some interval starts at i. See if we can merge it, since we will have prev. interval value.