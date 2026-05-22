#SUPREETH    
# Approach: Use two heaps to maintain a balanced partition of numbers.
# - small_heap: Max-heap (stores negated values) for lower half of numbers
# - large_heap: Min-heap (stores actual values) for upper half of numbers
# Maintain invariant: all values in small_heap <= all values in large_heap
# Keep sizes balanced so we can quickly find the median.

class MedianFinder:




    def __init__(self):
        self.large_heap = []  # Min-heap for upper half (stores positive values)
        self.small_heap = []  # Max-heap for lower half (stores negated values)
        

    def addNum(self, num: int) -> None:
        # Case 1: Both heaps exist
        if len(self.large_heap) > 0 and len(self.small_heap) > 0:    
            # Compare negated num with top of small_heap (which stores negated values)
            if -num >= self.small_heap[0]:
                heapq.heappush(self.small_heap, -num)
            else:
                heapq.heappush(self.large_heap, num)
        
        # Case 2: Both heaps are empty
        elif len(self.large_heap) == 0 and len(self.small_heap) == 0:
            heapq.heappush(self.small_heap, -num)
        
        # Case 3: Only small_heap exists
        elif len(self.large_heap) == 0 and len(self.small_heap) > 0:
            if -num >= self.small_heap[0]:
                heapq.heappush(self.small_heap, -num)
            else:
                heapq.heappush(self.large_heap, num)
        
        # Case 4: Only large_heap exists
        else:
            if num < self.large_heap[0]:
                heapq.heappush(self.large_heap, num)
            else:
                heapq.heappush(self.small_heap, -num)

        # Balance heaps: large_heap should not be more than 1 larger than small_heap
        while len(self.large_heap) - len(self.small_heap) > 1:
            # Move from large_heap to small_heap (negate to convert back)
            heapq.heappush(self.small_heap, -1 * heapq.heappop(self.large_heap))
        
        # Balance heaps: small_heap should not be more than 1 larger than large_heap
        while len(self.small_heap) - len(self.large_heap) > 1:
            # Move from small_heap to large_heap (negate to store as positive)
            heapq.heappush(self.large_heap, -1 * heapq.heappop(self.small_heap))        

    def findMedian(self) -> float:
        # If equal sizes, return average of both tops
        if len(self.small_heap) == len(self.large_heap):
            return (-1 * self.small_heap[0] + self.large_heap[0]) / 2
        
        # If small_heap is larger, its top is the median
        elif len(self.small_heap) > len(self.large_heap):
            return -self.small_heap[0]
        
        # If large_heap is larger, its top is the median
        else:
            return self.large_heap[0]


# A Crude approach I had come up with initially - 1 heap. Very bad TC for many findMedian
# class MedianFinder:

#     def __init__(self):
#         self.q = []
#         self.total_nums = 0
        

#     def addNum(self, num: int) -> None:
#         heapq.heappush(self.q,num)
#         self.total_nums = self.total_nums +1
        
        

#     def findMedian(self) -> float:
#         vals =[]
#         if self.total_nums %2 != 0:
#             for i in range(0, self.total_nums//2 +1):
#                 vals.append(heapq.heappop(self.q))
#             median = vals[len(vals)-1]
#             for val in vals:
#                 heapq.heappush(self.q,val)
            
#             return median
#         else:
#             for i in range(0, self.total_nums//2+1):
#                 vals.append(heapq.heappop(self.q))
#             median = (vals[len(vals)-1] + vals[len(vals)-2])/2
#             for val in vals:
#                 heapq.heappush(self.q,val)
            
#             return median

                