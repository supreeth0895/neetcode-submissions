class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def backtrack(i, subset_arr):
            if i == len(nums):
                answer.append(subset_arr)
                return
            backtrack(i+1, subset_arr)

            new_subset_arr = subset_arr[:]
            new_subset_arr.append(nums[i])

            backtrack(i+1, new_subset_arr)
        
        backtrack(0, [])
        return answer

    # Optimization: If you Don't want to Copy every time, you can modify same subset array, but after backtrack you should pop.
    # def backtrack(self, i, subset_arr, nums):
    # if i == len(nums):
    #     self.answer.append(subset_arr[:])
    #     return
    # self.backtrack(i+1, subset_arr, nums)

    # subset_arr.append(nums[i])
    # self.backtrack(i+1, subset_arr, nums)
    # subset_arr.pop