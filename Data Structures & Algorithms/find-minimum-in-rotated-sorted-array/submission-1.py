class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        min_val = math.inf
        while l<=r:
            if nums[l] < nums[r]:
                min_val = min(min_val, nums[l])
                break
            mid = (l+r)//2
            min_val = min(min_val, nums[mid])
            if nums[r] <= nums[mid]:
                l = mid+1
            elif nums[r] > nums[mid]:
                r = mid-1
        return min_val
