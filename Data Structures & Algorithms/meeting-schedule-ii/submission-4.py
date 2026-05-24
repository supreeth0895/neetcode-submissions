"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def get_key(self, interval):
        return interval.start
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        all_meeting_start_points = []
        all_meeting_end_points = []
        for interval in intervals:
            all_meeting_start_points.append(interval.start)
            all_meeting_end_points.append(interval.end)
        all_meeting_start_points.sort()
        all_meeting_end_points.sort()

        print(all_meeting_start_points,all_meeting_end_points )

        cur_meetings_ongoing_count = 0
        meeting_start_idx = 0
        meeting_end_idx = 0
        max_meetings_ongoing = 0
        while meeting_end_idx < len(all_meeting_end_points) and meeting_start_idx < len(all_meeting_start_points):
            if all_meeting_start_points[meeting_start_idx] < all_meeting_end_points[meeting_end_idx]:
                cur_meetings_ongoing_count = cur_meetings_ongoing_count+1
                max_meetings_ongoing = max(max_meetings_ongoing, cur_meetings_ongoing_count)
                meeting_start_idx = meeting_start_idx+1
            else:
                cur_meetings_ongoing_count = cur_meetings_ongoing_count-1
                meeting_end_idx = meeting_end_idx+1
        
        return max_meetings_ongoing
