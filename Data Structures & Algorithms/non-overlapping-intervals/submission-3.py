class Solution:
    # If overlapping, Compare current interval End to previous End Idx, and remove which ever has larger end index value
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # [1,2],[2,5],[3,4],[4,5]
        intervals.sort()
        end_idx = 1
        cur_interval = intervals[0]
        intervals_deletion_count = 0
        while end_idx < len(intervals):
            if intervals[end_idx][0] < cur_interval[1]:
                intervals_deletion_count = intervals_deletion_count+1
                if intervals[end_idx][1] < cur_interval[1]:
                    cur_interval = intervals[end_idx]
                #Otherwise, we can retain cur_interval value for comparison and move end_idx forward
            else:
                #no overlap, move ahead
                cur_interval = intervals[end_idx]

            end_idx = end_idx+1
        return intervals_deletion_count

                
                









        
