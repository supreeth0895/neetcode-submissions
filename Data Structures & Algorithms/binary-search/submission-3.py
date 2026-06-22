class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.target = target
        self.nums = nums
        return self.bin_search(0, len(nums)-1)
    def bin_search(self, left, right):
        if left>right or right > len(self.nums):
            return -1
        pivot = (left+right)//2
        if self.nums[pivot] > self.target:
            return self.bin_search(left, pivot-1)
        elif self.nums[pivot] < self.target:
            return self.bin_search(pivot+1, right)
        else:
            return pivot
