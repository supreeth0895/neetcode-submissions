class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q =[]
        for stone in stones:
            heapq.heappush(q, -stone)
        while len(q) > 1:
            val1 = heapq.heappop(q)
            val2 = heapq.heappop(q)
            heapq.heappush(q, val1-val2)
        
        return -q[0]


        