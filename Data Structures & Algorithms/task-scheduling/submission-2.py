#SUPREETH
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        my_map = {}

        #O(n)
        for task in tasks:
            if task in my_map:
                my_map[task] =  my_map[task] + 1
            else:
                my_map[task] = 1
        

        q = []
        #O(26)
        for key in my_map:
            heapq.heappush(q,(-my_map[key],key))
        
        time = 0
        while len(q) > 0:
            temp = []
            for i in range(0,n + 1):
                if q:
                    val = heapq.heappop(q)
                    if val[0] < -1:
                        temp.append((val[0]+1,val[1]))
                else:
                    if not temp:
                        return time
                time = time+1
            for val in temp:
                heapq.heappush(q,val)
        
        return time