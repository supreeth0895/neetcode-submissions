import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = defaultdict(int)
        for number in nums:
            dict1[number]+=1
        res = []
        for key, val in dict1.items():
            res.append((-val, key))
        heapq.heapify(res)
        res1 = []
        for i in range(k):
            res1.append(heapq.heappop(res)[1])
        return res1