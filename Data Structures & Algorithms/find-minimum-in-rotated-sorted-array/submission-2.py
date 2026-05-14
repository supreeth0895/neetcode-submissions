class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        total_len = len(nums)


        while start <= end:
            mid = math.trunc((start+ end)/2)
            if nums[mid] > nums[(mid-1)%total_len] and nums[mid] > nums[(mid+1)%total_len]:
                return nums[(mid+1)%total_len]
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid+1
        
        return nums[0]