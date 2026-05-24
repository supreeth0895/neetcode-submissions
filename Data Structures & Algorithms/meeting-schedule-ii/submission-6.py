#SUPREETH
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Separate all start and end times into their own lists
        all_meeting_start_points = []
        all_meeting_end_points = []
        for interval in intervals:
            all_meeting_start_points.append(interval.start)
            all_meeting_end_points.append(interval.end)
        
        # Sort both lists so we can process events in chronological order
        all_meeting_start_points.sort()
        all_meeting_end_points.sort()

        cur_meetings_ongoing_count = 0  # how many rooms are in use right now
        meeting_start_idx = 0           # pointer for start times list
        meeting_end_idx = 0             # pointer for end times list
        max_meetings_ongoing = 0        # tracks the peak number of rooms needed

        # Walk through all events using two pointers
        while meeting_end_idx < len(all_meeting_end_points) and meeting_start_idx < len(all_meeting_start_points):
            
            # A new meeting starts before the earliest ongoing meeting ends
            # → we need an extra room
            if all_meeting_start_points[meeting_start_idx] < all_meeting_end_points[meeting_end_idx]:
                cur_meetings_ongoing_count += 1
                max_meetings_ongoing = max(max_meetings_ongoing, cur_meetings_ongoing_count)
                meeting_start_idx += 1
            
            # A meeting ends before (or when) the next one starts
            # → a room is freed up
            else:
                cur_meetings_ongoing_count -= 1
                meeting_end_idx += 1
        
        return max_meetings_ongoing