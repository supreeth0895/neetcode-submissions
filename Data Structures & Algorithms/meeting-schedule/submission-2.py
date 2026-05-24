"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def get_start(self, interval):
        return interval.start
    
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=self.get_start)
        if len(intervals) == 0:
            return True
        cur_interval = intervals[0]
        end_idx = 1
        while end_idx < len(intervals):
            if cur_interval.end > intervals[end_idx].start:
                return False
            else:
                cur_interval = intervals[end_idx]
                end_idx = end_idx+1
        return True


            


