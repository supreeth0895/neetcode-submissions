class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = set()

        def backtrack(index, subset, cur_sum):
            if cur_sum > target:
                return
            if cur_sum == target:
                answer.add(tuple(subset))
                return
            if index == len(candidates):
                return
            
            # Case 1: Use the current candidate - This is the path where we consider one or more repitions
            subset.append(candidates[index])
            backtrack(index + 1, subset, cur_sum + candidates[index])
            subset.pop()

            # Case 2: Skip the current candidate and all identical successors - If we don't have the while loop, it works as well, but we get TLE.
            #This is the path where we skip the candidate.
            next_index = index + 1
            while next_index < len(candidates) and candidates[next_index] == candidates[index]:
                next_index += 1
            backtrack(next_index, subset, cur_sum)

        candidates.sort()
        backtrack(0, [], 0)

        ret = []
        for tup in answer:
            ret.append(list(tup))
        return ret

# 1 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3

#                                         []
#                     []                                          [1]
#             []                  [2]
#         []      [2]