class MedianFinder:

    def __init__(self):
        self.q = []
        self.total_nums = 0
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.q,num)
        self.total_nums = self.total_nums +1
        
        

    def findMedian(self) -> float:
        vals =[]
        if self.total_nums %2 != 0:
            for i in range(0, self.total_nums//2 +1):
                vals.append(heapq.heappop(self.q))
            median = vals[len(vals)-1]
            for val in vals:
                heapq.heappush(self.q,val)
            
            return median
        else:
            for i in range(0, self.total_nums//2+1):
                vals.append(heapq.heappop(self.q))
            median = (vals[len(vals)-1] + vals[len(vals)-2])/2
            for val in vals:
                heapq.heappush(self.q,val)
            
            return median

                

                    







        
        