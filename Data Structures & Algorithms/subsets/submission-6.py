class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        # def backtrack(i, subset_arr):
        #     if i == len(nums):
        #         answer.append(subset_arr)
        #         return
        #     backtrack(i+1, subset_arr)

        #     new_subset_arr = subset_arr[:]
        #     new_subset_arr.append(nums[i])

        #     backtrack(i+1, new_subset_arr)


        def backtrack(i, subset_arr):
            if i == len(nums):
                answer.append(subset_arr[:])
                return
            backtrack(i+1, subset_arr)

            subset_arr.append(nums[i])
            backtrack(i+1, subset_arr)
            subset_arr.pop()
        
        backtrack(0, [])
        return answer

    # Optimization: If you Don't want to Copy every time, you can modify same subset array, but after backtrack you should pop.
        # def backtrack(i, subset_arr):
        # if i == len(nums):
        #     answer.append(subset_arr[:])
        #     return
        # backtrack(i+1, subset_arr, nums)

        # subset_arr.append(nums[i])
        # backtrack(i+1, subset_arr)
        # subset_arr.pop()