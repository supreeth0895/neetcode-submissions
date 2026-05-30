class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        
        queries_sorted = queries[:]
        
        queries_sorted.sort()
        print(intervals)
        print(queries_sorted)
        cur_idx = 0
        pq= []
        answer_map  = {}
        for query in queries_sorted:
            if query in answer_map:
                continue
            while cur_idx < len(intervals) and intervals[cur_idx][0] <= query:
                val = intervals[cur_idx][1] - intervals[cur_idx][0] + 1
                heapq.heappush(pq, (val, intervals[cur_idx][1]))
                cur_idx = cur_idx+1
                print(cur_idx)
            print("PQ:",pq)
            
            while pq:
                if query > pq[0][1]:
                    heapq.heappop(pq)
                else:
                    answer_map[query] = pq[0][0]
                    break
        answer = []
        print(answer_map)
        for query in queries:
            if query in answer_map:
                answer.append(answer_map[query])
            else:
                answer.append(-1)
        
        return answer


            
            
                
            

            





        