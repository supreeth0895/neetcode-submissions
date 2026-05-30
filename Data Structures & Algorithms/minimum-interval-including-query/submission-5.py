#SUPREETH
# """
# Minimum Interval to Include Each Query
# ---------------------------------------
# Problem:
#     Given a list of intervals [left, right] and a list of queries, for each query
#     return the size of the smallest interval that contains the query value.
#     Interval size = right - left + 1. Return -1 if no such interval exists.

# Approach: Offline Sweep with Min-Heap
#     1. Sort intervals by start point.
#     2. Sort queries (while preserving original indices via a copy).
#     3. Sweep through sorted queries. For each query:
#        - Add all intervals whose start <= query into a min-heap keyed by interval size.
#        - Pop intervals from the heap whose end < query (they can't contain this query).
#        - The heap's top is the smallest valid interval for this query.
#     4. Use a hash map to cache results for duplicate queries.
#     5. Reconstruct answers in the original query order.

# Complexity:
#     Time:  O((N + Q) log N) — sorting + heap ops
#     Space: O(N + Q)         — heap + answer map
# """

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals by their start point so we can sweep left-to-right
        intervals.sort()

        # Work on a sorted copy of queries; keep originals for output ordering
        queries_sorted = queries[:]
        queries_sorted.sort()

        print(intervals)
        print(queries_sorted)

        cur_idx = 0          # Pointer into sorted intervals
        pq = []              # Min-heap of (interval_size, interval_end)
        answer_map = {}      # Cache: query value -> smallest interval size

        for query in queries_sorted:
            # Skip duplicate query values — already computed
            if query in answer_map:
                continue

            # Push all intervals that have started by this query point onto the heap
            while cur_idx < len(intervals) and intervals[cur_idx][0] <= query:
                val = intervals[cur_idx][1] - intervals[cur_idx][0] + 1  # interval size
                heapq.heappush(pq, (val, intervals[cur_idx][1]))         # (size, end)
                cur_idx += 1
                print(cur_idx)

            print("PQ:", pq)

            # Remove intervals from the heap that have already ended before this query
            while pq:
                if query > pq[0][1]:         # Heap top's end is before the query
                    heapq.heappop(pq)
                else:
                    # Smallest valid interval found — record it and stop pruning
                    answer_map[query] = pq[0][0]
                    break
            # If the heap is empty here, this query has no covering interval (-1 by default)

        # Reconstruct answers in the original query order
        answer = []
        print(answer_map)
        for query in queries:
            if query in answer_map:
                answer.append(answer_map[query])
            else:
                answer.append(-1)   # No interval covers this query

        return answer