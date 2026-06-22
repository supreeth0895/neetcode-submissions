class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = defaultdict(int)
        for elem in nums:
            dict1[elem]+=1
        heap = []
        for key, val in dict1.items():
            heap.append((-val, key))
        res = []
        heapq.heapify(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return (res)