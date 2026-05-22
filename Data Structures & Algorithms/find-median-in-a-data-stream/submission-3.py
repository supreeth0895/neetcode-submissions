class MedianFinder:

    def __init__(self):
        self.large_heap = []
        self.small_heap = []
        

    def addNum(self, num: int) -> None:
        if len(self.large_heap) > 0 and len(self.small_heap) > 0:    
            if -num >= self.small_heap[0]:
                heapq.heappush(self.small_heap, -num)
            else:
                heapq.heappush(self.large_heap, num)
        elif len(self.large_heap) == 0 and len(self.small_heap) == 0:
            heapq.heappush(self.small_heap, -num)
        elif len(self.large_heap) == 0 and len(self.small_heap) > 0:
            if -num >= self.small_heap[0]:
                heapq.heappush(self.small_heap, -num)
            else:
                heapq.heappush(self.large_heap, num)
        else:
            if num < self.large_heap[0]:
                heapq.heappush(self.large_heap, num)
            else:
                heapq.heappush(self.small_heap, -num)


        
        while len(self.large_heap) -  len(self.small_heap) > 1:
            heapq.heappush(self.small_heap, -1* heapq.heappop(self.large_heap))
        
        while len(self.small_heap) -  len(self.large_heap) > 1:
            heapq.heappush(self.large_heap, -1* heapq.heappop(self.small_heap))        

    def findMedian(self) -> float:
        if len(self.small_heap) == len(self.large_heap):
            return (-1*self.small_heap[0] + (self.large_heap[0]))/2
        elif len(self.small_heap) > len(self.large_heap):
            return -self.small_heap[0]
        else:
            return self.large_heap[0]


        


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

                