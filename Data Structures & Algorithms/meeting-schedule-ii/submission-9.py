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


# #We can also use Heap Approach It's much simpler to code, but same TC, and SC. So feel free to choose either approach

# 1. Sort all meetings by their start time.
# 2. Initialize an empty min heap min_heap to store meeting end times.
# 3. Iterate through each meeting in sorted order:
#         If the heap is not empty and the earliest end time (min_heap[0]) is less than or equal to the current meeting’s start:
#             pop the top of the heap (reuse that room)
#         Push the current meeting’s end time into the heap (occupy a room).
# 4. After processing all meetings start times, the maxsize of the heap at any point, represents the minimum number of rooms required
# 5. Return the maxsize of the heap.

# O(nlogn)
# class Solution:
#     def minMeetingRooms(self, intervals: List[Interval]) -> int:
#         intervals.sort(key=lambda x: x.start)
#         min_heap = []

#         for interval in intervals:
#             if min_heap and min_heap[0] <= interval.start:
#                 heapq.heappop(min_heap)
#             #There could be other rooms we could pop. But we do. not, because for this problem, we care about max rooms at any time
#             #So, We just remove the most earliest given up room and use it for the next meeting. We don't bother to clean up rest of the heap.
#             #This is the reason, we do not have to track max_val at every step. 
#             heapq.heappush(min_heap, interval.end)

#         return len(min_heap)