class Solution:
    def __init__(self):
        self.answer = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset_arr = []
        i = 0
        self.backtrack(i, subset_arr, nums)
        return self.answer

    def backtrack(self, i, subset_arr, nums):
        if i == len(nums):
            self.answer.append(subset_arr[:])
            return
        self.backtrack(i+1, subset_arr, nums)

        subset_arr.append(nums[i])
        self.backtrack(i+1, subset_arr, nums)
        subset_arr.pop()